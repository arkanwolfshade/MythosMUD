# server game chat service chatservice

> 142 nodes

## Key Concepts

- **ChatService** (96 connections) — `server/game/chat_service.py`
- **test_chat_service.py** (44 connections) — `server/tests/unit/game/test_chat_service.py`
- **asyncio** (22 connections)
- **._chat_send_services()** (5 connections) — `server/game/chat_service.py`
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
- **test_send_say_message_cannot_send()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_say_message_empty()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_say_message_globally_muted()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_say_message_muted()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_say_message_no_room()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- *... and 117 more nodes in this community*

## Relationships

- [server game chat channel message](server_game_chat_channel_message.md) (33 shared connections)
- [chatresult](chatresult.md) (12 shared connections)
- [server container bundles chat chatbundle](server_container_bundles_chat_chatbundle.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server app lifespan protocols nats](server_app_lifespan_protocols_nats.md) (1 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (1 shared connections)
- [server dependencies](server_dependencies.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [server npc communication integration npccommunicationintegration](server_npc_communication_integration_npccommunicationintegration.md) (1 shared connections)
- [server game chat service chatservice](server_game_chat_service_chatservice.md) (1 shared connections)
- [server api players](server_api_players.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 230 (86%)
- INFERRED: 36 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*