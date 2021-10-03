from enum import Enum
import json
import os
import subprocess
import prefect
from prefect import Flow, Task
from prefect.triggers import all_successful
from queue import Queue
import threading
from config import DBT_SINGLETON

class DbtAction(Enum):
    DEPS = 'deps'
    RUN = 'run'
    SEED = 'seed'
    TEST = 'test'
    RUN_OPERATION = 'run-operation'


class DBT():
    def __init__(self,
        action: str = DbtAction.RUN,
        macro: str = None,
        macro_args: dict = None,
        profiles_dir: str = None,
        target: str = None,
        project_dir: str = '.',
        vars: dict = None,
        models: str = None,
        full_refresh: bool = False
    ) -> None:
        self.action = action
        self.macro = macro
        self.macro_args = macro_args
        self.profiles_dir = profiles_dir
        self.target = target
        self.project_dir = project_dir
        self.vars = vars
        self.models = models
        self.full_refresh = full_refresh
    
    
    def build(self, *args, **kwargs):
        """
        Build args
        """
        arguments = [self.action.value]

        # Standard arguments
        if self.macro is not None:
            arguments.extend([self.macro])

            if self.macro_args is not None:
                arguments.extend(["--args", json.dumps(self.macro_args)])

        if self.target is not None:
            arguments.extend(["--target", self.target])

        if self.profiles_dir is not None:
            arguments.extend(["--profiles-dir", self.profiles_dir])

        if self.project_dir is not None:
            arguments.extend(["--project-dir", self.project_dir])

        if self.vars is not None:
            arguments.extend(["--vars", json.dumps(self.vars)])

        if self.models is not None:
            arguments.extend(["--models", self.models])

        if self.full_refresh:
            arguments.extend(["--full-refresh"])

        # Additional non-keyword arguments
        if args is not None:
            for arg in args:
                arguments.extend([arg])

        # Additional keyword arguments
        if kwargs is not None:
            for key, value in kwargs.items():
                arguments.extend([key, value])

        return arguments


class DbtTask(Task):
    def run(self, instance: DBT):
        logger = prefect.context.get("logger")
        dbt_cmd = ["dbt"]
        dbt_cmd.extend(instance.build())
        logger.info(dbt_cmd)
        sp = subprocess.Popen(
            dbt_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=os.getcwd(),
            close_fds=True
        )
        for line in iter(sp.stdout.readline, b''):
            line = line.decode('utf-8').rstrip()
            logger.info(line)
        sp.wait()
        if sp.returncode != 0:
            raise prefect.engine.signals.FAIL()

        return (
            f"Command exited with return code {sp.returncode}",
            sp.returncode == 0
        )
        

class DbtExec():
    def __init__(self, singleton: bool = True) -> None:
        self.singleton = singleton
        self.queue = Queue(maxsize=100) # Config max size
        if self.singleton:
            threading.Thread(target=self.__worker__, daemon=True).start()


    def __worker__(self):
        """"
        Queue worker
        """
        while True:
            flow = self.queue.get()
            print(f'Working on {flow}')
            flow.run()
            print(f'Finished {flow}')
            self.queue.task_done()


    def execute(self,
        flow_name: str = "Execution of dbt series | execute",
        dbts: list = []
    ):
        """
        General dbt execution
        """
        dbt_tasks = [DbtTask() for x in dbts]
        with Flow(name=flow_name) as f:
            prev_task = None
            for idx, dbt in enumerate(dbts):
                task = f.add_task(dbt_tasks[idx](instance=dbt))
                if prev_task is not None:
                    task.set_dependencies(upstream_tasks=[prev_task])
                prev_task = task

        if self.singleton:
            self.queue.put(f)
            return "Task queued"

        return f.run()

instance = DbtExec(singleton=DBT_SINGLETON)