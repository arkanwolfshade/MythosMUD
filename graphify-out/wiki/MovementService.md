# MovementService

> 64 nodes

## Key Concepts

- **MovementService** (51 connections) — `server/game/movement_service.py`
- **UUID** (19 connections)
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **.move_player()** (8 connections) — `server/game/movement_service.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._maybe_trigger_room_entry_hallucination()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **.get_player_room()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_added_player_room()** (4 connections) — `server/game/movement_service.py`
- *... and 39 more nodes in this community*

## Relationships

- [test_movement_service.py](test_movement_service.py.md) (14 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [GameBundle](GameBundle.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)
- [follow_movement.py](follow_movement.py.md) (2 shared connections)
- [follow_service.py](follow_service.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (1 shared connections)
- [FollowService](FollowService.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 146 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*