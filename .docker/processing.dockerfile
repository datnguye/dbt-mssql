# syntax=docker/dockerfile:1
# !!IMPORTANT: 
# This is to wrap the dbt commands into docker command. NOT a service yet!
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

# Install dbt
RUN pip3 install dbt==0.20.2
# Install dbt-sqlserver
RUN apt-get update && apt install -y gcc g++ unixodbc-dev && apt-get clean
RUN pip3 install dbt-sqlserver
# Copy dbt project
COPY . .

# Create dbt profiles file
# Recommend to use environment variables in: profiles.yml/outputs.prod
# [dbt env_var](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var)
RUN mkdir ./profile
RUN cp ".dbt_profiles.yml" "./profile/profiles.yml"

# Install dbt packages
RUN dbt deps --profiles-dir "./profile" --project-dir ./dbt
# Seed data (OPTIONAL)
RUN dbt seed --profiles-dir "./profile" --project-dir ./dbt --target prod

# Entry point
ENV OP="run"
ENV MODELS="+exposure:*"
CMD dbt run \
    --profiles-dir "./profile" \
    --project-dir ./dbt \
    --target prod \
    --models ${MODELS} \