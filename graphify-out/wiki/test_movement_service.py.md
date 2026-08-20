# test_movement_service.py

> 101 nodes

## Key Concepts

- **test_movement_service.py** (52 connections) — `server/tests/unit/game/test_movement_service.py`
- **movement_service.py** (35 connections) — `server/game/movement_service.py`
- **asyncio** (20 connections)
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
- **test_validate_player_room_membership_auto_add()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_room_membership_db_mismatch()** (4 connections) — `server/tests/unit/game/test_movement_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_player_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_room_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_success()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_allows_without_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_blocks_when_in_combat()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_player_posture_blocks_sitting()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 76 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [MovementService](MovementService.md) (11 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (2 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 196 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*