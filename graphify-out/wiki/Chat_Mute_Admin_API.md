# Chat Mute Admin API

> 128 nodes

## Key Concepts

- **ChatService** (83 connections) — `server/game/chat_service.py`
- **test_chat_service.py** (39 connections) — `server/tests/unit/game/test_chat_service.py`
- **UUID** (26 connections)
- **Any** (14 connections)
- **.send_say_message()** (4 connections) — `server/game/chat_service.py`
- **.send_local_message()** (4 connections) — `server/game/chat_service.py`
- **.send_global_message()** (4 connections) — `server/game/chat_service.py`
- **.send_party_message()** (4 connections) — `server/game/chat_service.py`
- **.send_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_whisper_message()** (4 connections) — `server/game/chat_service.py`
- **.send_emote_message()** (4 connections) — `server/game/chat_service.py`
- **.set_player_pose()** (4 connections) — `server/game/chat_service.py`
- **.send_predefined_emote()** (4 connections) — `server/game/chat_service.py`
- **.get_player_mutes()** (4 connections) — `server/game/chat_service.py`
- **test_get_room_messages()** (4 connections) — `server/tests/unit/game/test_chat_service.py`
- **._normalize_player_id()** (3 connections) — `server/game/chat_service.py`
- **.get_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.clear_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.mute_channel()** (3 connections) — `server/game/chat_service.py`
- **.unmute_channel()** (3 connections) — `server/game/chat_service.py`
- **.is_channel_muted()** (3 connections) — `server/game/chat_service.py`
- **.mute_player()** (3 connections) — `server/game/chat_service.py`
- **.unmute_player()** (3 connections) — `server/game/chat_service.py`
- **.is_player_muted()** (3 connections) — `server/game/chat_service.py`
- **.mute_global()** (3 connections) — `server/game/chat_service.py`
- *... and 103 more nodes in this community*

## Relationships

- [Who Command Tests](Who_Command_Tests.md) (13 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (4 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (1 shared connections)
- [Chat Moderation Service](Chat_Moderation_Service.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Feature Implementation Phases](Feature_Implementation_Phases.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_service.py`

## Audit Trail

- EXTRACTED: 405 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*