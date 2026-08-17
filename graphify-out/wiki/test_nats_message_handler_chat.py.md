# test_nats_message_handler_chat.py

> 18 nodes

## Key Concepts

- **test_nats_message_handler_chat.py** (41 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_build_chat_event_includes_speaker_kind()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_convert_ids_to_uuids_uuid_objects()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_extract_chat_message_fields()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_extract_chat_message_fields_system_target_id()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_should_echo_to_sender_no_message_id()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_should_echo_to_sender_with_targets()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_missing()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_sender_id_type_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Unit tests for NATS message handler chat and messaging. Tests chat field…** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields raises TypeError for invalid sender_id type.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _extract_chat_message_fields extracts fields.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Personal system chat maps target_id to target_player_id and keeps speaker_kind.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Chat WebSocket event carries speaker_kind for client pass-through.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _convert_ids_to_uuids handles UUID objects.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _should_echo_to_sender returns False when message_id is None.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _should_echo_to_sender returns True when targets exist.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields raises error when fields missing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Relationships

- [asyncio](asyncio.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [test_get_player_lucidity_tier_default](test_get_player_lucidity_tier_default.md) (1 shared connections)
- [test_validate_chat_message_fields_type_errors](test_validate_chat_message_fields_type_errors.md) (1 shared connections)
- [test_validate_chat_message_fields_sender_name_type_error](test_validate_chat_message_fields_sender_name_type_error.md) (1 shared connections)
- [test_validate_chat_message_fields_content_type_error](test_validate_chat_message_fields_content_type_error.md) (1 shared connections)
- [test_extract_chat_message_fields_whisper_target_id](test_extract_chat_message_fields_whisper_target_id.md) (1 shared connections)
- [test_process_message_with_retry_failure](test_process_message_with_retry_failure.md) (1 shared connections)
- [test_broadcast_by_channel_type_exception](test_broadcast_by_channel_type_exception.md) (1 shared connections)
- [test_send_messages_to_players_no_original_content](test_send_messages_to_players_no_original_content.md) (1 shared connections)
- [test_send_messages_to_players_with_tags](test_send_messages_to_players_with_tags.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*