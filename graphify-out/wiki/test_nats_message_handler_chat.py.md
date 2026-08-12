# test_nats_message_handler_chat.py

> 16 nodes

## Key Concepts

- **test_nats_message_handler_chat.py** (38 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_convert_ids_to_uuids_uuid_objects()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_should_echo_to_sender_no_message_id()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_should_echo_to_sender_not_chat_message()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_missing()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_sender_id_type_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_type_errors()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Unit tests for NATS message handler chat and messaging. Tests chat field…** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields raises TypeError for invalid types.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields raises TypeError for invalid sender_id type.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _convert_ids_to_uuids handles UUID objects.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _should_echo_to_sender returns False for non-chat messages.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _should_echo_to_sender returns False when message_id is None.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields validates fields.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields raises error when fields missing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Relationships

- [asyncio](asyncio.md) (7 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [test_get_player_lucidity_tier_default](test_get_player_lucidity_tier_default.md) (1 shared connections)
- [test_validate_chat_message_fields_sender_name_type_error](test_validate_chat_message_fields_sender_name_type_error.md) (1 shared connections)
- [test_validate_chat_message_fields_content_type_error](test_validate_chat_message_fields_content_type_error.md) (1 shared connections)
- [test_extract_chat_message_fields_whisper_target_id](test_extract_chat_message_fields_whisper_target_id.md) (1 shared connections)
- [test_extract_chat_message_fields](test_extract_chat_message_fields.md) (1 shared connections)
- [test_process_message_with_retry_failure](test_process_message_with_retry_failure.md) (1 shared connections)
- [test_broadcast_by_channel_type_exception](test_broadcast_by_channel_type_exception.md) (1 shared connections)
- [test_send_messages_to_players_blocked](test_send_messages_to_players_blocked.md) (1 shared connections)
- [test_should_echo_to_sender_not_echo_channel](test_should_echo_to_sender_not_echo_channel.md) (1 shared connections)
- [test_should_echo_to_sender_with_targets](test_should_echo_to_sender_with_targets.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*