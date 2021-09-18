{{ config(schema='ods', alias='ODS_Country', unique_key='CountryKey') }}

{% if is_incremental() %}
    {%- call statement('get_lastest_time', fetch_result=True) -%}
        SELECT MAX(LastUpdatedTimestamp) FROM {{ this }}
    {%- endcall -%}
    {%- set lastest_time = load_result('get_lastest_time')['data'][0][0] -%}
{% endif %}

SELECT  {{ surrogate_key(['Continent', 'Country']) }} as CountryKey,
        CountryCode,
        Continent,
        Country,

        GETUTCDATE() as LastUpdatedTimestamp

FROM    {{ref('STAG_Covid_Data')}}

WHERE   1=1
{% if is_incremental() %}
AND     (
            --update once a day
            CONVERT(date, GETUTCDATE()) > CONVERT(date, '{{lastest_time}}')
        )
{% endif %}