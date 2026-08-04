# config models rationale

> 33 nodes

## Key Concepts

- **test_config_models.py** (19 connections) — `server/tests/unit/config/test_config_models.py`
- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
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
- **BaseSettings** (2 connections)
- **.validate_port()** (2 connections) — `server/config/models/server_db.py`
- **test_parse_env_list_empty_and_none()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_default_cors_origins_fallback()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **Parse a string from the environment as JSON list or CSV.** (1 connections) — `server/config/models/_helpers.py`
- **Derive default CORS origins with environment taking precedence.** (1 connections) — `server/config/models/_helpers.py`
- **Server network configuration.** (1 connections) — `server/config/models/server_db.py`
- **Validate port is in valid range.** (1 connections) — `server/config/models/server_db.py`
- **Unit tests for configuration models.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing None as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing empty string as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- *... and 8 more nodes in this community*

## Relationships

- [admin command setstat](admin_command_setstat.md) (8 shared connections)
- [playerHandlers eventHandlers healthEvent](playerHandlers_eventHandlers_healthEvent.md) (6 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (4 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 104 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*