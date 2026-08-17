# server tests unit game test

> 75 nodes

## Key Concepts

- **test_movement_service.py** (52 connections) — `server/tests/unit/game/test_movement_service.py`
- **asyncio** (20 connections)
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
- **test_get_player_room_player_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_get_player_room_success()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_player_not_found()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_same_room()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_success()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_validation_fails()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init_no_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_remove_player_invalid_params()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_resolve_player_by_name()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_movement_allows_ghost_in_destination()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_movement_combat_blocks()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 50 more nodes in this community*

## Relationships

- [server game movement helpers](server_game_movement_helpers.md) (13 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (5 shared connections)
- [server game movement service movementservice](server_game_movement_service_movementservice.md) (4 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 113 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*