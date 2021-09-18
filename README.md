# dbt-mssql
This is where to start the data transformation with dbt and SQL Server

- Seed data
[Covid Data on 2021/09/19](/dbt/data/covid/CovidDataLatest.csv)
```
dbt seed --project-dir ./dbt --target dev
```

- Run all models
```
dbt run --project-dir ./dbt --target dev
dbt run --project-dir ./dbt --target dev --full-refresh
```