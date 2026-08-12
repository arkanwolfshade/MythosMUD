# MovementService

> 52 nodes

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
- **.get_room_players()** (3 connections) — `server/game/movement_service.py`
- **.validate_player_location()** (3 connections) — `server/game/movement_service.py`
- *... and 27 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (9 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (7 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (4 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (3 shared connections)
- [go_command.py](go_command.py.md) (2 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [Spell](Spell.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [spell_effects.py](spell_effects.py.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 210 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*