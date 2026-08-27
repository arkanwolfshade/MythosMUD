# test_check_no_production_assert.py

> 17 nodes

## Key Concepts

- **asyncio** (24 connections)
- **test_cleanup_empty_subzone_subscriptions()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_cleanup_empty_subzone_subscriptions_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_event_message()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_attacked_event()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_subscribe_to_subzone_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_event_subjects_partial()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_subzone_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
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

- [](unnamed.md) (16 shared connections)
- [Animate Skill](Animate_Skill.md) (8 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*