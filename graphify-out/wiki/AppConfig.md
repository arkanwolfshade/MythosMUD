# AppConfig

> 43 nodes

## Key Concepts

- **AppConfig** (35 connections) — `server/config/models/app.py`
- **test_config_init.py** (20 connections) — `server/tests/unit/config/test_config_init.py`
- **._sanitize_environment_for_nested_configs()** (8 connections) — `server/config/models/app.py`
- **test_first_cors_origins_env_returns_first_match()** (6 connections) — `server/tests/unit/config/test_config_init.py`
- **MonkeyPatch** (6 connections)
- **._first_cors_origins_env()** (5 connections) — `server/config/models/app.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **test_first_cors_origins_env_none_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_converts_comma_separated()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_already_json()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_only_commas()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **.set_legacy_environment_variables()** (3 connections) — `server/config/models/app.py`
- **test_appconfig_init_reraises_settings_error_unrelated_to_allow_origins()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_appconfig_init_retries_after_settings_error_naming_allow_origins()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_fresh_instances_in_test_mode()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **Any** (1 connections)
- **BaseSettings** (1 connections)
- **model_validator** (1 connections)
- **parametrize** (1 connections)
- **Composite application configuration. This is the main configuration class that…** (1 connections) — `server/config/models/app.py`
- *... and 18 more nodes in this community*

## Relationships

- [get_config](get_config.md) (13 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (6 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [LoggingConfig](LoggingConfig.md) (2 shared connections)
- [test_config_models.py](test_config_models.py.md) (1 shared connections)
- [DatabaseConfig](DatabaseConfig.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [GameConfig](GameConfig.md) (1 shared connections)
- [CORSConfig](CORSConfig.md) (1 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/config/models/app.py`
- `server/tests/unit/config/test_config_init.py`

## Audit Trail

- EXTRACTED: 77 (82%)
- INFERRED: 17 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*