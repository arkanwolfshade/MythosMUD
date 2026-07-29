# spawn defaults

> 120 nodes

## Key Concepts

- **Room** (72 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **room.py** (28 connections) — `server/models/room.py`
- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **instance_manager.py** (12 connections) — `server/game/instance_manager.py`
- **RoomRepository** (12 connections) — `server/persistence/repositories/room_repository.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **room_repository.py** (7 connections) — `server/persistence/repositories/room_repository.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **spawn_defaults.py** (4 connections) — `server/constants/spawn_defaults.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **Any** (3 connections)
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **tutorial_room()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_room_init()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_init_defaults()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered_string_id()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered_empty_id()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_add_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 95 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (24 shared connections)
- [. init ()](_init_%28%29.md) (7 shared connections)
- [Any](Any.md) (7 shared connections)
- [.initialize()](initialize%28%29.md) (6 shared connections)
- [UUID](UUID.md) (6 shared connections)
- [Instance](Instance.md) (5 shared connections)
- [Player Position Service](Player_Position_Service.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (2 shared connections)
- [. repr ()](_repr_%28%29.md) (2 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (2 shared connections)
- [websocket handler connection](websocket_handler_connection.md) (2 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/game/instance_manager.py`
- `server/models/room.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 385 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*