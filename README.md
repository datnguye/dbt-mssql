# dbt-mssql
This is where to start the data transformation with dbt and SQL Server.
> Sample data mart: `covid`

> Start your local development with `.\env\Scripts\activate`. For more details: [local dev](.local_dev.md)

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
Build and run dbt as [provisioning](/dockers/provision.md)

Build and run dbt as [processing](/dockers/processing.md)



## WHAT next?
- CI/CD with CircleCI
- Build a `dbt wrapper` service
- Clone this to do with Postgres DB