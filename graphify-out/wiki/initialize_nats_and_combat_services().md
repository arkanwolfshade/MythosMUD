# initialize nats and combat services()

> 122 nodes

## Key Concepts

- **test_nats_message_handler.py** (72 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_nats_message_handler_init()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_partial_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_circuit_breaker_open()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_dlq_on_final_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_nats_error_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_connection_manager_resolution_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_attribute_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_property_injected()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_property_fallback()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_setter()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_without_event_subscriptions()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_chat_subjects_no_subject_manager()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 97 more nodes in this community*

## Relationships

- [Any](Any.md) (9 shared connections)
- [circuit breaker](circuit_breaker.md) (4 shared connections)
- [test combat persistence handler events](test_combat_persistence_handler_events.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [correct patterns](correct_patterns.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 263 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*