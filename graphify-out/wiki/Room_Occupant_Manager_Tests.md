# Room Occupant Manager Tests

> 31 nodes · cohesion 0.06

## Key Concepts

- **test_room_occupant_manager.py** (15 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **occupant_manager()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_get_players_error()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants() returns empty list when room not found.** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_cache_not_found()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants returns occupants.** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants handles errors gracefully.** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_error()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_no_persistence()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_no_room()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_success()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_with_ensure_player()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_with_players_and_npcs()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_room_occupant_manager_init()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_separate_occupants_by_type()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_separate_occupants_by_type_empty_list()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_add_room_occupant_error_handling()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager.py`
- **Unit tests for room occupant manager.  Tests the RoomOccupantManager class for q** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants with ensure_player_included.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants returns both players and NPCs.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants handles get_players error.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test separate_occupants_by_type with empty list.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- *... and 6 more nodes in this community*

## Relationships

- [[Player Respawn Events]] (3 shared connections)
- [[Room Service Tests]] (1 shared connections)
- [[Game State Provider Tests]] (1 shared connections)
- [[Services Service Room]] (1 shared connections)
- [[Realtime Room Subscription]] (1 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/realtime/integration/test_game_state_provider.py`
- `server/tests/unit/realtime/test_room_occupant_manager.py`
- `server/tests/unit/realtime/test_room_subscription_manager.py`

## Audit Trail

- EXTRACTED: 66 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
