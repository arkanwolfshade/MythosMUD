# ContainerRepository

> 125 nodes

## Key Concepts

- **chat_service.py** (40 connections) — `server/game/chat_service.py`
- **chat_channel_message_senders.py** (33 connections) — `server/game/chat_channel_message_senders.py`
- **test_chat_message_senders.py** (27 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **chat_message_senders.py** (24 connections) — `server/game/chat_message_senders.py`
- **ChatSendServices** (19 connections) — `server/game/chat_channel_message_senders.py`
- **send_whisper_message()** (16 connections) — `server/game/chat_channel_message_senders.py`
- **send_system_message()** (15 connections) — `server/game/chat_channel_message_senders.py`
- **send_predefined_emote()** (14 connections) — `server/game/chat_message_senders.py`
- **ChatLogger** (13 connections) — `server/game/chat_channel_message_senders.py`
- **ChatUserManager** (13 connections) — `server/game/chat_channel_message_senders.py`
- **_attr()** (13 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **asyncio** (13 connections)
- **ChatRateLimiter** (12 connections) — `server/game/chat_channel_message_senders.py`
- **send_local_message()** (12 connections) — `server/game/chat_message_senders.py`
- **chat_validation_helpers.py** (12 connections) — `server/game/chat_validation_helpers.py`
- **ChatPlayerService** (11 connections) — `server/game/chat_channel_message_senders.py`
- **send_global_message()** (11 connections) — `server/game/chat_channel_message_senders.py`
- **send_party_message()** (11 connections) — `server/game/chat_message_senders.py`
- **_ctx()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **_player()** (11 connections) — `server/tests/unit/game/test_chat_message_senders.py`
- **ChatResult** (10 connections)
- **ChatEmoteService** (9 connections) — `server/game/chat_channel_message_senders.py`
- **ChatPlayerView** (9 connections) — `server/game/chat_channel_message_senders.py`
- **send_party_message()** (9 connections) — `server/game/chat_channel_message_senders.py`
- **WhisperTracker** (8 connections) — `server/game/chat_channel_message_senders.py`
- *... and 100 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (15 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (14 shared connections)
- [Communities (355 total, 223 thin omitted)](Communities_355_total,_223_thin_omitted.md) (8 shared connections)
- [magic_service.py](magic_service.py.md) (3 shared connections)
- [container_persistence.py](container_persistence.py.md) (1 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (1 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (1 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (1 shared connections)
- [Async Facades Implementation - COMPLETE ✅](Async_Facades_Implementation_-_COMPLETE_✅.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/game/chat_channel_message_senders.py`
- `server/game/chat_message_senders.py`
- `server/game/chat_service.py`
- `server/game/chat_validation_helpers.py`
- `server/tests/unit/game/test_chat_message_senders.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 325 (94%)
- INFERRED: 19 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*