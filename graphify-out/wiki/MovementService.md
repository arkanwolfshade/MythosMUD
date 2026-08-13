# MovementService

> 32 nodes

## Key Concepts

- **MovementService** (45 connections) — `server/game/movement_service.py`
- **UUID** (18 connections)
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **.move_player()** (7 connections) — `server/game/movement_service.py`
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (5 connections) — `server/game/movement_service.py`
- **.get_player_room()** (4 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_added_player_room()** (4 connections) — `server/game/movement_service.py`
- **.get_room_players()** (3 connections) — `server/game/movement_service.py`
- **.validate_player_location()** (3 connections) — `server/game/movement_service.py`
- **.set_player_combat_service()** (2 connections) — `server/game/movement_service.py`
- **Exception** (1 connections)
- **Validate movement parameters. Returns False if validation fails (same room),…** (1 connections) — `server/game/movement_service.py`
- **Mark destination room as explored (non-blocking).** (1 connections) — `server/game/movement_service.py`
- **Handle movement errors with monitoring.** (1 connections) — `server/game/movement_service.py`
- **Log movement timing breakdown after a successful move.** (1 connections) — `server/game/movement_service.py`
- **Move a player from one room to another atomically. This operation ensures ACID…** (1 connections) — `server/game/movement_service.py`
- **Service for handling atomic player movement operations. This class provides…** (1 connections) — `server/game/movement_service.py`
- **Validate player and room IDs for add_player_to_room.** (1 connections) — `server/game/movement_service.py`
- **Update player current_room_id in persistence after room add.** (1 connections) — `server/game/movement_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [._execute_move_locked](_execute_move_locked.md) (11 shared connections)
- [log_and_raise](log_and_raise.md) (9 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [._validate_movement](_validate_movement.md) (5 shared connections)
- [._get_rooms_for_movement](_get_rooms_for_movement.md) (4 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 93 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*