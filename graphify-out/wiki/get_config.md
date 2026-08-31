# get_config

> 33 nodes

## Key Concepts

- **get_config()** (103 connections) — `server/config/__init__.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **generate_invites.py** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_test_mode_returns_fresh_instances()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/test_config_smoke.py`
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites.py`
- **main()** (3 connections) — `tools/invite_tools/generate_invites.py`
- **test_config_smoke.py** (3 connections) — `server/tests/unit/test_config_smoke.py`
- **Reset the configuration cache. In test mode, this is a no-op since get_config()…** (1 connections) — `server/config/__init__.py`
- **Detect if running in test environment. Uses multiple detection methods to…** (1 connections) — `server/config/__init__.py`
- **Get application configuration (singleton in production, fresh in tests). In…** (1 connections) — `server/config/__init__.py`
- **Test that reset_config() works in test mode.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- **Unit tests for configuration system.** (1 connections) — `server/tests/unit/config/test_config.py`
- **Test that get_config() returns fresh instances in test mode.** (1 connections) — `server/tests/unit/config/test_config.py`
- **Test that reset_config() clears global state.** (1 connections) — `server/tests/unit/config/test_config.py`
- **Test that config has server configuration.** (1 connections) — `server/tests/unit/config/test_config.py`
- *... and 8 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [test_config_init.py](test_config_init.py.md) (8 shared connections)
- [AppConfig](AppConfig.md) (6 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (5 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (4 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (3 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 141 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*