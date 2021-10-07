# Requirements:
- python >=3.7.x
- dbt >=0.20.2


# Getting ready?

## Install the Microsoft ODBC driver for SQL Server (Linux only)
[Here](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)

## Install dbt & the mssql plugin
Installed version: `dbt 0.20.2`
Plugins - `sqlserver: 0.20.1`

- Windows:
```
python -m venv env
.\env\Scripts\activate
python -m pip install --upgrade pip==21.2.4
python -m pip install -r requirements.txt
```

- Linux (Recommend to install WSL if you're in Windows):
```
sudo apt-get update && apt install -y curl gnupg2
# apt-get install python3.7-venv
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```


## Create dbt profile for SQL Server with 10 threads
- Windows:
```
mkdir "%userprofile%/.dbt" 
xcopy ".dbt_profiles.yml" "%userprofile%/.dbt/profiles.yml" /Y
dbt deps --project-dir ./dbt
```

- Linux:
```
mkdir ~/.dbt
cp ".dbt_profiles.yml" ~/.dbt/profiles.yml /Y
dbt deps --project-dir ./dbt
```

Find [mssql-profile](https://docs.getdbt.com/reference/warehouse-profiles/mssql-profile) for more options


## Install dbt packages 
You will find the basic packages in [packages.yml](packages.yml)
```
dbt deps --project-dir ./dbt
```

## Let's run the first model
```
dbt run --project-dir ./dbt --target dev --models MyFirstModel
```

Off we go!
```
Running with dbt=0.20.2
Found 1 model, 2 tests, 0 snapshots, 0 analyses, 448 macros, 0 operations, 1 seed file, 0 sources, 0 exposures

12:37:53 | Concurrency: 10 threads (target='dev')
12:37:53 | 
12:37:53 | 1 of 1 START table model dbo.MyFirstModel............................ [RUN]
12:38:00 | 1 of 1 OK created table model dbo.MyFirstModel....................... [OK in 7.34s]
12:38:00 | 
12:38:00 | Finished running 1 table model in 7.55s.

Completed successfully

Done. PASS=1 WARN=0 ERROR=0 SKIP=0 TOTAL=1
```