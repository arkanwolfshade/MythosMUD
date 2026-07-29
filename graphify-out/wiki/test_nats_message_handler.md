# test nats message handler

> 67 nodes

## Key Concepts

- **test_nats_message_handler.py** (72 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_partial_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_dlq_on_final_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_subscribe_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_attribute_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _subscribe_to_standardized_chat_subjects handles NATSSubscribeError and con** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _process_single_message raises exception when event handler fails.** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_property_injected()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_setter()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_success()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_retry_on_failure()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_chat()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_event()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_room_no_subject_manager()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_get_active_subjects()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subzone()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_track_player_subzone_subscription()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_validation_error_missing_fields()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 42 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (9 shared connections)
- [circuit breaker](circuit_breaker.md) (4 shared connections)
- [Test handle nats message handles](Test_handle_nats_message_handles.md) (3 shared connections)
- [Test subscribe to subject returns](Test_subscribe_to_subject_returns.md) (3 shared connections)
- [nats retry handler](nats_retry_handler.md) (2 shared connections)
- [Test subscribe to chat subjects()](Test_subscribe_to_chat_subjects%28%29.md) (2 shared connections)
- [Test subscribe to event subjects()](Test_subscribe_to_event_subjects%28%29.md) (2 shared connections)
- [Test unsubscribe from subject() handles](Test_unsubscribe_from_subject%28%29_handles.md) (2 shared connections)
- [nats config()](nats_config%28%29.md) (1 shared connections)
- [Test connection manager property falls](Test_connection_manager_property_falls.md) (1 shared connections)
- [Test connection manager setter updates](Test_connection_manager_setter_updates.md) (1 shared connections)
- [Test get subscription count returns](Test_get_subscription_count_returns.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 187 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*