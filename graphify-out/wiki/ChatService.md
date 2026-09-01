# ChatService

> 143 nodes

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
- **test_send_say_message_cannot_send()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- *... and 118 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (18 shared connections)
- [ChatMessage](ChatMessage.md) (16 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [SpellEffects](SpellEffects.md) (1 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (1 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 243 (86%)
- INFERRED: 38 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*