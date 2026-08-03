# config models rationale

> 29 nodes

## Key Concepts

- **test_config_models.py** (19 connections) — `server/tests/unit/config/test_config_models.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
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
- **Server network configuration.** (1 connections) — `server/config/models/server_db.py`
- **Validate port is in valid range.** (1 connections) — `server/config/models/server_db.py`
- **Database configuration.** (1 connections) — `server/config/models/server_db.py`
- **Validate database URL format - PostgreSQL only.** (1 connections) — `server/config/models/server_db.py`
- **Validate pool configuration values are positive.** (1 connections) — `server/config/models/server_db.py`
- **Unit tests for configuration models.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test ServerConfig default host.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test ServerConfig port validation with valid port.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test ServerConfig port validation with port too low.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test ServerConfig port validation with port too high.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- *... and 4 more nodes in this community*

## Relationships

- [admin command setstat](admin_command_setstat.md) (9 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (6 shared connections)
- [player event handlers](player_event_handlers.md) (2 shared connections)

## Source Files

- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 89 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*