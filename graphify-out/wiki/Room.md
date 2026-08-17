# Room

> 27 nodes

## Key Concepts

- **Room** (73 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **.has_npc()** (2 connections) — `server/models/room.py`
- **.has_object()** (2 connections) — `server/models/room.py`
- **.__repr__()** (2 connections) — `server/models/room.py`
- **.__str__()** (2 connections) — `server/models/room.py`
- **Add a player to the room without triggering an event. This method is used for…** (1 connections) — `server/models/room.py`
- **Remove a player from the room without triggering an event. This method is used…** (1 connections) — `server/models/room.py`
- **Remove a player from the room and trigger event. Args: player_id: The ID of the…** (1 connections) — `server/models/room.py`
- **Add an object to the room and trigger event. Args: object_id: The ID of the…** (1 connections) — `server/models/room.py`
- **Remove an object from the room and trigger event. Args: object_id: The ID of…** (1 connections) — `server/models/room.py`
- **Remove an NPC from the room and trigger event. Args: npc_id: The ID of the NPC…** (1 connections) — `server/models/room.py`
- **Represents a room in the MythosMUD game world. This class provides a stateless…** (1 connections) — `server/models/room.py`
- **Check if a player is in the room. Args: player_id: The ID of the player to…** (1 connections) — `server/models/room.py`
- **Check if an object is in the room. Args: object_id: The ID of the object to…** (1 connections) — `server/models/room.py`
- **Check if an NPC is in the room. Args: npc_id: The ID of the NPC to check…** (1 connections) — `server/models/room.py`
- **String representation of the room.** (1 connections) — `server/models/room.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_room_class.py](test_room_class.py.md) (22 shared connections)
- [NPCDefinition](NPCDefinition.md) (9 shared connections)
- [.to_dict](to_dict.md) (8 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (4 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [InstanceManager](InstanceManager.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (1 shared connections)
- [RoomRepository](RoomRepository.md) (1 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (1 shared connections)

## Source Files

- `server/models/room.py`

## Audit Trail

- EXTRACTED: 66 (67%)
- INFERRED: 32 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*