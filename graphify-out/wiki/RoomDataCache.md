# RoomDataCache

> 51 nodes · cohesion 0.07

## Key Concepts

- **PlayerPositionService** (50 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **asyncio** (17 connections)
- **test_change_position_database_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_all_positions()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_already_in_position()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_get_stats_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_invalid_position()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_get_stats()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_persistence()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_success()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_updates_connection_manager()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_updates_existing_connection_info()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_creates_missing()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_handles_errors()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_keeps_correct()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_no_storage()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_updates_incorrect()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_player_position_service_init()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_player_position_service_init_none_values()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_handles_errors()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_no_manager()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_no_online_players()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- *... and 26 more nodes in this community*

## Relationships

- [LoggingConfig](LoggingConfig.md) (12 shared connections)
- [PlayerCombatState](PlayerCombatState.md) (3 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (3 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [.initialize](initialize.md) (2 shared connections)
- [_CombatServiceDeps](_CombatServiceDeps.md) (2 shared connections)
- [SchemaValidator](SchemaValidator.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 96 (81%)
- INFERRED: 22 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*