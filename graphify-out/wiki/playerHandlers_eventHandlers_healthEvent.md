# playerHandlers eventHandlers healthEvent

> 17 nodes

## Key Concepts

- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **.ensure_url_set()** (4 connections) — `server/config/models/server_db.py`
- **test_database_config_validate_url_postgresql()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_empty()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_invalid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **.validate_database_url()** (2 connections) — `server/config/models/server_db.py`
- **.validate_pool_config()** (2 connections) — `server/config/models/server_db.py`
- **Any** (1 connections)
- **Database configuration.** (1 connections) — `server/config/models/server_db.py`
- **Validate database URL format - PostgreSQL only.** (1 connections) — `server/config/models/server_db.py`
- **Validate pool configuration values are positive.** (1 connections) — `server/config/models/server_db.py`
- **Ensure url is set - use npc_url as fallback if url is missing.          This han** (1 connections) — `server/config/models/server_db.py`
- **Test DatabaseConfig URL validation with PostgreSQL URL.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test DatabaseConfig URL validation with empty URL.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test DatabaseConfig pool config validation with positive values.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test DatabaseConfig pool config validation with invalid value.** (1 connections) — `server/tests/unit/config/test_config_models.py`

## Relationships

- [config models rationale](config_models_rationale.md) (6 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (2 shared connections)
- [admin command setstat](admin_command_setstat.md) (2 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)

## Source Files

- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 42 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*