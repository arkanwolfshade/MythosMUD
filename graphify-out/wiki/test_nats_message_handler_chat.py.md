# test_nats_message_handler_chat.py

> 10 nodes · cohesion 0.20

## Key Concepts

- **test_nats_message_handler_chat.py** (38 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_apply_dampening_and_send_message_exception()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_apply_dampening_and_send_message_no_original_content()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_extract_chat_message_fields_whisper_target_id()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_should_echo_to_sender_no_targets_not_notified()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Unit tests for NATS message handler chat and messaging.  Tests chat field extrac** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _extract_chat_message_fields handles whisper target_id.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _should_echo_to_sender returns True when no targets but not notified.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _apply_dampening_and_send_message handles missing original_content.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _apply_dampening_and_send_message handles exceptions.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Relationships

- [CombatService](CombatService.md) (2 shared connections)
- [test_apply_dampening_and_send_message_blocked](test_apply_dampening_and_send_message_blocked.md) (1 shared connections)
- [test_broadcast_by_channel_type_exception](test_broadcast_by_channel_type_exception.md) (1 shared connections)
- [test_broadcast_to_room_with_filtering_exception](test_broadcast_to_room_with_filtering_exception.md) (1 shared connections)
- [test_build_chat_event](test_build_chat_event.md) (1 shared connections)
- [test_convert_ids_to_uuids](test_convert_ids_to_uuids.md) (1 shared connections)
- [test_convert_ids_to_uuids_none_target](test_convert_ids_to_uuids_none_target.md) (1 shared connections)
- [test_convert_ids_to_uuids_uuid_objects](test_convert_ids_to_uuids_uuid_objects.md) (1 shared connections)
- [test_echo_message_to_sender_exception](test_echo_message_to_sender_exception.md) (1 shared connections)
- [test_echo_message_to_sender_success](test_echo_message_to_sender_success.md) (1 shared connections)
- [test_extract_chat_message_fields](test_extract_chat_message_fields.md) (1 shared connections)
- [test_format_message_for_receiver](test_format_message_for_receiver.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*