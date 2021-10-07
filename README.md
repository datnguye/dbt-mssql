# dbt-mssql
This is where to start the data transformation with dbt and SQL Server.
> Sample data mart: `covid`

> Start your local development with `.\env\Scripts\activate`. For more details: [LOCALDEV.md](LOCALDEV.md)

## Common commands:
### Seed data
[Covid](/dbt/data/covid/covid_raw.csv)
```
dbt seed --project-dir ./dbt --target dev
```

### Run all models
```
dbt run --project-dir ./dbt --target dev --full-refresh [--models +exposure:*]
```

### Run all models - DELTA mode
```
dbt run --project-dir ./dbt --target dev [--models +exposure:*]
```

### Test models
```
dbt test --project-dir ./dbt --target dev [--models +exposure:*]
```

## Dockerizing
Build and run dbt as [provisioning](/.docker/provision.md)

Build and run dbt as [processing](/.docker/processing.md)


## Services
### API service - Awesome dbt
An API endpoint using [FastAPI](https://fastapi.tiangolo.com) with [Prefect](https://docs.prefect.io/) as a Dataflow

The dbt will be running as the background task, optional configured in queue.

*Swagger*:

![Alt text](/services/api_service/.insomia/awesome-dbt-api-docs-2021-10-03.png?raw=true "api redoc")

*Redoc*:

![Alt text](/services/api_service/.insomia/awesome-dbt-api-redoc-2021-10-03.png?raw=true "api redoc")


See [README.md](/services/api_service/README.md) for more details.


### Admin portal
> TBU

See [README.md](/services/admin_portal/README.md) for more details.


## WHAT next?
- `Awesome dbt` CI/CD with CircleCI or Github Action
- `Awesome dbt` authentication
- The `dbt` with Postgres DB
- Admin portal
