# spawn defaults

> 119 nodes

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
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
- *... and 94 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (19 shared connections)
- [UUID](UUID.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [real time](real_time.md) (3 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (1 shared connections)
- [.is required()](is_required%28%29.md) (1 shared connections)
- [test command service](test_command_service.md) (1 shared connections)
- [PasswordHasher](PasswordHasher.md) (1 shared connections)
- [container helpers inventory find](container_helpers_inventory_find.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 345 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*