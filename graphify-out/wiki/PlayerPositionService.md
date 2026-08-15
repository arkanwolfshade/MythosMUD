# PlayerPositionService

> 51 nodes

## Key Concepts

- **PlayerPositionService** (48 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **asyncio** (12 connections)
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
- **test_ensure_default_aliases_creates_missing()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_handles_errors()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_keeps_correct()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_no_storage()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_updates_incorrect()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_player_position_service_init()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_player_position_service_init_none_values()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_handles_errors()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_no_manager()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_update_connection_manager_no_online_players()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- *... and 26 more nodes in this community*

## Relationships

- [.change_position](change_position.md) (10 shared connections)
- [position_commands.py](position_commands.py.md) (3 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [FollowService](FollowService.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 84 (76%)
- INFERRED: 27 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*