# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /

# Install the Microsoft ODBC driver for SQL Server (Debian 10)
RUN apt-get update && apt install -y curl gnupg2
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN . ~/.bashrc 

# Install ODBC
RUN apt-get update && apt install -y gcc g++ unixodbc-dev && apt-get clean

# Copy project
RUN mkdir app
RUN mkdir app/dbt
COPY ./dbt ./app/dbt
RUN mkdir app/api
COPY ./services/api_service ./app/api

# Setup dbt profiles.yml
RUN mkdir ~/.dbt
COPY ./.dbt_profiles.yml ./.dbt_profiles.yml
RUN  cp ./.dbt_profiles.yml ~/.dbt/profiles.yml
RUN export ENV_DBT_SERVER=${{ secrets.ENV_DBT_SERVER }}
RUN export ENV_DBT_PORT=${{ secrets.ENV_DBT_PORT }}
RUN export ENV_DBT_DATABASE=${{ secrets.ENV_DBT_DATABASE }}
RUN export ENV_DBT_SCHEMA=${{ secrets.ENV_DBT_SCHEMA }}
RUN export ENV_DBT_USER=${{ secrets.ENV_DBT_USER }}
RUN export ENV_DBT_PASSWORD=${{ secrets.ENV_DBT_PASSWORD }}

# Install requirements
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# Install dbt packages
RUN dbt deps --project-dir ./app/dbt

# Seed data (OPTIONAL)
# TODO: Secret chick HERE
# RUN dbt seed --project-dir ./app/dbt --target prod

# Entry point
CMD uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir "./app/api"