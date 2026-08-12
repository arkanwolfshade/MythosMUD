# test_nats_message_handler.py

> 111 nodes

## Key Concepts

- **test_nats_message_handler.py** (72 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **asyncio** (55 connections)
- **test_handle_nats_message_attribute_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_connection_manager_resolution_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_dlq_on_final_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_subscribe_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_nats_error_returns_false()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_property_injected_returns_none()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_setter_updates_helpers()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_event_data_detection()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_event_type_detection()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_retry_on_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_success()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_success_path_metrics()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_validation_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_message_with_retry_exhaustion()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_message_with_retry_success_path()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_broadcast_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_chat()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 86 more nodes in this community*

## Relationships

- [build_event](build_event.md) (13 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (6 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [test_subscribe_to_standardized_chat_subjects_partial_failure](test_subscribe_to_standardized_chat_subjects_partial_failure.md) (2 shared connections)
- [test_unsubscribe_from_subject_not_found](test_unsubscribe_from_subject_not_found.md) (2 shared connections)
- [test_unsubscribe_from_subzone](test_unsubscribe_from_subzone.md) (2 shared connections)
- [test_process_single_message_validation_error_type_error](test_process_single_message_validation_error_type_error.md) (2 shared connections)
- [test_handle_nats_message_runtime_error](test_handle_nats_message_runtime_error.md) (2 shared connections)
- [test_subscribe_to_subject_runtime_error_returns_false](test_subscribe_to_subject_runtime_error_returns_false.md) (2 shared connections)
- [test_handle_nats_message_unknown_channel_defaults](test_handle_nats_message_unknown_channel_defaults.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 345 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*