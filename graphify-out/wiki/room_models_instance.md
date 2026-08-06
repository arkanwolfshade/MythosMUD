# room models instance

> 108 nodes

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **RoomRepository** (17 connections) — `server/persistence/repositories/room_repository.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **room_repository.py** (8 connections) — `server/persistence/repositories/room_repository.py`
- **test_room_repository.py** (7 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **UUID** (6 connections)
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
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **test_room_init()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_init_defaults()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered_string_id()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered_empty_id()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_add_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 83 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (15 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [persistence protocols rationale](persistence_protocols_rationale.md) (3 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (2 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (2 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (1 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 336 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*