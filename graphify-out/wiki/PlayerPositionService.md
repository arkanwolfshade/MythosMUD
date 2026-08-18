# PlayerPositionService

> 79 nodes

## Key Concepts

- **PlayerPositionService** (48 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (28 connections) — `server/tests/unit/services/test_player_position_service.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **asyncio** (12 connections)
- **Player** (8 connections)
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **test_change_position_database_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **._get_player_for_position_change()** (4 connections) — `server/services/player_position_service.py`
- **._initial_response()** (4 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (4 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (4 connections) — `server/services/player_position_service.py`
- **.save_player()** (4 connections) — `server/services/player_position_service.py`
- **test_change_position_all_positions()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_already_in_position()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_get_stats_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_invalid_position()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_get_stats()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_persistence()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_success()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_updates_connection_manager()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- *... and 54 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (6 shared connections)
- [command_service.py](command_service.py.md) (5 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (3 shared connections)
- [GameBundle](GameBundle.md) (3 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 134 (89%)
- INFERRED: 17 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*