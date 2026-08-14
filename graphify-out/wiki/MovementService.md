# MovementService

> 46 nodes

## Key Concepts

- **MovementService** (45 connections) — `server/game/movement_service.py`
- **UUID** (18 connections)
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **.move_player()** (7 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (5 connections) — `server/game/movement_service.py`
- **.get_player_room()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_added_player_room()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._record_move_validation_failure()** (4 connections) — `server/game/movement_service.py`
- **Room** (2 connections)
- **Exception** (1 connections)
- *... and 21 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [movement_helpers.py](movement_helpers.py.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (3 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [movement_service](movement_service.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [.get_room_players](get_room_players.md) (1 shared connections)
- [.validate_player_location](validate_player_location.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 118 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*