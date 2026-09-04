# Test Player Position Service

> 91 nodes

## Key Concepts

- **PlayerPositionService** (50 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (28 connections) — `server/tests/unit/services/test_player_position_service.py`
- **player_position_service.py** (15 connections) — `server/services/player_position_service.py`
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

- [Test Position Commands](Test_Position_Commands.md) (7 shared connections)
- [Test Rest Command](Test_Rest_Command.md) (4 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (4 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (3 shared connections)
- [Follow Movement](Follow_Movement.md) (3 shared connections)
- [Follow Service](Follow_Service.md) (3 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (2 shared connections)
- [Test Follow Service](Test_Follow_Service.md) (2 shared connections)
- [Combat Turn Participant Actions](Combat_Turn_Participant_Actions.md) (1 shared connections)
- [Test Exploration Service](Test_Exploration_Service.md) (1 shared connections)
- [Instance Manager](Instance_Manager.md) (1 shared connections)
- [Movement Service](Movement_Service.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 170 (90%)
- INFERRED: 19 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*