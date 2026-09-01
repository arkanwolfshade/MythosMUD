# get_config

> 61 nodes

## Key Concepts

- **get_config()** (102 connections) — `server/config/__init__.py`
- **server/config/__init__.py** (26 connections) — `server/config/__init__.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **services/rate_limiter.py** (10 connections) — `server/services/rate_limiter.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **load_motd()** (8 connections) — `server/utils/motd_loader.py`
- **test_motd_loader.py** (7 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **motd_loader.py** (7 connections) — `server/utils/motd_loader.py`
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **generate_invites.py** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **.get_default_starting_room()** (3 connections) — `server/game/player_service.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_test_mode_returns_fresh_instances()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/test_config_smoke.py`
- **test_load_motd_empty_file()** (3 connections) — `server/tests/unit/utils/test_motd_loader.py`
- *... and 36 more nodes in this community*

## Relationships

- [AppConfig](AppConfig.md) (13 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [CombatParticipant](CombatParticipant.md) (9 shared connections)
- [factory.py](factory.py.md) (5 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (5 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (3 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (3 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/container/bundles/core.py`
- `server/game/player_service.py`
- `server/services/rate_limiter.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `server/tests/unit/utils/test_motd_loader.py`
- `server/utils/motd_loader.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 212 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*