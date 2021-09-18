{{ config(schema='staging', alias='STAG_Covid_Data', unique_key='CovidDataKey') }}

{% if is_incremental() %}
    {%- call statement('get_lastest_time', fetch_result=True) -%}
        SELECT MAX(UpdatedDate) FROM {{ this }}
    {%- endcall -%}
    {%- set lastest_time = load_result('get_lastest_time')['data'][0][0] -%}
{% endif %}

SELECT  DISTINCT 
        {{ surrogate_key(['continent', 'location', 'last_updated_date']) }} as CovidDataKey,

        TRY_CONVERT(varchar(3), iso_code)                     as CountryCode,
        TRY_CONVERT(varchar(255), continent)                  as Continent,
        TRY_CONVERT(varchar(255), location)                   as Country,
        TRY_CONVERT(date, last_updated_date)                  as UpdatedDate,
        COALESCE(TRY_CONVERT(decimal(17,0), total_cases),0)   as TotalCase,
        COALESCE(TRY_CONVERT(decimal(17,0), new_cases),0)     as NewCase,
        COALESCE(TRY_CONVERT(decimal(17,0), total_deaths),0)  as TotalDeath,
        COALESCE(TRY_CONVERT(decimal(17,0), new_deaths),0)    as NewDeath,

        GETUTCDATE() as LastUpdatedTimestamp

FROM    {{ref('covid_raw')}}
WHERE   continent IS NOT NULL

{% if is_incremental() %}
AND   (
            TRY_CONVERT(date, last_updated_date) >= '{{lastest_time}}'
        )
{% endif %}