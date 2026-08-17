# test_movement_service.py

> 92 nodes

## Key Concepts

- **test_movement_service.py** (52 connections) — `server/tests/unit/game/test_movement_service.py`
- **asyncio** (20 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **test_move_player_empty_player_id()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_from_room()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_to_room()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_room_membership_auto_add()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_room_membership_db_mismatch()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_player_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_room_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_success()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_allows_without_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_blocks_when_in_combat()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_player_posture_blocks_sitting()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_get_player_room_player_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_get_player_room_success()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_player_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_same_room()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 67 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [MovementService](MovementService.md) (8 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [movement_service](movement_service.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 162 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*