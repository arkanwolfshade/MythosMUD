# Room

> 30 nodes

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **.npc_entered()** (4 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **test_room_add_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_players()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_init()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_is_empty()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_object_added()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_str()** (3 connections) — `server/tests/unit/models/test_room_class.py`
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
- **Test Room.object_added() adds object to room.** (1 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 5 more nodes in this community*

## Relationships

- [test_room_class.py](test_room_class.py.md) (25 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [.to_dict](to_dict.md) (8 shared connections)
- [UUID](UUID.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (3 shared connections)
- [test_instance_manager.py](test_instance_manager.py.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [test_room_has_object](test_room_has_object.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 94 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*