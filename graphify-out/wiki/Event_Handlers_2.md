# Event Handlers

> 53 nodes

## Key Concepts

- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (23 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **asyncio** (11 connections)
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **_npc_died_ids_or_warn()** (5 connections) — `server/realtime/event_handlers.py`
- **_participant_key_strings()** (5 connections) — `server/realtime/event_handlers.py`
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
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

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (9 shared connections)
- [Event Handlers](Event_Handlers.md) (4 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)
- [Nats Message Handler Broadcast](Nats_Message_Handler_Broadcast.md) (2 shared connections)
- [Test Envelope](Test_Envelope.md) (1 shared connections)
- [Test Nats Retry Handler](Test_Nats_Retry_Handler.md) (1 shared connections)
- [Test Dead Letter Queue](Test_Dead_Letter_Queue.md) (1 shared connections)
- [Test Circuit Breaker](Test_Circuit_Breaker.md) (1 shared connections)
- [Message Filtering](Message_Filtering.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 95 (87%)
- INFERRED: 14 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*