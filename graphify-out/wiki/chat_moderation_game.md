# chat moderation game

> 82 nodes

## Key Concepts

- **ChatModeration** (27 connections) — `server/game/chat_moderation.py`
- **UserManagerProtocol** (21 connections) — `server/game/chat_moderation.py`
- **normalize_player_id()** (18 connections) — `server/game/chat_moderation.py`
- **UUID** (17 connections)
- **.get_player_by_id()** (12 connections) — `server/game/chat_moderation.py`
- **chat_moderation.py** (11 connections) — `server/game/chat_moderation.py`
- **Any** (8 connections)
- **.get_mute_status()** (8 connections) — `server/game/chat_moderation.py`
- **.resolve_player_name()** (7 connections) — `server/game/chat_moderation.py`
- **.mute_player()** (6 connections) — `server/game/chat_moderation.py`
- **.unmute_player()** (6 connections) — `server/game/chat_moderation.py`
- **.mute_global()** (6 connections) — `server/game/chat_moderation.py`
- **.unmute_global()** (6 connections) — `server/game/chat_moderation.py`
- **.get_player_mutes()** (6 connections) — `server/game/chat_moderation.py`
- **PlayerServiceProtocol** (5 connections) — `server/game/chat_moderation.py`
- **.mute_channel()** (5 connections) — `server/game/chat_moderation.py`
- **.unmute_channel()** (5 connections) — `server/game/chat_moderation.py`
- **.add_admin()** (5 connections) — `server/game/chat_moderation.py`
- **.remove_admin()** (5 connections) — `server/game/chat_moderation.py`
- **.is_admin()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_entry()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_section()** (5 connections) — `server/game/chat_moderation.py`
- **.is_channel_muted()** (4 connections) — `server/game/chat_moderation.py`
- **.is_player_muted()** (4 connections) — `server/game/chat_moderation.py`
- **.is_globally_muted()** (4 connections) — `server/game/chat_moderation.py`
- *... and 57 more nodes in this community*

## Relationships

- [eventLog eventStore projector](eventLog_eventStore_projector.md) (5 shared connections)
- [chat game message](chat_game_message.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [chat service game](chat_service_game.md) (2 shared connections)
- [game chat whisper](game_chat_whisper.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 289 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*