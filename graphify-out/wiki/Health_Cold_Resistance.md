# Health Cold Resistance

> 23 nodes

## Key Concepts

- **Room** (75 connections) — `server/models/room.py`
- **.npc_entered()** (4 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **test_room_player_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_has_object()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **.has_object()** (2 connections) — `server/models/room.py`
- **.has_npc()** (2 connections) — `server/models/room.py`
- **.__str__()** (2 connections) — `server/models/room.py`
- **.__repr__()** (2 connections) — `server/models/room.py`
- **mock_room()** (2 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Represents a room in the MythosMUD game world.      This class provides a statel** (1 connections) — `server/models/room.py`
- **Add an object to the room and trigger event.          Args:             object_i** (1 connections) — `server/models/room.py`
- **Remove an object from the room and trigger event.          Args:             obj** (1 connections) — `server/models/room.py`
- **Add an NPC to the room and trigger event.          Args:             npc_id: The** (1 connections) — `server/models/room.py`
- **Remove an NPC from the room and trigger event.          Args:             npc_id** (1 connections) — `server/models/room.py`
- **Check if an object is in the room.          Args:             object_id: The ID** (1 connections) — `server/models/room.py`
- **Check if an NPC is in the room.          Args:             npc_id: The ID of the** (1 connections) — `server/models/room.py`
- **String representation of the room.** (1 connections) — `server/models/room.py`
- **Detailed string representation of the room.** (1 connections) — `server/models/room.py`
- **Test Room.player_entered() adds player to room.** (1 connections) — `server/tests/unit/models/test_room_class.py`
- **Test Room.has_object() returns True if object in room.** (1 connections) — `server/tests/unit/models/test_room_class.py`

## Relationships

- [Dependency Injection Tests](Dependency_Injection_Tests.md) (18 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (14 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (5 shared connections)
- [Integration DB Fixtures](Integration_DB_Fixtures.md) (3 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (3 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (2 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Player Occupant Processor](Player_Occupant_Processor.md) (2 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (1 shared connections)
- [Client ASCII Map API](Client_ASCII_Map_API.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 108 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*