# get_config

> 45 nodes

## Key Concepts

- **get_config()** (110 connections) — `server/config/__init__.py`
- **server/config/__init__.py** (29 connections) — `server/config/__init__.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **generate_invites.py** (4 connections) — `tools/invite_tools/generate_invites.py`
- **.get_default_starting_room()** (3 connections) — `server/game/player_service.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_test_mode_returns_fresh_instances()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/test_config_smoke.py`
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites.py`
- **main()** (3 connections) — `tools/invite_tools/generate_invites.py`
- **test_config_smoke.py** (3 connections) — `server/tests/unit/test_config_smoke.py`
- **Configuration module for MythosMUD server. This module provides type-safe,…** (1 connections) — `server/config/__init__.py`
- **Return the runtime app instance attached during lifespan startup. This provides…** (1 connections) — `server/config/__init__.py`
- *... and 20 more nodes in this community*

## Relationships

- [AppConfig](AppConfig.md) (13 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [.state](state.md) (6 shared connections)
- [factory.py](factory.py.md) (5 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (4 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (3 shared connections)
- [DatabaseManager](DatabaseManager.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (3 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/game/player_service.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 186 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*