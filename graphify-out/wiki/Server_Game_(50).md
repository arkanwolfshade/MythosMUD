# Server Game (50)

> 7 nodes

## Key Concepts

- **.get_mute_status()** (8 connections) — `server/game/chat_moderation.py`
- **.get_player_mutes()** (6 connections) — `server/game/chat_moderation.py`
- **.is_admin()** (5 connections) — `server/game/chat_moderation.py`
- **.load_player_mutes()** (2 connections) — `server/game/chat_moderation.py`
- **Check if a player is an admin.** (1 connections) — `server/game/chat_moderation.py`
- **Get all mutes applied by a player.** (1 connections) — `server/game/chat_moderation.py`
- **Get comprehensive mute status for a player.          Args:             player_id** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [Server Game (29)](Server_Game_%2829%29.md) (6 shared connections)
- [Server Game (41)](Server_Game_%2841%29.md) (3 shared connections)
- [Server Game (48)](Server_Game_%2848%29.md) (2 shared connections)
- [Server Game (30)](Server_Game_%2830%29.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*