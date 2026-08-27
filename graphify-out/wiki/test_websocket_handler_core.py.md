# test_websocket_handler_core.py

> 153 nodes

## Key Concepts

- **ChatService** (92 connections) — `server/game/chat_service.py`
- **test_chat_service.py** (44 connections) — `server/tests/unit/game/test_chat_service.py`
- **UUID** (28 connections)
- **asyncio** (22 connections)
- **.send_say_message()** (7 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (6 connections) — `server/game/chat_service.py`
- **._chat_send_services()** (5 connections) — `server/game/chat_service.py`
- **._normalize_player_id()** (5 connections) — `server/game/chat_service.py`
- **.send_global_message()** (4 connections) — `server/game/chat_service.py`
- **.send_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_whisper_message()** (4 connections) — `server/game/chat_service.py`
- **_publish_room_chat()** (4 connections) — `server/game/chat_service.py`
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
- *... and 128 more nodes in this community*

## Relationships

- [ContainerRepository](ContainerRepository.md) (14 shared connections)
- [Communities (355 total, 223 thin omitted)](Communities_355_total,_223_thin_omitted.md) (11 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (3 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [service.py](service.py.md) (1 shared connections)
- [npc_schedules.schema.json](npc_schedules.schema.json.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 248 (89%)
- INFERRED: 32 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*