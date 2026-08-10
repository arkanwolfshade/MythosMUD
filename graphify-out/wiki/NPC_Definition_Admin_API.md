# NPC Definition Admin API

> 68 nodes

## Key Concepts

- **ChatService** (83 connections) — `server/game/chat_service.py`
- **UUID** (26 connections)
- **Any** (14 connections)
- **.initialize()** (5 connections) — `server/container/bundles/chat.py`
- **._normalize_player_id()** (5 connections) — `server/game/chat_service.py`
- **.send_local_message()** (4 connections) — `server/game/chat_service.py`
- **.send_global_message()** (4 connections) — `server/game/chat_service.py`
- **.send_party_message()** (4 connections) — `server/game/chat_service.py`
- **.send_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_whisper_message()** (4 connections) — `server/game/chat_service.py`
- **.set_player_pose()** (4 connections) — `server/game/chat_service.py`
- **.send_predefined_emote()** (4 connections) — `server/game/chat_service.py`
- **.get_player_mutes()** (4 connections) — `server/game/chat_service.py`
- **.get_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.clear_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.mute_channel()** (3 connections) — `server/game/chat_service.py`
- **.unmute_channel()** (3 connections) — `server/game/chat_service.py`
- **.is_channel_muted()** (3 connections) — `server/game/chat_service.py`
- **.mute_player()** (3 connections) — `server/game/chat_service.py`
- **.unmute_player()** (3 connections) — `server/game/chat_service.py`
- **.is_player_muted()** (3 connections) — `server/game/chat_service.py`
- **.mute_global()** (3 connections) — `server/game/chat_service.py`
- **.unmute_global()** (3 connections) — `server/game/chat_service.py`
- **.is_globally_muted()** (3 connections) — `server/game/chat_service.py`
- **.add_admin()** (3 connections) — `server/game/chat_service.py`
- *... and 43 more nodes in this community*

## Relationships

- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (29 shared connections)
- [Chat Message Helpers](Chat_Message_Helpers.md) (11 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (1 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/game/chat_service.py`

## Audit Trail

- EXTRACTED: 249 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*