# SERVICES
This is the data services

## dbt Api service
Root folder [Here](apis)

### DEV
- Set the `python` alias (if Linux)
```
update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
python --version
```
- [Install dbt](TBU)
- Activate venv, install [requirements]()

#### Start service locally
```
uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir "./services/api_service" --reload
```

- To see the API document: http://127.0.0.1:8000/docs
- To see the Open API document: http://127.0.0.1:8000/redoc


