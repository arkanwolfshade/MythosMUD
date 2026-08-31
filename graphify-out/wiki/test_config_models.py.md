# test_config_models.py

> 40 nodes

## Key Concepts

- **test_config_models.py** (25 connections) — `server/tests/unit/config/test_config_models.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **.ensure_url_set()** (5 connections) — `server/config/models/server_db.py`
- **.validate_database_url()** (3 connections) — `server/config/models/server_db.py`
- **.validate_pool_config()** (3 connections) — `server/config/models/server_db.py`
- **.validate_port()** (3 connections) — `server/config/models/server_db.py`
- **test_database_config_validate_pool_config_invalid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_empty()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_postgresql()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_tick_rate_accepts_positive_override()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_tick_rate_rejects_negative()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_tick_rate_rejects_zero()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_default_host()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_high()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_low()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_valid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **field_validator** (3 connections)
- **BaseSettings** (2 connections)
- **Any** (1 connections)
- **model_validator** (1 connections)
- **Server network configuration.** (1 connections) — `server/config/models/server_db.py`
- **Validate port is in valid range.** (1 connections) — `server/config/models/server_db.py`
- **Database configuration.** (1 connections) — `server/config/models/server_db.py`
- *... and 15 more nodes in this community*

## Relationships

- [_parse_env_list](_parse_env_list.md) (9 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (6 shared connections)
- [GameConfig](GameConfig.md) (5 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 71 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*