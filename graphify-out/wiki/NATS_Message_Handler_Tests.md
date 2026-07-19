# NATS Message Handler Tests

> 113 nodes · cohesion 0.02

## Key Concepts

- **test_nats_message_handler.py** (69 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _subscribe_to_standardized_chat_subjects handles NATSSubscribeError and con** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _process_single_message raises exception when event handler fails.** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_attribute_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_circuit_breaker_open()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_connection_manager_resolution_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_dlq_on_final_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_runtime_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_broadcast_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_event_handler_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_subscribe_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_partial_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_runtime_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_nats_error_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_runtime_error_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_not_found()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _subscribe_to_chat_subjects() raises error when subject manager not availab** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _process_single_message processes chat message.** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _handle_nats_message handles RuntimeError and adds to DLQ.** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 88 more nodes in this community*

## Relationships

- [[Combat Domain Events]] (15 shared connections)
- [[Database Manager Tests]] (6 shared connections)
- [[NATS Chat Broadcasting]] (3 shared connections)
- [[Services Service Room]] (2 shared connections)
- [[NATS Retry Handler]] (1 shared connections)
- [[Realtime Nats Message]] (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 265 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
