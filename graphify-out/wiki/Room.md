# Room

> 22 nodes

## Key Concepts

- **Room** (62 connections) — `server/models/room.py`
- **.npc_entered()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **test_room_has_object()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_npc_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **.has_npc()** (2 connections) — `server/models/room.py`
- **.has_object()** (2 connections) — `server/models/room.py`
- **.__repr__()** (2 connections) — `server/models/room.py`
- **.__str__()** (2 connections) — `server/models/room.py`
- **Add an object to the room and trigger event. Args: object_id: The ID of the…** (1 connections) — `server/models/room.py`
- **Remove an object from the room and trigger event. Args: object_id: The ID of…** (1 connections) — `server/models/room.py`
- **Add an NPC to the room and trigger event. Args: npc_id: The ID of the NPC…** (1 connections) — `server/models/room.py`
- **Remove an NPC from the room and trigger event. Args: npc_id: The ID of the NPC…** (1 connections) — `server/models/room.py`
- **Represents a room in the MythosMUD game world. This class provides a stateless…** (1 connections) — `server/models/room.py`
- **Check if an object is in the room. Args: object_id: The ID of the object to…** (1 connections) — `server/models/room.py`
- **Check if an NPC is in the room. Args: npc_id: The ID of the NPC to check…** (1 connections) — `server/models/room.py`
- **String representation of the room.** (1 connections) — `server/models/room.py`
- **Detailed string representation of the room.** (1 connections) — `server/models/room.py`
- **Test Room.npc_entered() adds NPC to room.** (1 connections) — `server/tests/unit/models/test_room_class.py`
- **Test Room.has_object() returns True if object in room.** (1 connections) — `server/tests/unit/models/test_room_class.py`

## Relationships

- [Test Room Class](Test_Room_Class.md) (27 shared connections)
- [Room](Room.md) (13 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (5 shared connections)
- [Test Movement Service](Test_Movement_Service.md) (2 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (2 shared connections)
- [Test Room Utils](Test_Room_Utils.md) (1 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (1 shared connections)
- [Room Repository](Room_Repository.md) (1 shared connections)
- [Test Player Disconnect Handlers](Test_Player_Disconnect_Handlers.md) (1 shared connections)
- [Websocket Handler Connection](Websocket_Handler_Connection.md) (1 shared connections)
- [Test Target Resolution Service](Test_Target_Resolution_Service.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 76 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*