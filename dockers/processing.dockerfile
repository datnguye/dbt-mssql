# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /

RUN pip3 install dbt==0.20.2
COPY . .
RUN dbt deps --project-dir ./dbt

# Recommend to use environment variables in: profiles.yml/outputs.prod
# [dbt env_var](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var)
RUN cp ".dbt_profiles.yml" "~/.dbt/profiles.yml"

# entry point
ENV OP="run"
ENV MODELS="+exposure:*"
ENV FULL="--full-refresh"
CMD dbt ${OP} \
    --project-dir ./dbt \
    --target prod \
    --models ${MODELS} \
    ${FULL}