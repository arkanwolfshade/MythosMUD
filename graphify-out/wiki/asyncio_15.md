# asyncio

> 17 nodes

## Key Concepts

- **asyncio** (24 connections)
- **test_cleanup_empty_subzone_subscriptions_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_subscribe_to_subzone_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_subzone_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_cleanup_empty_subzone_subscriptions()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_event_message()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_attacked_event()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_event_subjects_partial()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_subzone_not_subscribed()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test cleanup_empty_subzone_subscriptions cleans up empty subzones.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test subscribe_to_subzone handles errors.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test unsubscribe_from_event_subjects handles partial success.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test cleanup_empty_subzone_subscriptions handles NATSError.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _handle_player_attacked_event delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test unsubscribe_from_subzone handles not subscribed case.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _handle_event_message delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test unsubscribe_from_subzone handles errors.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Relationships

- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (8 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_handle_combat_ended_event](test_handle_combat_ended_event.md) (1 shared connections)
- [test_handle_combat_started_event](test_handle_combat_started_event.md) (1 shared connections)
- [test_handle_npc_attacked_event](test_handle_npc_attacked_event.md) (1 shared connections)
- [test_handle_npc_died_event](test_handle_npc_died_event.md) (1 shared connections)
- [test_handle_npc_took_damage_event](test_handle_npc_took_damage_event.md) (1 shared connections)
- [test_handle_player_movement_different_subzone](test_handle_player_movement_different_subzone.md) (1 shared connections)
- [test_handle_player_movement_error](test_handle_player_movement_error.md) (1 shared connections)
- [test_handle_player_movement_exception](test_handle_player_movement_exception.md) (1 shared connections)
- [test_handle_player_movement_new_subzone_none](test_handle_player_movement_new_subzone_none.md) (1 shared connections)
- [test_handle_player_movement_old_subzone_none](test_handle_player_movement_old_subzone_none.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*