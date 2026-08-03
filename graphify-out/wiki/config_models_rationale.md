# config models rationale

> 35 nodes

## Key Concepts

- **test_config_models.py** (19 connections) — `server/tests/unit/config/test_config_models.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
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
- **Server network configuration.** (1 connections) — `server/config/models/server_db.py`
- **Validate port is in valid range.** (1 connections) — `server/config/models/server_db.py`
- **Unit tests for configuration models.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing None as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing empty string as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing JSON list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing CSV list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- *... and 10 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (17 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)

## Source Files

- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 93 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*