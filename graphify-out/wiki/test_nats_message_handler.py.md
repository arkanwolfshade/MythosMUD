# test_nats_message_handler.py

> 130 nodes

## Key Concepts

- **test_nats_message_handler.py** (72 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **NATSError** (67 connections) — `server/services/nats_exceptions.py`
- **asyncio** (55 connections)
- **CircuitBreakerOpen** (13 connections) — `server/realtime/circuit_breaker.py`
- **test_handle_nats_message_attribute_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_circuit_breaker_open()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_connection_manager_resolution_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_dlq_on_final_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_partial_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
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
- **test_handle_nats_message_success_path_metrics()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 105 more nodes in this community*

## Relationships

- [nats_exceptions.py](nats_exceptions.py.md) (22 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (9 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (3 shared connections)
- [NATSMessageHandlerMixinBase](NATSMessageHandlerMixinBase.md) (3 shared connections)
- [test_nats_message_handler_chat.py](test_nats_message_handler_chat.py.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (2 shared connections)
- [test_combat_persistence_handler_events.py](test_combat_persistence_handler_events.py.md) (2 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 251 (93%)
- INFERRED: 18 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*