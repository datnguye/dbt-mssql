### Dockerfile
> [dbt processing dockerfile](/.docker/processing.dockerfile)

### Build image:latest
```
# docker rmi tuiladat/dbt-mssql-processing
docker build --tag tuiladat/dbt-mssql-processing:latest . -f ./.docker/processing.dockerfile
```

### Run containter
```
# remove exists container:
docker rm dbt-mssql-processing

# run with default arguments
docker run --name "dbt-mssql-processing" tuiladat/dbt-mssql-processing

# run with all models
docker run --name "dbt-mssql-processing" --env MODELS="+exposure:*" tuiladat/dbt-mssql-processing

# test with all models
docker run --name "dbt-mssql-processing" --env OP="test" --env MODELS="+exposure:*" tuiladat/dbt-mssql-processing
```


### Publish to Hub
```
docker push tuiladat/dbt-mssql-processing:latest
```
