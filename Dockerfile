# syntax=docker/dockerfile:1
# COPY from /.docker/awesome-dbt.dockerfile
FROM python:3.8-slim-buster
RUN mkdir myapp
WORKDIR /myapp/

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
RUN mkdir dbt
COPY ./dbt ./dbt
COPY ./services/api_service .

# Create dbt profiles.yml
# Recommend to use environment variables in: profiles.yml/outputs.prod
# [dbt env_var](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var)
RUN mkdir ~/.dbt
COPY .dbt_profiles.yml .dbt_profiles.yml
RUN  cp ./.dbt_profiles.yml ~/.dbt/profiles.yml

# Install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Install dbt packages
RUN dbt deps --project-dir ./dbt

# Arguments
ENV SERVER="dummy"
# TODO: Use Key Vault here
ENV USER="dummy"
ENV PASSWORD="dummy"

# Entry point
CMD export env_sqlserver_host_secret=${SERVER} && \
    export env_sqlserver_user_secret=${USER} && \
    export env_sqlserver_password_secret=${PASSWORD} && \
    uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir "/myapp"