# EventHandler

> 53 nodes

## Key Concepts

- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (23 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **asyncio** (11 connections)
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
- **test_handle_player_entered_missing_room_id()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- *... and 28 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (19 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 88 (86%)
- INFERRED: 14 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*