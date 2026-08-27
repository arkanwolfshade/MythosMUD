# test_spell_repository.py

> 20 nodes

## Key Concepts

- **Any** (8 connections)
- **PlayerServiceProtocol** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_entry()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_section()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_duration()** (4 connections) — `server/game/chat_moderation.py`
- **.get_mute_status()** (4 connections) — `server/game/chat_moderation.py`
- **.get_user_management_stats()** (3 connections) — `server/game/chat_moderation.py`
- **.get_player_by_id()** (3 connections) — `server/game/chat_moderation.py`
- **.resolve_player_name()** (3 connections) — `server/game/chat_moderation.py`
- **.get_player_mutes()** (2 connections) — `server/game/chat_moderation.py`
- **.get_system_stats()** (2 connections) — `server/game/chat_moderation.py`
- **datetime** (2 connections)
- **Protocol** (2 connections)
- **Protocol for player service.** (1 connections) — `server/game/chat_moderation.py`
- **Resolve player name to player object.** (1 connections) — `server/game/chat_moderation.py`
- **Get user management system statistics.** (1 connections) — `server/game/chat_moderation.py`
- **Format mute duration text with remaining time or expiration status.** (1 connections) — `server/game/chat_moderation.py`
- **Format a single mute entry for display.** (1 connections) — `server/game/chat_moderation.py`
- **Format a section of mutes (personal or global) for display.** (1 connections) — `server/game/chat_moderation.py`
- **Get comprehensive mute status for a player. Args: player_id: Player ID to get…** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [Phase 3, Task 3.2: NATS Subject Manager Usage Review](Phase_3,_Task_3.2-_NATS_Subject_Manager_Usage_Review.md) (8 shared connections)
- [test_player_repository_room.py](test_player_repository_room.py.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*