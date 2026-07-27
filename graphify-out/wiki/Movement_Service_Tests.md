# Movement Service Tests

> 47 nodes · cohesion 0.04

## Key Concepts

- **test_movement_service.py** (24 connections) — `server/tests/unit/game/test_movement_service.py`
- **movement_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **Create a mock event bus.** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init_no_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_room_get_players()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test get_room_players() when room is not found.** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test validate_player_location() returns False when player is not in room.** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test add_player_to_room() when room is not found.** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_player_not_found()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_room_not_found()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_add_player_to_room_success()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_get_player_room_player_not_found()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_get_player_room_success()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_get_room_players()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_get_room_players_room_not_found()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_empty_player_id()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_from_room()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_invalid_to_room()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_same_room()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_remove_player_from_room_room_not_found()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_remove_player_from_room_success()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_location_false()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 22 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (4 shared connections)
- [[Room Occupancy Class]] (2 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Room Service Tests]] (1 shared connections)
- [[Async Persistence Core]] (1 shared connections)
- [[Realtime Event Delegation]] (1 shared connections)
- [[Player Combat XP]] (1 shared connections)

## Source Files

- `server/tests/unit/game/test_movement_service.py`
- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 107 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
