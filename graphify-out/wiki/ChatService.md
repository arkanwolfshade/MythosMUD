# ChatService

> 145 nodes

## Key Concepts

- **ChatService** (97 connections) — `server/game/chat_service.py`
- **test_chat_service.py** (44 connections) — `server/tests/unit/game/test_chat_service.py`
- **UUID** (28 connections)
- **asyncio** (22 connections)
- **.send_say_message()** (11 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (10 connections) — `server/game/chat_service.py`
- **_publish_room_chat()** (6 connections) — `server/game/chat_service.py`
- **._chat_send_services()** (5 connections) — `server/game/chat_service.py`
- **._normalize_player_id()** (5 connections) — `server/game/chat_service.py`
- **.send_global_message()** (4 connections) — `server/game/chat_service.py`
- **.send_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_whisper_message()** (4 connections) — `server/game/chat_service.py`
- **test_get_last_whisper_sender()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_get_last_whisper_sender_none()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_get_room_messages()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_emote_message_empty()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_emote_message_success()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_global_message_empty()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_global_message_success()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_local_message_empty()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_local_message_success()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_party_message_empty()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_party_message_player_not_found()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_party_message_rate_limited()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_party_message_success()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- *... and 120 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (15 shared connections)
- [ChatMessage](ChatMessage.md) (15 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (3 shared connections)
- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [SpellLearningService](SpellLearningService.md) (1 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 245 (87%)
- INFERRED: 38 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*