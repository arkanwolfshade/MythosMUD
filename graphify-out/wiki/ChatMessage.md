# ChatMessage

> 41 nodes

## Key Concepts

- **ChatMessage** (59 connections) — `server/game/chat_message.py`
- **chat_message.py** (19 connections) — `server/game/chat_message.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- **test_chat_message_helpers.py** (12 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **store_message_in_room_history()** (11 connections) — `server/game/chat_message_helpers.py`
- **create_and_log_say_message()** (7 connections) — `server/game/chat_message_helpers.py`
- **store_global_message_in_history()** (6 connections) — `server/game/chat_message_helpers.py`
- **.to_dict()** (3 connections) — `server/game/chat_message.py`
- **test_create_and_log_chat_message()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_store_global_message_in_history_trims()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_store_message_in_room_history_creates_and_trims()** (3 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **test_chat_message_to_dict_includes_speaker_kind()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_chat_message_init()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_init_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_log_message()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_echo_sent()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **.__init__()** (2 connections) — `server/game/chat_message.py`
- **.log_message()** (2 connections) — `server/game/chat_message.py`
- **test_create_and_log_say_message()** (2 connections) — `server/tests/unit/game/test_chat_message_helpers.py`
- **UUID** (2 connections)
- **Any** (1 connections)
- **Message creation and storage helpers for chat service.** (1 connections) — `server/game/chat_message_helpers.py`
- *... and 16 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (27 shared connections)
- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (15 shared connections)
- [ChatService](ChatService.md) (15 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (14 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (5 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (5 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 123 (86%)
- INFERRED: 20 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*