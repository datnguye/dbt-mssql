### Dockerfile
> [dbt provision dockerfile](/.docker/provision.dockerfile)

### Build image:latest
```
# docker rmi tuiladat/dbt-mssql-provision
docker build --tag tuiladat/dbt-mssql-provision:latest . -f ./.docker/provision.dockerfile
```

### Run containter
```
# remove exists container:
docker rm dbt-mssql-provision

# run with default arguments
docker run --name "dbt-mssql-provision" tuiladat/dbt-mssql-provision

# run with all models
docker run --name "dbt-mssql-provision" --env MODELS="+exposure:*" tuiladat/dbt-mssql-provision

```


### Publish to Hub
```
docker push tuiladat/dbt-mssql-provision:latest
```
