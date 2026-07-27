# Chat Mute Admin API

> 54 nodes · cohesion 0.04

## Key Concepts

- **UUID** (31 connections) — `server/game/chat_service.py`
- **Any** (19 connections) — `server/game/chat_service.py`
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
- *... and 29 more nodes in this community*

## Relationships

- [[Chat Service Whispers]] (26 shared connections)
- [[Chat Message Helpers]] (12 shared connections)
- [[Game Chat Whisper]] (3 shared connections)
- [[Game Chat Moderation]] (2 shared connections)
- [[Chat Moderation Service]] (2 shared connections)
- [[Game Chat Pose]] (2 shared connections)

## Source Files

- `server/game/chat_service.py`

## Audit Trail

- EXTRACTED: 157 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
