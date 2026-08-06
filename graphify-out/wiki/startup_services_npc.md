# startup services npc

> 9 nodes

## Key Concepts

- **Any** (8 connections)
- **._format_mute_entry()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_section()** (5 connections) — `server/game/chat_moderation.py`
- **.get_user_management_stats()** (4 connections) — `server/game/chat_moderation.py`
- **.get_system_stats()** (3 connections) — `server/game/chat_moderation.py`
- **.get_player_mutes()** (2 connections) — `server/game/chat_moderation.py`
- **Get user management system statistics.** (1 connections) — `server/game/chat_moderation.py`
- **Format a single mute entry for display.** (1 connections) — `server/game/chat_moderation.py`
- **Format a section of mutes (personal or global) for display.** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [player persistence repository](player_persistence_repository.md) (3 shared connections)
- [chat moderation game](chat_moderation_game.md) (2 shared connections)
- [tsconfig app src/**/*](tsconfig_app_src-__-_.md) (2 shared connections)
- [combat services service](combat_services_service.md) (2 shared connections)
- [lucidity commands services](lucidity_commands_services.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 30 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*