# MovementService

> 42 nodes

## Key Concepts

- **MovementService** (47 connections) — `server/game/movement_service.py`
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **UUID** (13 connections)
- **.move_player()** (8 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (6 connections) — `server/game/movement_service.py`
- **.__init__()** (6 connections) — `server/game/movement_service.py`
- **._maybe_trigger_room_entry_hallucination()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._record_move_validation_failure()** (4 connections) — `server/game/movement_service.py`
- **test_movement_service_init_no_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_room_transfer_tells_the_source_room_where_the_player_went()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **.set_player_combat_service()** (2 connections) — `server/game/movement_service.py`
- **Room** (2 connections)
- **Exception** (1 connections)
- **Validate movement parameters. Returns False if validation fails (same room),…** (1 connections) — `server/game/movement_service.py`
- **Resolve player by ID or name and return player object and resolved ID.** (1 connections) — `server/game/movement_service.py`
- *... and 17 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (5 shared connections)
- [FollowService](FollowService.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [SpellEffects](SpellEffects.md) (3 shared connections)
- [asyncio](asyncio.md) (3 shared connections)
- [go_command.py](go_command.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [movement_service](movement_service.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 107 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*