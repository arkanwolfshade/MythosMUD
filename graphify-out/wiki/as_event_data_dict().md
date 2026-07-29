# as event data dict()

> 47 nodes

## Key Concepts

- **EventHandler** (22 connections) — `server/realtime/event_handlers.py`
- **_EventBusPublishPort** (7 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (7 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (6 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (5 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.publish()** (3 connections) — `server/realtime/event_handlers.py`
- **_npc_died_ids_or_warn()** (3 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (3 connections) — `server/realtime/event_handlers.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.handle_player_entered_event()** (2 connections) — `server/realtime/event_handlers.py`
- **.handle_player_left_event()** (2 connections) — `server/realtime/event_handlers.py`
- **.handle_game_tick_event()** (2 connections) — `server/realtime/event_handlers.py`
- **Protocol** (1 connections)
- **Minimal surface for publishing domain events from ConnectionManager.event_bus.** (1 connections) — `server/realtime/event_handlers.py`
- *... and 22 more nodes in this community*

## Relationships

- [UUID](UUID.md) (11 shared connections)
- [Player](Player.md) (6 shared connections)
- [. repr ()](_repr_%28%29.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 122 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*