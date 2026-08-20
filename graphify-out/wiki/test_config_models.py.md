# test_config_models.py

> 37 nodes

## Key Concepts

- **test_config_models.py** (25 connections) — `server/tests/unit/config/test_config_models.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **.validate_database_url()** (3 connections) — `server/config/models/server_db.py`
- **.validate_pool_config()** (3 connections) — `server/config/models/server_db.py`
- **.validate_port()** (3 connections) — `server/config/models/server_db.py`
- **test_database_config_validate_pool_config_invalid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_empty()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_postgresql()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_no_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_with_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_default_host()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_high()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_low()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_valid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **field_validator** (3 connections)
- **test_default_cors_origins_fallback()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **BaseSettings** (2 connections)
- **Derive default CORS origins with environment taking precedence.** (1 connections) — `server/config/models/_helpers.py`
- **Server network configuration.** (1 connections) — `server/config/models/server_db.py`
- **Validate port is in valid range.** (1 connections) — `server/config/models/server_db.py`
- **Database configuration.** (1 connections) — `server/config/models/server_db.py`
- **Validate database URL format - PostgreSQL only.** (1 connections) — `server/config/models/server_db.py`
- *... and 12 more nodes in this community*

## Relationships

- [config/models/__init__.py](config-models-__init__.py.md) (7 shared connections)
- [_parse_env_list](_parse_env_list.md) (6 shared connections)
- [GameConfig](GameConfig.md) (5 shared connections)
- [test_config_model_helpers.py](test_config_model_helpers.py.md) (3 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 72 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*