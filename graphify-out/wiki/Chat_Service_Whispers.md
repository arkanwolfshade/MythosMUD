# Chat Service Whispers

> 80 nodes · cohesion 0.04

## Key Concepts

- **ChatService** (88 connections) — `server/game/chat_service.py`
- **test_chat_service.py** (37 connections) — `server/tests/unit/game/test_chat_service.py`
- **.initialize()** (5 connections) — `server/container/bundles/chat.py`
- **Test send_say_message() when player is not found.** (5 connections) — `server/tests/unit/game/test_chat_service.py`
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
- *... and 55 more nodes in this community*

## Relationships

- [[Chat Mute Admin API]] (26 shared connections)
- [[Chat Message Helpers]] (12 shared connections)
- [[Magic Service Bundle]] (6 shared connections)
- [[Application DI Bundles]] (4 shared connections)
- [[Magic Command Handlers]] (4 shared connections)
- [[Lifespan Startup Hooks]] (2 shared connections)
- [[Game Chat Whisper]] (2 shared connections)
- [[Database Manager Tests]] (1 shared connections)
- [[Combat Service Bundle]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Game Chat Moderation]] (1 shared connections)
- [[Chat Moderation Service]] (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 270 (93%)
- INFERRED: 19 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
