# Chat Service & Channels

> 319 nodes

## Key Concepts

- **ChatService** (97 connections) — `server/game/chat_service.py`
- **chat_service.py** (61 connections) — `server/game/chat_service.py`
- **ChatMessage** (59 connections) — `server/game/chat_message.py`
- **test_chat_service.py** (44 connections) — `server/tests/unit/game/test_chat_service.py`
- **chat_channel_message_senders.py** (40 connections) — `server/game/chat_channel_message_senders.py`
- **chat_nats_publisher.py** (32 connections) — `server/game/chat_nats_publisher.py`
- **chat_message_senders.py** (30 connections) — `server/game/chat_message_senders.py`
- **publish_chat_message_to_nats()** (29 connections) — `server/game/chat_nats_publisher.py`
- **UUID** (28 connections)
- **test_chat_message_senders.py** (28 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **asyncio** (22 connections)
- **ChatSendServices** (20 connections) — `server/game/chat_channel_message_senders.py`
- **chat_message.py** (19 connections) — `server/game/chat_message.py`
- **send_local_message()** (18 connections) — `server/game/chat_message_senders.py`
- **send_whisper_message()** (17 connections) — `server/game/chat_channel_message_senders.py`
- **send_predefined_emote()** (17 connections) — `server/game/chat_message_senders.py`
- **send_system_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **chat_pose_helpers.py** (15 connections) — `server/game/chat_pose_helpers.py`
- **send_global_message()** (14 connections) — `server/game/chat_channel_message_senders.py`
- **create_and_log_chat_message()** (14 connections) — `server/game/chat_message_helpers.py`
- **send_party_message()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **_attr()** (13 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **chat_message_helpers.py** (13 connections) — `server/game/chat_message_helpers.py`
- *... and 294 more nodes in this community*

## Relationships

- [Test Chat Npc System](Test_Chat_Npc_System.md) (23 shared connections)
- [Test Chat Nats Publisher](Test_Chat_Nats_Publisher.md) (23 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (21 shared connections)
- [Test Chat Pose Helpers](Test_Chat_Pose_Helpers.md) (13 shared connections)
- [Test Chat Validator](Test_Chat_Validator.md) (10 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (5 shared connections)
- [Chat Logger](Chat_Logger.md) (5 shared connections)
- [Test Magic Commands](Test_Magic_Commands.md) (4 shared connections)
- [Chat Moderation](Chat_Moderation.md) (4 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (3 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (3 shared connections)
- [NATS Messaging Config](NATS_Messaging_Config.md) (3 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message.py`
- `server/game/chat_message_helpers.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_helpers.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `server/tests/unit/game/test_chat_service.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 763 (92%)
- INFERRED: 68 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*