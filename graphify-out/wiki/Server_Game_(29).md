# Server Game (29)

> 21 nodes

## Key Concepts

- **UUID** (17 connections)
- **normalize_player_id()** (16 connections) — `server/game/chat_moderation.py`
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
- **Mute a specific player for another player.** (2 connections) — `server/game/chat_moderation.py`
- **Resolve player name to player object.** (1 connections) — `server/game/chat_moderation.py`
- **Normalize player identifiers to string form.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a specific channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a specific channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Apply a global mute to a player (cannot use any chat channels).** (1 connections) — `server/game/chat_moderation.py`
- **Remove a global mute from a player.** (1 connections) — `server/game/chat_moderation.py`
- **Add a player as an admin.** (1 connections) — `server/game/chat_moderation.py`
- **Remove a player's admin status.** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [Server Game (41)](Server_Game_%2841%29.md) (14 shared connections)
- [Server Game (50)](Server_Game_%2850%29.md) (6 shared connections)
- [Server Game (49)](Server_Game_%2849%29.md) (4 shared connections)
- [Server Game (48)](Server_Game_%2848%29.md) (2 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 106 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*