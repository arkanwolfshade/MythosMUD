# chat_nats_publisher.py

> 39 nodes

## Key Concepts

- **chat_nats_publisher.py** (32 connections) — `server/game/chat_nats_publisher.py`
- **test_chat_validator.py** (22 connections) — `server/tests/unit/game/test_chat_validator.py`
- **chat_message.py** (19 connections) — `server/game/chat_message.py`
- **validate_chat_message()** (12 connections) — `server/game/chat_validator.py`
- **chat_validator.py** (10 connections) — `server/game/chat_validator.py`
- **validate_room_access()** (9 connections) — `server/game/chat_validator.py`
- **_message()** (8 connections) — `server/tests/unit/game/test_chat_validator.py`
- **contains_malicious_content()** (7 connections) — `server/game/chat_validator.py`
- **_chat_passes_nats_validation()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_unexpected_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **test_contains_malicious_content_detects_patterns()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_accepts_valid_message()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_handles_invalid_object()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_rejects_empty_content()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_rejects_malicious_script()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_rejects_missing_sender()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_rejects_too_long_content()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **.__init__()** (2 connections) — `server/game/chat_message.py`
- **test_contains_malicious_content_allows_safe_text()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_contains_malicious_content_fails_safe_on_type_error()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_room_access_accepts_valid_room()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_room_access_allows_none_room_for_system()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_room_access_rejects_blank_room_id()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_room_access_rejects_empty_sender()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- *... and 14 more nodes in this community*

## Relationships

- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (15 shared connections)
- [ChatMessage](ChatMessage.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [chat_service.py](chat_service.py.md) (6 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [NATSPublishError](NATSPublishError.md) (2 shared connections)
- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (2 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_validator.py`
- `server/tests/unit/game/test_chat_validator.py`

## Audit Trail

- EXTRACTED: 114 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*