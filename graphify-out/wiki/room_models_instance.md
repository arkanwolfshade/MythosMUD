# room models instance

> 71 nodes

## Key Concepts

- **Room** (74 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **test_room_init()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_init_defaults()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered_string_id()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered_empty_id()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_add_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_remove_player_silently()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_left()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_object_added()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_object_removed()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_npc_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_npc_left()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_players()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_objects()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_npcs()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_has_player()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_has_player_false()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_has_object()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_has_npc()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_get_occupant_count()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 46 more nodes in this community*

## Relationships

- [event events serialization](event_events_serialization.md) (8 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (7 shared connections)
- [status game spell](status_game_spell.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [persistence protocols rationale](persistence_protocols_rationale.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (2 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (2 shared connections)
- [combat npc services](combat_npc_services.md) (1 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 229 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*