# Awesome dbt
This is the data services via API Endpoint

### DEV
- [Optional] Set the `python` alias (if Linux)
```
update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
python --version
```
- [Install dbt & activate env](../../LOCALDEV.md)


#### Start service locally
```
set env_sqlserver_user_secret=datnguye
set env_sqlserver_password_secret=datnguye
set env_sqlserver_host_secret=DAT\DAT19
uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir "./services/api_service" --reload
```

- To see the API document: http://127.0.0.1:8000/docs
- To see the Open API document: http://127.0.0.1:8000/redoc


