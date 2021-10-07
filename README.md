# dbt-mssql
This is where to start the data transformation with dbt and SQL Server.
> Sample data mart: `covid`

> Start your local development with `.\env\Scripts\activate`. For more details: [LOCALDEV.md](LOCALDEV.md)

BUILD statuses:

[![Awesome dbt CI](https://github.com/datnguye/dbt-mssql/actions/workflows/di-awesome-dbt.yml/badge.svg?branch=main)](https://github.com/datnguye/dbt-mssql/actions/workflows/di-awesome-dbt.yml)


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
- [Provisioning](/.docker/provision.md)

- [Processing](/.docker/processing.md)

- [API Service](/.docker/awesome-dbt.md)


## Services
### API service - Awesome dbt
[![Awesome dbt CI](https://github.com/datnguye/dbt-mssql/actions/workflows/di-awesome-dbt.yml/badge.svg?branch=main)](https://github.com/datnguye/dbt-mssql/actions/workflows/di-awesome-dbt.yml)

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
- `Awesome dbt` log storage with mssql & dbt env variables
- `Awesome dbt` authentication
- `Awesome dbt` CD with Github Action
- The `dbt` with Postgres DB
- Admin portal
