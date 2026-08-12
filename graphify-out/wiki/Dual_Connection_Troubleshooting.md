# Dual Connection Troubleshooting

> 28 nodes

## Key Concepts

- **test_room_occupant_manager.py** (16 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **occupant_manager()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_get_players_error()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_room_occupant_manager_init()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_no_persistence()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_no_room()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_success()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_error()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_separate_occupants_by_type()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_with_ensure_player()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_with_players_and_npcs()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_separate_occupants_by_type_empty_list()** (2 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Unit tests for room occupant manager.  Tests the RoomOccupantManager class for q** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Create mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Create RoomOccupantManager instance.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test RoomOccupantManager initialization.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants returns empty when no connection manager.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants returns empty when no persistence.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants returns empty when room not found.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants returns occupants.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants handles errors gracefully.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test separate_occupants_by_type separates occupants.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants with ensure_player_included.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- *... and 3 more nodes in this community*

## Relationships

- [Character Creation E2E](Character_Creation_E2E.md) (3 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (1 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 58 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*