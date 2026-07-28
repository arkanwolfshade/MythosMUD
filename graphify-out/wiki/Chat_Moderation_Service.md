# Chat Moderation Service

> 55 nodes · cohesion 0.07

## Key Concepts

- **ChatModeration** (25 connections) — `server/game/chat_moderation.py`
- **UUID** (17 connections)
- **normalize_player_id()** (16 connections) — `server/game/chat_moderation.py`
- **.get_player_by_id()** (12 connections) — `server/game/chat_moderation.py`
- **chat_moderation.py** (10 connections) — `server/game/chat_moderation.py`
- **.get_mute_status()** (8 connections) — `server/game/chat_moderation.py`
- **Any** (8 connections)
- **.resolve_player_name()** (7 connections) — `server/game/chat_moderation.py`
- **.get_player_mutes()** (6 connections) — `server/game/chat_moderation.py`
- **.mute_global()** (6 connections) — `server/game/chat_moderation.py`
- **.mute_player()** (6 connections) — `server/game/chat_moderation.py`
- **.unmute_global()** (6 connections) — `server/game/chat_moderation.py`
- **.unmute_player()** (6 connections) — `server/game/chat_moderation.py`
- **.add_admin()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_entry()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_section()** (5 connections) — `server/game/chat_moderation.py`
- **.is_admin()** (5 connections) — `server/game/chat_moderation.py`
- **.mute_channel()** (5 connections) — `server/game/chat_moderation.py`
- **.remove_admin()** (5 connections) — `server/game/chat_moderation.py`
- **.unmute_channel()** (5 connections) — `server/game/chat_moderation.py`
- **PlayerServiceProtocol** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_duration()** (4 connections) — `server/game/chat_moderation.py`
- **.get_user_management_stats()** (4 connections) — `server/game/chat_moderation.py`
- **.is_channel_muted()** (4 connections) — `server/game/chat_moderation.py`
- **.is_globally_muted()** (4 connections) — `server/game/chat_moderation.py`
- *... and 30 more nodes in this community*

## Relationships

- [Combat Command Helpers](Combat_Command_Helpers.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Chat Message Helpers](Chat_Message_Helpers.md) (2 shared connections)
- [Command Factory Creators](Command_Factory_Creators.md) (1 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 226 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*