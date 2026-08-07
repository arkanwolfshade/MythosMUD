# combat services service

> 24 nodes

## Key Concepts

- **UserManagerProtocol** (21 connections) — `server/game/chat_moderation.py`
- **.mute_channel()** (2 connections) — `server/game/chat_moderation.py`
- **.unmute_channel()** (2 connections) — `server/game/chat_moderation.py`
- **.is_channel_muted()** (2 connections) — `server/game/chat_moderation.py`
- **.mute_player()** (2 connections) — `server/game/chat_moderation.py`
- **.unmute_player()** (2 connections) — `server/game/chat_moderation.py`
- **.is_player_muted()** (2 connections) — `server/game/chat_moderation.py`
- **.is_globally_muted()** (2 connections) — `server/game/chat_moderation.py`
- **.is_admin()** (2 connections) — `server/game/chat_moderation.py`
- **.can_send_message()** (2 connections) — `server/game/chat_moderation.py`
- **.mute_global()** (1 connections) — `server/game/chat_moderation.py`
- **.unmute_global()** (1 connections) — `server/game/chat_moderation.py`
- **.add_admin()** (1 connections) — `server/game/chat_moderation.py`
- **.remove_admin()** (1 connections) — `server/game/chat_moderation.py`
- **Protocol for user manager.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if channel is muted.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player is muted.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player is globally muted.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player is admin.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player can send message.** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [lucidity commands services](lucidity_commands_services.md) (2 shared connections)
- [startup services npc](startup_services_npc.md) (2 shared connections)
- [tsconfig app src/**/*](tsconfig_app_src-__-_.md) (1 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)
- [chat service game](chat_service_game.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 52 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*