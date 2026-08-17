# test_chat_nats_publisher.py

> 57 nodes

## Key Concepts

- **test_chat_nats_publisher.py** (36 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **chat_nats_publisher.py** (32 connections) — `server/game/chat_nats_publisher.py`
- **publish_chat_message_to_nats()** (29 connections) — `server/game/chat_nats_publisher.py`
- **_message()** (24 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **build_nats_subject()** (13 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (11 connections) — `server/game/chat_nats_publisher.py`
- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **_nats_service_ready()** (8 connections) — `server/game/chat_nats_publisher.py`
- **Any** (8 connections)
- **_extract_subzone_from_room()** (7 connections) — `server/game/chat_nats_publisher.py`
- **_build_nats_message_data()** (6 connections) — `server/game/chat_nats_publisher.py`
- **_chat_passes_nats_validation()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_system_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_handles_publish_error()** (5 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **asyncio** (5 connections)
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_unexpected_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_room_access_failure()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_success()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_unexpected_error()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_validation_failure()** (4 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_global()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_build_legacy_subject_local_uses_subzone()** (3 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- *... and 32 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (10 shared connections)
- [NATSError](NATSError.md) (6 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (5 shared connections)
- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (4 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (4 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (3 shared connections)
- [ChatMessage](ChatMessage.md) (3 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [SubjectValidator](SubjectValidator.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/tests/unit/game/test_chat_nats_publisher.py`

## Audit Trail

- EXTRACTED: 170 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*