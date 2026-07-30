# spawn defaults

> 124 nodes

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **RoomRepository** (12 connections) — `server/persistence/repositories/room_repository.py`
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
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **tutorial_room()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_room_init()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_init_defaults()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered_string_id()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 99 more nodes in this community*

## Relationships

- [chat nats publisher](chat_nats_publisher.md) (12 shared connections)
- [world](world.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (6 shared connections)
- [real time](real_time.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [message formatters](message_formatters.md) (2 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (1 shared connections)
- [F](F.md) (1 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (1 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 360 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*