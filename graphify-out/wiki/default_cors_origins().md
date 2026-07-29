# default cors origins()

> 49 nodes

## Key Concepts

- **test_config_models.py** (19 connections) — `server/tests/unit/config/test_config_models.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **_parse_env_list()** (11 connections) — `server/config/models/_helpers.py`
- **_default_cors_origins()** (7 connections) — `server/config/models/_helpers.py`
- **.ensure_url_set()** (4 connections) — `server/config/models/server_db.py`
- **_parse_list_from_string()** (3 connections) — `server/config/models/_helpers.py`
- **test_parse_env_list_none()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_empty_string()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_json()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_csv()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_no_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_with_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_default_host()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_valid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_low()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_high()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_postgresql()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_empty()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_invalid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **BaseSettings** (2 connections)
- **.validate_port()** (2 connections) — `server/config/models/server_db.py`
- **.validate_database_url()** (2 connections) — `server/config/models/server_db.py`
- **.validate_pool_config()** (2 connections) — `server/config/models/server_db.py`
- *... and 24 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (13 shared connections)
- [init](init.md) (2 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 143 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*