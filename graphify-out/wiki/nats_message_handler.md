# nats message handler

> 104 nodes

## Key Concepts

- **test_nats_message_handler.py** (72 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_nats_message_handler_init()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_not_found()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_connection_manager_resolution_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
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
- **test_handle_nats_message_retry_on_failure()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_no_subject_manager()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_chat()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_event()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_room()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_room_no_subject_manager()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_room()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_get_subscription_count()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 79 more nodes in this community*

## Relationships

- [message filtering realtime](message_filtering_realtime.md) (9 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (4 shared connections)
- [container main rationale](container_main_rationale.md) (3 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (3 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)
- [look helpers commands](look_helpers_commands.md) (2 shared connections)
- [service services rescue](service_services_rescue.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 227 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*