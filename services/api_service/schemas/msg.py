from pydantic import BaseModel

class Msg(BaseModel):
    msg: str


class TaskMsg(BaseModel):
    taskid: str
    msg: str