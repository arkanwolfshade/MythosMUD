# test_movement_service.py

> 32 nodes

## Key Concepts

- **test_movement_service.py** (50 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_allows_without_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_combat_state_blocks_when_in_combat()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init_no_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_get_room_players()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_get_room_players_room_not_found()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_mark_room_explored_with_service()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_remove_player_from_room_room_not_found()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_remove_player_from_room_success()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_remove_player_invalid_params()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_set_player_combat_service()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_move_params_same_room()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_location_false()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_location_room_not_found()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_location_true()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **Unit tests for movement service. Tests the MovementService class.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test remove_player_from_room() successfully removes player.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test remove_player_from_room() when room is not found.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test get_room_players() returns list of player IDs.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test get_room_players() when room is not found.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test validate_player_location() returns True when player is in room.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test validate_player_location() returns False when player is not in room.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test validate_player_location() returns False when room is not found.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test set_player_combat_service updates combat service reference.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (19 shared connections)
- [movement_helpers.py](movement_helpers.py.md) (11 shared connections)
- [MovementService](MovementService.md) (3 shared connections)
- [movement_service](movement_service.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*