# player persistence repository

> 11 nodes

## Key Concepts

- **ChatModeration** (27 connections) — `server/game/chat_moderation.py`
- **.is_channel_muted()** (4 connections) — `server/game/chat_moderation.py`
- **.is_player_muted()** (4 connections) — `server/game/chat_moderation.py`
- **.__init__()** (2 connections) — `server/game/chat_moderation.py`
- **.can_send_message()** (2 connections) — `server/game/chat_moderation.py`
- **moderation()** (2 connections) — `server/tests/unit/game/test_chat_moderation.py`
- **Handles chat moderation operations.** (1 connections) — `server/game/chat_moderation.py`
- **Initialize moderation handler.          Args:             player_service: Player** (1 connections) — `server/game/chat_moderation.py`
- **Check if a channel is muted for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if a player is muted by another player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if a player can send a message.** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [chat moderation game](chat_moderation_game.md) (13 shared connections)
- [startup services npc](startup_services_npc.md) (3 shared connections)
- [tsconfig app src/**/*](tsconfig_app_src-__-_.md) (3 shared connections)
- [lucidity commands services](lucidity_commands_services.md) (2 shared connections)
- [chat service game](chat_service_game.md) (2 shared connections)
- [eventLog eventStore projector](eventLog_eventStore_projector.md) (2 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`
- `server/tests/unit/game/test_chat_moderation.py`

## Audit Trail

- EXTRACTED: 45 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*