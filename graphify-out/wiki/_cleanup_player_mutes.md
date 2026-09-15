# ._cleanup_player_mutes

> 25 nodes

## Key Concepts

- **._cleanup_player_mutes()** (8 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.get_player_mutes()** (7 connections) — `server/services/user_manager.py`
- **datetime** (7 connections)
- **._cleanup_expired_mutes()** (6 connections) — `server/services/user_manager.py`
- **._get_active_channel_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_global_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_player_mutes()** (5 connections) — `server/services/user_manager.py`
- **.__init__()** (5 connections) — `server/services/user_manager.py`
- **._cleanup_channel_mutes()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_global_mutes()** (4 connections) — `server/services/user_manager.py`
- **.get_system_stats()** (3 connections) — `server/services/user_manager.py`
- **Path** (2 connections)
- **Get active global mutes applied by a player.** (1 connections) — `server/services/user_manager.py`
- **Get all mutes applied by a player. Args: player_id: Player ID Returns:…** (1 connections) — `server/services/user_manager.py`
- **Get system-wide user management statistics. Returns: Dictionary with system…** (1 connections) — `server/services/user_manager.py`
- **Clean up expired player mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired channel mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired global mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired mutes from all storage.** (1 connections) — `server/services/user_manager.py`
- **Get the mute data file path for a specific player.** (1 connections) — `server/services/user_manager.py`
- **Remove mute data for a player from memory and optionally delete their file.…** (1 connections) — `server/services/user_manager.py`
- **Initialize the user manager. Args: data_dir: Directory for player-specific mute…** (1 connections) — `server/services/user_manager.py`
- **Get active player mutes for a player.** (1 connections) — `server/services/user_manager.py`
- **Get active channel mutes for a player.** (1 connections) — `server/services/user_manager.py`

## Relationships

- [UserManager](UserManager.md) (21 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*