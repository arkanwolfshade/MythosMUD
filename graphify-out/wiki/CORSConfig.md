# CORSConfig

> 42 nodes

## Key Concepts

- **CORSConfig** (30 connections) — `server/config/models/cors.py`
- **test_cors_config.py** (14 connections) — `server/tests/unit/config/test_cors_config.py`
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
- **._validate_and_warn_wildcards()** (3 connections) — `server/config/models/cors.py`
- **.validate_max_age()** (3 connections) — `server/config/models/cors.py`
- **test_cors_defaults_include_local_dev_origins()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- **test_cors_parse_allow_methods_uppercases()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- **test_cors_parse_allow_origins_from_comma_separated_string()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- **test_cors_parse_allow_origins_from_json_array()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- **test_cors_parse_expose_headers_allows_empty()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- **test_cors_parse_max_age_from_string()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- **test_cors_parse_max_age_invalid_string_uses_default()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- **test_cors_rejects_empty_allow_origins()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- **test_cors_rejects_negative_max_age()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- **test_cors_wildcard_origin_accepted()** (2 connections) — `server/tests/unit/config/test_cors_config.py`
- *... and 17 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [factory.py](factory.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/config/models/cors.py`
- `server/tests/unit/config/test_cors_config.py`

## Audit Trail

- EXTRACTED: 73 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*