# nats message handler

> 122 nodes

## Key Concepts

- **test_nats_message_handler.py** (72 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_partial_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_not_found()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_circuit_breaker_open()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_dlq_on_final_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_subscribe_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_nats_error_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
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

- [nats exceptions services](nats_exceptions_services.md) (15 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (5 shared connections)
- [retry nats handler](retry_nats_handler.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 265 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*