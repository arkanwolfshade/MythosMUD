# CORSConfig

> 27 nodes

## Key Concepts

- **CORSConfig** (19 connections) — `server/config/models/cors.py`
- **._parse_csv()** (10 connections) — `server/config/models/cors.py`
- **field_validator** (6 connections)
- **._clean_list_items()** (5 connections) — `server/config/models/cors.py`
- **._parse_json_array()** (5 connections) — `server/config/models/cors.py`
- **._validate_non_empty()** (5 connections) — `server/config/models/cors.py`
- **.parse_allow_headers()** (4 connections) — `server/config/models/cors.py`
- **.parse_allow_methods()** (4 connections) — `server/config/models/cors.py`
- **.parse_allow_origins()** (4 connections) — `server/config/models/cors.py`
- **._parse_comma_separated()** (4 connections) — `server/config/models/cors.py`
- **.parse_expose_headers()** (4 connections) — `server/config/models/cors.py`
- **.parse_max_age()** (3 connections) — `server/config/models/cors.py`
- **.validate_max_age()** (3 connections) — `server/config/models/cors.py`
- **Any** (1 connections)
- **BaseSettings** (1 connections)
- **Parse comma-separated string into cleaned list.** (1 connections) — `server/config/models/cors.py`
- **Parse comma separated strings or lists into a cleaned list of strings.** (1 connections) — `server/config/models/cors.py`
- **Parse allowed origins from various input formats.** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS allowed methods. Converts all methods to uppercase.** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS allowed headers.** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS max age value. Returns default 600 if invalid.** (1 connections) — `server/config/models/cors.py`
- **Cross-origin resource sharing configuration. Configuration precedence (highest…** (1 connections) — `server/config/models/cors.py`
- **Parse and validate CORS exposed headers. Allows empty list.** (1 connections) — `server/config/models/cors.py`
- **Validate that max_age is non-negative.** (1 connections) — `server/config/models/cors.py`
- **Validate that cleaned list is not empty if allow_empty is False.** (1 connections) — `server/config/models/cors.py`
- *... and 2 more nodes in this community*

## Relationships

- [config/models/__init__.py](config-models-__init__.py.md) (2 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [._validate_and_warn_wildcards](_validate_and_warn_wildcards.md) (1 shared connections)

## Source Files

- `server/config/models/cors.py`

## Audit Trail

- EXTRACTED: 89 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*