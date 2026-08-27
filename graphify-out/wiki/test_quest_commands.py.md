# test_quest_commands.py

> 39 nodes

## Key Concepts

- **test_config_init.py** (18 connections) — `server/tests/unit/config/test_config_init.py`
- **._sanitize_environment_for_nested_configs()** (8 connections) — `server/config/models/app.py`
- **test_first_cors_origins_env_returns_first_match()** (6 connections) — `server/tests/unit/config/test_config_init.py`
- **MonkeyPatch** (6 connections)
- **._first_cors_origins_env()** (5 connections) — `server/config/models/app.py`
- **test_first_cors_origins_env_none_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_converts_comma_separated()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_already_json()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_only_commas()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **.__init__()** (4 connections) — `server/config/models/app.py`
- **test_appconfig_init_reraises_settings_error_unrelated_to_allow_origins()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_appconfig_init_retries_after_settings_error_naming_allow_origins()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_fresh_instances_in_test_mode()** (2 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_database_config()** (2 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_game_config()** (2 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_server_config()** (2 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_returns_app_config()** (2 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_in_test_mode()** (2 connections) — `server/tests/unit/config/test_config_init.py`
- **Any** (1 connections)
- **parametrize** (1 connections)
- **Initialize configuration and set environment variables for legacy compatibility.** (1 connections) — `server/config/models/app.py`
- **Return first set CORS origins env var to reduce CCN in _sanitize.** (1 connections) — `server/config/models/app.py`
- **Normalize environment variables so nested configs can parse them reliably.** (1 connections) — `server/config/models/app.py`
- **Unit tests for config module initialization.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- *... and 14 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (13 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/config/models/app.py`
- `server/tests/unit/config/test_config_init.py`

## Audit Trail

- EXTRACTED: 56 (90%)
- INFERRED: 6 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*