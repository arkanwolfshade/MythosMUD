# .test_on_sanitarium_failover_debounced_does_not_invoke_callback_twice

> 2 nodes

## Key Concepts

- **test_get_event_handler_map()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _get_event_handler_map delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Relationships

- [Connection State Hooks](Connection_State_Hooks.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Audit Trail

- EXTRACTED: 3 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*