# tsconfig app src/**/*

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

- [chat moderation game](chat_moderation_game.md) (6 shared connections)
- [player persistence repository](player_persistence_repository.md) (3 shared connections)
- [startup services npc](startup_services_npc.md) (2 shared connections)
- [combat services service](combat_services_service.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*