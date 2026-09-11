# test_movement_service.py

> 107 nodes

## Key Concepts

- **test_movement_service.py** (54 connections) — `server/tests/unit/game/test_movement_service.py`
- **movement_service.py** (38 connections) — `server/game/movement_service.py`
- **asyncio** (23 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **movement_service()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_empty_player_id()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_from_room()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_to_room()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_skips_hallucination_check_for_non_uneasy_tier()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_survives_hallucination_check_error()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_triggers_uneasy_room_entry_hallucination()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_room_membership_auto_add()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_room_membership_db_mismatch()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_player_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_room_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_success()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 82 more nodes in this community*

## Relationships

- [MovementService](MovementService.md) (14 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (5 shared connections)
- [Room](Room.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [RoomService](RoomService.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 208 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*