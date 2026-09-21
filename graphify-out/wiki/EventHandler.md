# EventHandler

> 55 nodes

## Key Concepts

- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (22 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **asyncio** (11 connections)
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **_npc_died_ids_or_warn()** (5 connections) — `server/realtime/event_handlers.py`
- **_participant_key_strings()** (5 connections) — `server/realtime/event_handlers.py`
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **test_handle_combat_ended_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_combat_started_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_event_message_dispatches_handler()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_event_message_invalid_skips()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_game_tick_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_npc_attacked_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_npc_died_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- *... and 30 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (12 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (3 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 92 (87%)
- INFERRED: 14 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*