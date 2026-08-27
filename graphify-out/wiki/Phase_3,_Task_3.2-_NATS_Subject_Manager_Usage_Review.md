# Phase 3, Task 3.2: NATS Subject Manager Usage Review

> 37 nodes

## Key Concepts

- **ChatModeration** (24 connections) — `server/game/chat_moderation.py`
- **normalize_player_id()** (18 connections) — `server/game/chat_moderation.py`
- **UUID** (17 connections)
- **.get_player_mutes()** (5 connections) — `server/game/chat_moderation.py`
- **.add_admin()** (4 connections) — `server/game/chat_moderation.py`
- **.is_admin()** (4 connections) — `server/game/chat_moderation.py`
- **.is_channel_muted()** (4 connections) — `server/game/chat_moderation.py`
- **.is_globally_muted()** (4 connections) — `server/game/chat_moderation.py`
- **.is_player_muted()** (4 connections) — `server/game/chat_moderation.py`
- **.mute_channel()** (4 connections) — `server/game/chat_moderation.py`
- **.mute_global()** (4 connections) — `server/game/chat_moderation.py`
- **.mute_player()** (4 connections) — `server/game/chat_moderation.py`
- **.remove_admin()** (4 connections) — `server/game/chat_moderation.py`
- **.unmute_channel()** (4 connections) — `server/game/chat_moderation.py`
- **.unmute_global()** (4 connections) — `server/game/chat_moderation.py`
- **.unmute_player()** (4 connections) — `server/game/chat_moderation.py`
- **.can_send_message()** (2 connections) — `server/game/chat_moderation.py`
- **.__init__()** (2 connections) — `server/game/chat_moderation.py`
- **.is_globally_muted()** (2 connections) — `server/game/chat_moderation.py`
- **test_normalize_player_id_accepts_uuid()** (2 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **Check if player is globally muted.** (2 connections) — `server/game/chat_moderation.py`
- **Mute a specific channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a specific channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if a channel is muted for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a specific player for another player.** (1 connections) — `server/game/chat_moderation.py`
- *... and 12 more nodes in this community*

## Relationships

- [test_spell_repository.py](test_spell_repository.py.md) (8 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [test_player_repository_room.py](test_player_repository_room.py.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`
- `server/tests/unit/game/test_chat_moderation.py`

## Audit Trail

- EXTRACTED: 76 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*