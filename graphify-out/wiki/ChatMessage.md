# ChatMessage

> 63 nodes

## Key Concepts

- **ChatMessage** (59 connections) — `server/game/chat_message.py`
- **chat_channel_message_senders.py** (39 connections) — `server/game/chat_channel_message_senders.py`
- **test_chat_message_senders.py** (28 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **ChatSendServices** (20 connections) — `server/game/chat_channel_message_senders.py`
- **send_whisper_message()** (17 connections) — `server/game/chat_channel_message_senders.py`
- **send_system_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **send_global_message()** (14 connections) — `server/game/chat_channel_message_senders.py`
- **_attr()** (13 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **asyncio** (13 connections)
- **_ctx()** (12 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_channel_message_senders.py`
- **_player()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **ChatResult** (10 connections)
- **ChatPlayerView** (9 connections) — `server/game/chat_channel_message_senders.py`
- **_publish_chat_or_unavailable()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **WhisperTracker** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_whisper_message()** (8 connections) — `server/game/chat_channel_message_senders.py`
- **_authorize_global_sender()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **_log_and_store_system_message()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **normalize_player_id()** (7 connections) — `server/game/chat_channel_message_senders.py`
- **test_send_global_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_rate_limit_and_nats_fail()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_system_message_validation_and_auth()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **test_send_whisper_message_success()** (7 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- *... and 38 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (41 shared connections)
- [chat_message.py](chat_message.py.md) (15 shared connections)
- [ChatService](ChatService.md) (13 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (7 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (7 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (3 shared connections)
- [test_chat_pose_helpers.py](test_chat_pose_helpers.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_senders.py`

## Audit Trail

- EXTRACTED: 232 (84%)
- INFERRED: 43 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*