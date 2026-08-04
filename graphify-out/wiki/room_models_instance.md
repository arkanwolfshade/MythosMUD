# room models instance

> 102 nodes

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.npc_entered()** (4 connections) — `server/models/room.py`
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
- *... and 77 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (15 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (2 shared connections)
- [target resolution service](target_resolution_service.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [persistence protocols rationale](persistence_protocols_rationale.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 308 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*