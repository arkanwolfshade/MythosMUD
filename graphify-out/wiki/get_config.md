# get_config

> 61 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **load_motd()** (8 connections) — `server/utils/motd_loader.py`
- **test_motd_loader.py** (7 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **generate_invites.py** (5 connections) — `tools/invite_tools/generate_invites.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **.get_default_starting_room()** (3 connections) — `server/game/player_service.py`
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
- **test_get_default_damage_fallback_on_error()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_get_default_damage_from_config()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/test_config_smoke.py`
- **test_load_motd_empty_file()** (3 connections) — `server/tests/unit/utils/test_motd_loader.py`
- *... and 36 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [server/tests/conftest.py](server-tests-conftest.py.md) (5 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [AppConfig](AppConfig.md) (3 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (3 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (3 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (3 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/game/player_service.py`
- `server/models/combat.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/test_config_smoke.py`
- `server/tests/unit/utils/test_motd_loader.py`
- `server/utils/motd_loader.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 175 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*