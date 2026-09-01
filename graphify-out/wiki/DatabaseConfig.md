# DatabaseConfig

> 21 nodes

## Key Concepts

- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **.ensure_url_set()** (5 connections) — `server/config/models/server_db.py`
- **.validate_database_url()** (3 connections) — `server/config/models/server_db.py`
- **.validate_pool_config()** (3 connections) — `server/config/models/server_db.py`
- **.validate_port()** (3 connections) — `server/config/models/server_db.py`
- **test_database_config_validate_pool_config_invalid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_empty()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_postgresql()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **field_validator** (3 connections)
- **Any** (1 connections)
- **model_validator** (1 connections)
- **Validate port is in valid range.** (1 connections) — `server/config/models/server_db.py`
- **Database configuration.** (1 connections) — `server/config/models/server_db.py`
- **Validate database URL format - PostgreSQL only.** (1 connections) — `server/config/models/server_db.py`
- **Validate pool configuration values are positive.** (1 connections) — `server/config/models/server_db.py`
- **Ensure url is set - use npc_url as fallback if url is missing. This handles…** (1 connections) — `server/config/models/server_db.py`
- **Test DatabaseConfig URL validation with PostgreSQL URL.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test DatabaseConfig URL validation with empty URL.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test DatabaseConfig pool config validation with positive values.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test DatabaseConfig pool config validation with invalid value.** (1 connections) — `server/tests/unit/config/test_config_models.py`

## Relationships

- [test_config_models.py](test_config_models.py.md) (7 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (2 shared connections)
- [_helpers.py](_helpers.py.md) (2 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)

## Source Files

- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 32 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*