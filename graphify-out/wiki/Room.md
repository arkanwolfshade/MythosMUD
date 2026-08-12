# Room

> 129 nodes

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **instance_manager.py** (12 connections) — `server/game/instance_manager.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **._compute_player_context()** (5 connections) — `server/npc/aggressive_mob_npc.py`
- **instance_manager()** (5 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **._enrich_behavior_context()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **tutorial_room()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- *... and 104 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (12 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (8 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [GameBundle](GameBundle.md) (5 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (2 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (2 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)

## Source Files

- `server/game/instance_manager.py`
- `server/models/room.py`
- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 213 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*