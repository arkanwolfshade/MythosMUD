# test_nats_message_handler.py

> 132 nodes

## Key Concepts

- **test_nats_message_handler.py** (72 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **asyncio** (55 connections)
- **CircuitBreakerOpen** (11 connections) — `server/realtime/circuit_breaker.py`
- **test_handle_nats_message_attribute_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_circuit_breaker_open()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_connection_manager_resolution_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_dlq_on_final_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_subscribe_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_partial_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_nats_error_returns_false()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_not_found()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_property_injected_returns_none()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_setter_updates_helpers()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_event_data_detection()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_event_type_detection()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_retry_on_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_runtime_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_success()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 107 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (15 shared connections)
- [test_circuit_breaker.py](test_circuit_breaker.py.md) (2 shared connections)
- [circuit_breaker.py](circuit_breaker.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [.call](call.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 210 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*