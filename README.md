# dbt-mssql
This is where to start the data transformation with dbt and SQL Server.
> Sample data mart: `covid`

> Start your local development with [local dev](.local_dev.md)

## Common commands:
### Seed data
[Covid](/dbt/data/covid/covid_raw.csv)
```
dbt seed --project-dir ./dbt --target dev
```

### Run all models
```
dbt run --project-dir ./dbt --target dev --full-refresh
```

### Run all models - DELTA mode
```
dbt run --project-dir ./dbt --target dev
```

### Test models
```
dbt test --project-dir ./dbt --target dev
```