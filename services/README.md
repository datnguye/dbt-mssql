# SERVICES
This is the data services

## Api service
Root folder [Here](apis)

#### Start service
```
uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir "./services/apis" --reload
```

- To see the API document: http://127.0.0.1:8000/docs
- To see the Open API document: http://127.0.0.1:8000/redoc




## Other Notes
- Set the `python` alias
```
update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
python --version
```