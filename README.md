# dbt-mssql
This is where to start the data transformation with dbt and SQL Server.
> Sample data mart: `covid`

> Start your local development with `.\env\Scripts\activate`. For more details: [LOCALDEV.md](LOCALDEV.md)

[![SSH deployment](https://github.com/datnguye/dbt-mssql/actions/workflows/ssh-to-server.yml/badge.svg)](https://github.com/datnguye/dbt-mssql/actions/workflows/ssh-to-server.yml)

[![Awesome dbt CI](https://github.com/datnguye/dbt-mssql/actions/workflows/ci-awesome-dbt.yml/badge.svg)](https://github.com/datnguye/dbt-mssql/actions/workflows/ci-awesome-dbt.yml)
[![Awesome dbt Publish](https://github.com/datnguye/dbt-mssql/actions/workflows/cd-awesome-dbt.yml/badge.svg)](https://github.com/datnguye/dbt-mssql/actions/workflows/cd-awesome-dbt.yml)


## Common commands:
### Set enviroment variables before any dbt operations as we're gonna use dbt `env_var` within our `profiles.yml`:
- Windows
```
set ENV_DBT_SERVER=DAT\DAT19
set ENV_DBT_PORT=1433
set ENV_DBT_DATABASE=PLAY
set ENV_DBT_SCHEMA=analytic
set ENV_DBT_USER=datnguye
set ENV_DBT_PASSWORD=datnguye
```

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
- [Provisioning](/.docker/provision.md)

- [Processing](/.docker/processing.md)

- [API Service](/.docker/awesome-dbt.md)


## Services
### API service - Awesome dbt
[![Awesome dbt CI](https://github.com/datnguye/dbt-mssql/actions/workflows/ci-awesome-dbt.yml/badge.svg)](https://github.com/datnguye/dbt-mssql/actions/workflows/ci-awesome-dbt.yml)
[![Awesome dbt Publish](https://github.com/datnguye/dbt-mssql/actions/workflows/cd-awesome-dbt.yml/badge.svg)](https://github.com/datnguye/dbt-mssql/actions/workflows/cd-awesome-dbt.yml)

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
- `Awesome dbt` key vault / authentication / Serialize dbt Result
- The `dbt` with Postgres DB
- Admin portal
