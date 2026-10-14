# ChatMessage

> 99 nodes

## Key Concepts

- **ChatMessage** (65 connections) — `server/game/chat_message.py`
- **chat_service.py** (60 connections) — `server/game/chat_service.py`
- **chat_nats_publisher.py** (34 connections) — `server/game/chat_nats_publisher.py`
- **chat_message.py** (23 connections) — `server/game/chat_message.py`
- **test_chat_event_category.py** (20 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **test_chat_pose_helpers.py** (17 connections) — `server/tests/unit/game/test_chat_pose_helpers.py`
- **set_player_pose()** (15 connections) — `server/game/chat_pose_helpers.py`
- **chat_pose_helpers.py** (15 connections) — `server/game/chat_pose_helpers.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **test_fake_npc_whisper_and_real_whisper_get_the_same_category()** (10 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **test_build_chat_event_tags_category_per_channel()** (8 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **clear_player_pose()** (7 connections) — `server/game/chat_pose_helpers.py`
- **get_player_pose()** (7 connections) — `server/game/chat_pose_helpers.py`
- **asyncio** (7 connections)
- **_CapturingNats** (6 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **store_global_message_in_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **get_room_poses()** (6 connections) — `server/game/chat_pose_helpers.py`
- **normalize_player_id()** (6 connections) — `server/game/chat_pose_helpers.py`
- **_publish_room_chat()** (6 connections) — `server/game/chat_service.py`
- **_chat_event_data()** (6 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **_chat_passes_nats_validation()** (5 connections) — `server/game/chat_nats_publisher.py`
- *... and 74 more nodes in this community*

## Relationships

- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (37 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (24 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (23 shared connections)
- [ChatService](ChatService.md) (21 shared connections)
- [test_chat_message_senders.py](test_chat_message_senders.py.md) (17 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (10 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (9 shared connections)
- [MessageCategory](MessageCategory.md) (5 shared connections)
- [NATSError](NATSError.md) (3 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (3 shared connections)
- [NpcDisposition](NpcDisposition.md) (2 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/game/test_chat_pose_helpers.py`
- `server/tests/unit/game/test_chat_service.py`
- `server/tests/unit/realtime/test_chat_event_category.py`

## Audit Trail

- EXTRACTED: 325 (92%)
- INFERRED: 30 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*