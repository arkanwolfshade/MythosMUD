# test_chat_nats_publisher.py

> 101 nodes

## Key Concepts

- **test_chat_nats_publisher.py** (36 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **chat_nats_publisher.py** (32 connections) — `server/game/chat_nats_publisher.py`
- **publish_chat_message_to_nats()** (29 connections) — `server/game/chat_nats_publisher.py`
- **_message()** (24 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **test_room_utils.py** (22 connections) — `server/tests/unit/utils/test_room_utils.py`
- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **build_nats_subject()** (13 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (11 connections) — `server/game/chat_nats_publisher.py`
- **room_utils.py** (10 connections) — `server/utils/room_utils.py`
- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **_nats_service_ready()** (8 connections) — `server/game/chat_nats_publisher.py`
- **Any** (8 connections)
- **_extract_subzone_from_room()** (7 connections) — `server/game/chat_nats_publisher.py`
- **_build_nats_message_data()** (6 connections) — `server/game/chat_nats_publisher.py`
- **get_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **get_plane_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **get_subzone_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **get_zone_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **_chat_passes_nats_validation()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_system_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **test_publish_chat_message_to_nats_handles_publish_error()** (5 connections) — `server/tests/unit/game/test_chat_nats_publisher.py`
- **is_valid_room_id_format()** (5 connections) — `server/utils/room_utils.py`
- **asyncio** (5 connections)
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- *... and 76 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (7 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (5 shared connections)
- [ChatMessage](ChatMessage.md) (5 shared connections)
- [NATSPublishError](NATSPublishError.md) (4 shared connections)
- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (4 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [SubjectValidator](SubjectValidator.md) (2 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [ChatService](ChatService.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/tests/unit/game/test_chat_nats_publisher.py`
- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 244 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*