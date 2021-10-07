### Dockerfile
> [Awesome dbt dockerfile](/.docker/awesome-dbt.dockerfile)

### Build image:latest
```
docker rm awesome-dbt
docker rmi tuiladat/awesome-dbt
docker build --tag tuiladat/awesome-dbt:latest . -f ./.docker/awesome-dbt.dockerfile
```

### Run containter
```
docker rm awesome-dbt
docker run --publish 8000:8000 --name "awesome-dbt" tuiladat/awesome-dbt
```


### Publish to Hub
```
docker push tuiladat/awesome-dbt:latest
```
