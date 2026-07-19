# Services User Manager

> 12 nodes · cohesion 0.20

## Key Concepts

- **datetime** (8 connections) — `server/services/user_manager.py`
- **._cleanup_player_mutes()** (8 connections) — `server/services/user_manager.py`
- **._cleanup_expired_mutes()** (6 connections) — `server/services/user_manager.py`
- **._cleanup_channel_mutes()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_global_mutes()** (4 connections) — `server/services/user_manager.py`
- **.get_system_stats()** (3 connections) — `server/services/user_manager.py`
- **Get system-wide user management statistics.          Returns:             Dic** (1 connections) — `server/services/user_manager.py`
- **Clean up expired player mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired channel mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired global mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired mutes from all storage.** (1 connections) — `server/services/user_manager.py`
- **Remove mute data for a player from memory and optionally delete their file.** (1 connections) — `server/services/user_manager.py`

## Relationships

- [[Player Mute Persistence]] (11 shared connections)
- [[Chat Channel Logger]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 38 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
