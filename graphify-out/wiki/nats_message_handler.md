# nats message handler

> 118 nodes

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
- **test_handle_nats_message_retry_on_failure()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 93 more nodes in this community*

## Relationships

- [game chat service](game_chat_service.md) (9 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (4 shared connections)
- [commands communication say](commands_communication_say.md) (4 shared connections)
- [follow game service](follow_game_service.md) (3 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)
- [room sync service](room_sync_service.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 257 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*