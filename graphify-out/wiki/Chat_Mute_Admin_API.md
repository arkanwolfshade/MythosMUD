# Chat Mute Admin API

> 35 nodes · cohesion 0.04

## Key Concepts

- **UUID** (27 connections)
- **Any** (16 connections)
- **._normalize_player_id()** (5 connections) — `server/game/chat_service.py`
- **.get_player_mutes()** (4 connections) — `server/game/chat_service.py`
- **.send_global_message()** (4 connections) — `server/game/chat_service.py`
- **.send_local_message()** (4 connections) — `server/game/chat_service.py`
- **.send_party_message()** (4 connections) — `server/game/chat_service.py`
- **.send_predefined_emote()** (4 connections) — `server/game/chat_service.py`
- **.send_system_message()** (4 connections) — `server/game/chat_service.py`
- **.send_whisper_message()** (4 connections) — `server/game/chat_service.py`
- **.set_player_pose()** (4 connections) — `server/game/chat_service.py`
- **.add_admin()** (3 connections) — `server/game/chat_service.py`
- **.clear_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.get_mute_status()** (3 connections) — `server/game/chat_service.py`
- **.get_player_pose()** (3 connections) — `server/game/chat_service.py`
- **.get_room_messages()** (3 connections) — `server/game/chat_service.py`
- **.get_user_management_stats()** (3 connections) — `server/game/chat_service.py`
- **.is_admin()** (3 connections) — `server/game/chat_service.py`
- **.is_channel_muted()** (3 connections) — `server/game/chat_service.py`
- **.is_globally_muted()** (3 connections) — `server/game/chat_service.py`
- **.is_player_muted()** (3 connections) — `server/game/chat_service.py`
- **.mute_channel()** (3 connections) — `server/game/chat_service.py`
- **.mute_global()** (3 connections) — `server/game/chat_service.py`
- **.mute_player()** (3 connections) — `server/game/chat_service.py`
- **.remove_admin()** (3 connections) — `server/game/chat_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [Command Factory Creators](Command_Factory_Creators.md) (27 shared connections)
- [Chat Message Helpers](Chat_Message_Helpers.md) (7 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (1 shared connections)

## Source Files

- `server/game/chat_service.py`

## Audit Trail

- EXTRACTED: 138 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*