# Command Factory Creators

> 79 nodes · cohesion 0.03

## Key Concepts

- **ChatService** (87 connections) — `server/game/chat_service.py`
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
- *... and 54 more nodes in this community*

## Relationships

- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (27 shared connections)
- [Chat Message Helpers](Chat_Message_Helpers.md) (14 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (3 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (2 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)
- [Lifespan Startup Hooks](Lifespan_Startup_Hooks.md) (1 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (1 shared connections)
- [Combat Command Helpers](Combat_Command_Helpers.md) (1 shared connections)
- [Chat Moderation Service](Chat_Moderation_Service.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/npc/communication_integration.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 271 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*