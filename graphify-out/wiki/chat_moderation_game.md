# chat moderation game

> 24 nodes

## Key Concepts

- **normalize_player_id()** (18 connections) — `server/game/chat_moderation.py`
- **UUID** (17 connections)
- **.get_player_by_id()** (12 connections) — `server/game/chat_moderation.py`
- **.resolve_player_name()** (7 connections) — `server/game/chat_moderation.py`
- **.mute_player()** (6 connections) — `server/game/chat_moderation.py`
- **.unmute_player()** (6 connections) — `server/game/chat_moderation.py`
- **.mute_global()** (6 connections) — `server/game/chat_moderation.py`
- **.unmute_global()** (6 connections) — `server/game/chat_moderation.py`
- **.mute_channel()** (5 connections) — `server/game/chat_moderation.py`
- **.unmute_channel()** (5 connections) — `server/game/chat_moderation.py`
- **.add_admin()** (5 connections) — `server/game/chat_moderation.py`
- **.remove_admin()** (5 connections) — `server/game/chat_moderation.py`
- **.is_globally_muted()** (4 connections) — `server/game/chat_moderation.py`
- **Resolve player name to player object.** (1 connections) — `server/game/chat_moderation.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a specific channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a specific channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a specific player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a specific player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Apply a global mute to a player (cannot use any chat channels).** (1 connections) — `server/game/chat_moderation.py`
- **Remove a global mute from a player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if a player is globally muted.** (1 connections) — `server/game/chat_moderation.py`
- **Add a player as an admin.** (1 connections) — `server/game/chat_moderation.py`
- **Remove a player's admin status.** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [dialogue schemas tree](dialogue_schemas_tree.md) (13 shared connections)
- [services ascii map](services_ascii_map.md) (10 shared connections)
- [command parser build](command_parser_build.md) (2 shared connections)
- [eventLog eventStore projector](eventLog_eventStore_projector.md) (2 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 113 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*