# PlayerPositionService

> 91 nodes

## Key Concepts

- **PlayerPositionService** (50 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **player_position_service.py** (18 connections) — `server/services/player_position_service.py`
- **PositionPlayer** (13 connections) — `server/services/player_position_service.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **asyncio** (12 connections)
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **SupportsPlayerPersistence** (8 connections) — `server/services/player_position_service.py`
- **SupportsConnectionManager** (7 connections) — `server/services/player_position_service.py`
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **test_change_position_database_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **._get_player_for_position_change()** (4 connections) — `server/services/player_position_service.py`
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **._initial_response()** (4 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (4 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (4 connections) — `server/services/player_position_service.py`
- **test_change_position_all_positions()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_already_in_position()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_get_stats_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_invalid_position()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_get_stats()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- *... and 66 more nodes in this community*

## Relationships

- [PlayerEnteredRoom](PlayerEnteredRoom.md) (8 shared connections)
- [command_service.py](command_service.py.md) (7 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [PartyService](PartyService.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 172 (91%)
- INFERRED: 18 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*