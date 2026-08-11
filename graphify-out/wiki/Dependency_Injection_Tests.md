# Dependency Injection Tests

> 101 nodes

## Key Concepts

- **Room** (75 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **Any** (3 connections)
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **tutorial_room()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_room_init()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_init_defaults()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered_string_id()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 76 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (9 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (4 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (3 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (2 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (2 shared connections)
- [Conftest Migration Plan](Conftest_Migration_Plan.md) (1 shared connections)
- [Room Map Viewer UI](Room_Map_Viewer_UI.md) (1 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (1 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 306 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*