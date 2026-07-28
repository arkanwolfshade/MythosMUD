# UI Player Event Handlers

> 118 nodes · cohesion 0.02

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **Any** (3 connections)
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **tutorial_room()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_room_add_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_containers()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_npcs()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 93 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (21 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (2 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (2 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (2 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (2 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (1 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (1 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (1 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 344 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*