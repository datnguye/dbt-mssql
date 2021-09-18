{% macro concat(fields, op='+') -%}
    {{ fields|join(' ' ~ op ~ ' ') }}
{%- endmacro %}