# MovementService

> 30 nodes

## Key Concepts

- **MovementService** (45 connections) — `server/game/movement_service.py`
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._record_move_validation_failure()** (4 connections) — `server/game/movement_service.py`
- **.get_room_players()** (3 connections) — `server/game/movement_service.py`
- **.validate_player_location()** (3 connections) — `server/game/movement_service.py`
- **.set_player_combat_service()** (2 connections) — `server/game/movement_service.py`
- **Room** (2 connections)
- **Resolve player by ID or name and return player object and resolved ID.** (1 connections) — `server/game/movement_service.py`
- **Get and validate rooms for movement.** (1 connections) — `server/game/movement_service.py`
- **Execute the atomic room transfer.** (1 connections) — `server/game/movement_service.py`
- **Update player location in database.** (1 connections) — `server/game/movement_service.py`
- **If player exited tutorial instance (moved to fixed exit room), clear and…** (1 connections) — `server/game/movement_service.py`
- **Mark destination room as explored (non-blocking).** (1 connections) — `server/game/movement_service.py`
- **Record timing and monitor stats when movement validation fails.** (1 connections) — `server/game/movement_service.py`
- **Run movement logic while holding the service lock.** (1 connections) — `server/game/movement_service.py`
- **Log movement timing breakdown after a successful move.** (1 connections) — `server/game/movement_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [UUID](UUID.md) (17 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [movement_helpers.py](movement_helpers.py.md) (4 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [magic_service.py](magic_service.py.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [movement_service](movement_service.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 128 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*