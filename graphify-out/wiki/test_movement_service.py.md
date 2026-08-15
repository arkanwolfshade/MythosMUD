# test_movement_service.py

> 103 nodes

## Key Concepts

- **test_movement_service.py** (51 connections) — `server/tests/unit/game/test_movement_service.py`
- **movement_service.py** (35 connections) — `server/game/movement_service.py`
- **asyncio** (20 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **movement_service()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_empty_player_id()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_from_room()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_to_room()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_room_membership_auto_add()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_room_membership_db_mismatch()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_player_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_room_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_success()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_allows_without_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 78 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [MovementService](MovementService.md) (11 shared connections)
- [Player](Player.md) (6 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (1 shared connections)
- [test_go_command.py](test_go_command.py.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 202 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*