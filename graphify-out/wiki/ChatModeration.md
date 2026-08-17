# ChatModeration

> 34 nodes

## Key Concepts

- **ChatModeration** (27 connections) — `server/game/chat_moderation.py`
- **normalize_player_id()** (18 connections) — `server/game/chat_moderation.py`
- **UUID** (17 connections)
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
- **test_normalize_player_id_accepts_uuid()** (2 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **Mute a specific channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a specific channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if a channel is muted for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a specific player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a specific player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if a player is muted by another player.** (1 connections) — `server/game/chat_moderation.py`
- **Apply a global mute to a player (cannot use any chat channels).** (1 connections) — `server/game/chat_moderation.py`
- *... and 9 more nodes in this community*

## Relationships

- [Any](Any.md) (5 shared connections)
- [._format_mute_entry](_format_mute_entry.md) (5 shared connections)
- [test_chat_moderation.py](test_chat_moderation.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`
- `server/tests/unit/game/test_chat_moderation.py`

## Audit Trail

- EXTRACTED: 74 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*