# user_manager.py

> 22 nodes

## Key Concepts

- **user_manager.py** (17 connections) — `server/services/user_manager.py`
- **._cleanup_player_mutes()** (8 connections) — `server/services/user_manager.py`
- **.get_player_mutes()** (7 connections) — `server/services/user_manager.py`
- **datetime** (7 connections)
- **._cleanup_expired_mutes()** (6 connections) — `server/services/user_manager.py`
- **._get_active_channel_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_global_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_player_mutes()** (5 connections) — `server/services/user_manager.py`
- **._cleanup_channel_mutes()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_global_mutes()** (4 connections) — `server/services/user_manager.py`
- **.get_system_stats()** (3 connections) — `server/services/user_manager.py`
- **User management service for MythosMUD chat system. This module provides…** (1 connections) — `server/services/user_manager.py`
- **Get active global mutes applied by a player.** (1 connections) — `server/services/user_manager.py`
- **Get all mutes applied by a player. Args: player_id: Player ID Returns:…** (1 connections) — `server/services/user_manager.py`
- **Get system-wide user management statistics. Returns: Dictionary with system…** (1 connections) — `server/services/user_manager.py`
- **Clean up expired player mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired channel mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired global mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired mutes from all storage.** (1 connections) — `server/services/user_manager.py`
- **Remove mute data for a player from memory and optionally delete their file.…** (1 connections) — `server/services/user_manager.py`
- **Get active player mutes for a player.** (1 connections) — `server/services/user_manager.py`
- **Get active channel mutes for a player.** (1 connections) — `server/services/user_manager.py`

## Relationships

- [UserManager](UserManager.md) (19 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)
- [follow_service.py](follow_service.py.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*