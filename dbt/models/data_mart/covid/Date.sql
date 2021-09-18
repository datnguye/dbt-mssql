{{ config(alias='Date', unique_key='DateKey') }}

{% if is_incremental() %}
    {%- call statement('get_lastest_time', fetch_result=True) -%}
        SELECT MAX(LastUpdatedTimestamp) FROM {{ this }}
    {%- endcall -%}
    {%- set lastest_time = load_result('get_lastest_time')['data'][0][0] -%}
{% endif %}

SELECT  DISTINCT 
        {{ surrogate_key(['UpdatedDate']) }} as DateKey,
        GETUTCDATE() as LastUpdatedTimestamp,

        UpdatedDate as [Date Value],
        DATEPART(DAY, UpdatedDate) as [Day],
        DATEPART(MONTH, UpdatedDate) as [Month],
        DATENAME(MONTH, UpdatedDate) as [Month Name],
        'Q' + CONVERT(varchar, DATEPART(QUARTER, UpdatedDate)) as [Quarter],
        DATEPART(YEAR, UpdatedDate) as [Year]

FROM    {{ref('ODS_Covid_Case')}}

WHERE   1=1
{% if is_incremental() %}
AND     (
            --update once a day
            CONVERT(date, GETUTCDATE()) > CONVERT(date, '{{lastest_time}}')
        )
{% endif %}