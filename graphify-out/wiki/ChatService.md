# ChatService

> 84 nodes · cohesion 0.03

## Key Concepts

- **ChatService** (83 connections) — `server/game/chat_service.py`
- **test_chat_service.py** (39 connections) — `server/tests/unit/game/test_chat_service.py`
- **.__init__()** (4 connections) — `server/npc/communication_integration.py`
- **test_get_room_messages()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_init()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_init_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_log_message()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_echo_sent()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_message_to_dict_with_target()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_service_init()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_service_normalize_player_id()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_chat_service_normalize_player_id_string()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_clear_last_whisper_sender()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_clear_player_pose()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_get_last_whisper_sender()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_get_last_whisper_sender_none()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_get_player_pose()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_get_player_pose_none()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_get_room_messages_empty()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_emote_message_empty()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_global_message_empty()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_local_message_empty()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_party_message_empty()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- **test_send_party_message_player_not_found()** (3 connections) — `server/tests/unit/game/test_chat_service.py`
- *... and 59 more nodes in this community*

## Relationships

- [UUID](UUID.md) (26 shared connections)
- [chat_service.py](chat_service.py.md) (14 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [dependencies.py](dependencies.py.md) (2 shared connections)
- [ChatWhisperTracker](ChatWhisperTracker.md) (2 shared connections)
- [npc_base.py](npc_base.py.md) (2 shared connections)
- [test_lifespan_startup.py](test_lifespan_startup.py.md) (1 shared connections)
- [SpellRegistry](SpellRegistry.md) (1 shared connections)
- [UserManagerProtocol](UserManagerProtocol.md) (1 shared connections)
- [ChatModeration](ChatModeration.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/npc/communication_integration.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 272 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*