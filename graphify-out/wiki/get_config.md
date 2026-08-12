# get_config

> 45 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **generate_invites.py** (4 connections) — `tools/invite_tools/generate_invites.py`
- **test_get_config_fresh_instances_in_test_mode()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
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
- *... and 20 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (5 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (3 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (3 shared connections)
- [database.py](database.py.md) (2 shared connections)
- [server/main.py](server-main.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)
- [combat_attack.py](combat_attack.py.md) (2 shared connections)
- [_create_config_instance](_create_config_instance.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 217 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*