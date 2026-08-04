# player occupant processor

> 36 nodes

## Key Concepts

- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **test_room_occupant_manager.py** (16 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **Any** (3 connections)
- **.separate_occupants_by_type()** (3 connections) — `server/realtime/room_occupant_manager.py`
- **occupant_manager()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **UUID** (2 connections)
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
- **Manages room occupant queries and processing.      Handles both players and NPCs** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Initialize the room occupant manager.          Args:             connection_mana** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Get the list of occupants in a room.          Args:             room_id: The roo** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Separate occupants into players, NPCs, and all occupants lists.          Args:** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Unit tests for room occupant manager.  Tests the RoomOccupantManager class for q** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Create mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- *... and 11 more nodes in this community*

## Relationships

- [event bus events](event_bus_events.md) (7 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (3 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (2 shared connections)
- [schedule services service](schedule_services_service.md) (2 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (2 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (2 shared connections)
- [logging processors structured](logging_processors_structured.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 94 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*