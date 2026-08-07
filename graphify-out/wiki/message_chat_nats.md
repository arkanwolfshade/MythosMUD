# message chat nats

> 76 nodes

## Key Concepts

- **test_nats_message_handler_chat.py** (40 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_echo_message_to_sender_exception()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_broadcast_to_room_with_filtering_exception()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_extract_chat_message_fields()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_missing()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_build_chat_event()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_convert_ids_to_uuids()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_convert_ids_to_uuids_none_target()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_format_message_for_receiver()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_get_player_lucidity_tier()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_get_player_lucidity_tier_default()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_type_errors()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_sender_name_type_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_content_type_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_sender_id_type_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_extract_chat_message_fields_whisper_target_id()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_extract_chat_message_fields_system_target_id()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_build_chat_event_includes_speaker_kind()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_convert_ids_to_uuids_uuid_objects()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_process_message_with_retry_failure()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_broadcast_by_channel_type_exception()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_send_messages_to_players_no_original_content()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_send_messages_to_players_blocked()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_send_messages_to_players_with_tags()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- *... and 51 more nodes in this community*

## Relationships

- [game chat service](game_chat_service.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 154 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*