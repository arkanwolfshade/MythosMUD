# Community 342

> 49 nodes

## Key Concepts

- **MovementService** (47 connections) — `server/game/movement_service.py`
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **UUID** (13 connections)
- **.move_player()** (7 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (6 connections) — `server/game/movement_service.py`
- **.__init__()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._validate_movement()** (5 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (5 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._maybe_trigger_room_entry_hallucination()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._record_move_validation_failure()** (4 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (4 connections) — `server/game/movement_service.py`
- **test_movement_service_init()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init_no_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_room_transfer_tells_the_source_room_where_the_player_went()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **.set_player_combat_service()** (2 connections) — `server/game/movement_service.py`
- **Room** (2 connections)
- *... and 24 more nodes in this community*

## Relationships

- [Community 112](Community_112.md) (9 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (9 shared connections)
- [Community 159](Community_159.md) (2 shared connections)
- [Community 88](Community_88.md) (2 shared connections)
- [Community 395](Community_395.md) (2 shared connections)
- [Community 99](Community_99.md) (2 shared connections)
- [Community 55](Community_55.md) (2 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (2 shared connections)
- [Community 248](Community_248.md) (1 shared connections)
- [Community 1397](Community_1397.md) (1 shared connections)
- [Community 839](Community_839.md) (1 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 107 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*