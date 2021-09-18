{% macro hash(field) -%}
    CONVERT(NVARCHAR(32), HashBytes('MD5', {{field}}), 2)
{%- endmacro %}