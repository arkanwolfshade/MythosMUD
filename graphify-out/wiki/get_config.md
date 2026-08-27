# get_config

> 69 nodes

## Key Concepts

- **get_config()** (103 connections) — `server/config/__init__.py`
- **test_config_init.py** (20 connections) — `server/tests/unit/config/test_config_init.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **._sanitize_environment_for_nested_configs()** (8 connections) — `server/config/models/app.py`
- **test_first_cors_origins_env_returns_first_match()** (6 connections) — `server/tests/unit/config/test_config_init.py`
- **MonkeyPatch** (6 connections)
- **._first_cors_origins_env()** (5 connections) — `server/config/models/app.py`
- **test_first_cors_origins_env_none_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_converts_comma_separated()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_already_json()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_only_commas()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **generate_invites.py** (5 connections) — `tools/invite_tools/generate_invites.py`
- **main()** (4 connections) — `scripts/verify_and_load_seed.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **test_appconfig_init_reraises_settings_error_unrelated_to_allow_origins()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_appconfig_init_retries_after_settings_error_naming_allow_origins()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_fresh_instances_in_test_mode()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- *... and 44 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (24 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [combat_service.py](combat_service.py.md) (4 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (3 shared connections)
- [models/combat.py](models-combat.py.md) (3 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (3 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (3 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (3 shared connections)
- [factory.py](factory.py.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)

## Source Files

- `scripts/verify_and_load_seed.py`
- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 195 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*