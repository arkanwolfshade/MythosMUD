# server tests unit realtime test

> 15 nodes

## Key Concepts

- **test_nats_message_handler_chat.py** (41 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields raises TypeError for invalid types.** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_build_chat_event()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_convert_ids_to_uuids_none_target()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_extract_chat_message_fields_whisper_target_id()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_should_echo_to_sender_not_chat_message()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_content_type_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_sender_id_type_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_sender_name_type_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_type_errors()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Unit tests for NATS message handler chat and messaging. Tests chat field…** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _extract_chat_message_fields handles whisper target_id.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _should_echo_to_sender returns False for non-chat messages.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _build_chat_event builds event.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _convert_ids_to_uuids handles None target.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Relationships

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (29 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*