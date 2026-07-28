# Server Models (23)

> 29 nodes

## Key Concepts

- **Room** (70 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **test_room_player_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_remove_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_left()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_npc_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_occupant_count()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_repr()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **.has_object()** (2 connections) — `server/models/room.py`
- **.has_npc()** (2 connections) — `server/models/room.py`
- **.__str__()** (2 connections) — `server/models/room.py`
- **.__repr__()** (2 connections) — `server/models/room.py`
- **mock_room()** (2 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Represents a room in the MythosMUD game world.      This class provides a statel** (1 connections) — `server/models/room.py`
- **Add an object to the room and trigger event.          Args:             object_i** (1 connections) — `server/models/room.py`
- **Remove an object from the room and trigger event.          Args:             obj** (1 connections) — `server/models/room.py`
- **Remove an NPC from the room and trigger event.          Args:             npc_id** (1 connections) — `server/models/room.py`
- **Check if an object is in the room.          Args:             object_id: The ID** (1 connections) — `server/models/room.py`
- **Check if an NPC is in the room.          Args:             npc_id: The ID of the** (1 connections) — `server/models/room.py`
- **String representation of the room.** (1 connections) — `server/models/room.py`
- **Detailed string representation of the room.** (1 connections) — `server/models/room.py`
- **Test Room.player_entered() adds player to room.** (1 connections) — `server/tests/unit/models/test_room_class.py`
- **Test Room.remove_player_silently() removes player without event.** (1 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 4 more nodes in this community*

## Relationships

- [Server Models (18)](Server_Models_%2818%29.md) (24 shared connections)
- [Server Models (27)](Server_Models_%2827%29.md) (8 shared connections)
- [Server Events](Server_Events.md) (5 shared connections)
- [Server Models (34)](Server_Models_%2834%29.md) (5 shared connections)
- [Server Admin](Server_Admin.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (3 shared connections)
- [Server (5)](Server_%285%29.md) (1 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (1 shared connections)
- [Server Npc](Server_Npc.md) (1 shared connections)
- [Server Services](Server_Services.md) (1 shared connections)
- [Server Persistence (10)](Server_Persistence_%2810%29.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 115 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*