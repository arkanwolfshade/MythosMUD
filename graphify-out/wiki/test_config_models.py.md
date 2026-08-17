# test_config_models.py

> 42 nodes

## Key Concepts

- **test_config_models.py** (20 connections) — `server/tests/unit/config/test_config_models.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **_parse_list_from_string()** (4 connections) — `server/config/models/_helpers.py`
- **test_database_config_validate_pool_config_invalid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_empty()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_postgresql()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_no_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_with_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_csv()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_empty_string()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_json()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_none()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_default_host()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_high()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_low()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_valid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_fallback()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_env_list_empty_and_none()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_list_from_string_json_and_csv()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **BaseSettings** (2 connections)
- **Parse non-empty string as JSON list or CSV. Used by _parse_env_list.** (1 connections) — `server/config/models/_helpers.py`
- **Parse a string from the environment as JSON list or CSV.** (1 connections) — `server/config/models/_helpers.py`
- *... and 17 more nodes in this community*

## Relationships

- [config/models/__init__.py](config-models-__init__.py.md) (14 shared connections)
- [test_config_model_helpers.py](test_config_model_helpers.py.md) (5 shared connections)
- [.validate_database_url](validate_database_url.md) (1 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 73 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*