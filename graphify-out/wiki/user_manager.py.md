# user_manager.py

> 21 nodes

## Key Concepts

- **user_manager.py** (18 connections) — `server/services/user_manager.py`
- **message_filtering.py** (11 connections) — `server/realtime/message_filtering.py`
- **._cleanup_player_mutes()** (8 connections) — `server/services/user_manager.py`
- **datetime** (7 connections)
- **._cleanup_expired_mutes()** (6 connections) — `server/services/user_manager.py`
- **_get_proper_data_dir()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_channel_mutes()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_global_mutes()** (4 connections) — `server/services/user_manager.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **.get_system_stats()** (3 connections) — `server/services/user_manager.py`
- **Path** (3 connections)
- **Message filtering utilities for NATS message handler. This module handles room…** (1 connections) — `server/realtime/message_filtering.py`
- **User management service for MythosMUD chat system. This module provides…** (1 connections) — `server/services/user_manager.py`
- **Get system-wide user management statistics. Returns: Dictionary with system…** (1 connections) — `server/services/user_manager.py`
- **Clean up expired player mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired channel mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired global mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired mutes from all storage.** (1 connections) — `server/services/user_manager.py`
- **Remove mute data for a player from memory and optionally delete their file.…** (1 connections) — `server/services/user_manager.py`
- **Get the proper environment-aware data directory for user management. Uses…** (1 connections) — `server/services/user_manager.py`
- **Initialize the user manager. Args: data_dir: Directory for player-specific mute…** (1 connections) — `server/services/user_manager.py`

## Relationships

- [UserManager](UserManager.md) (16 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (2 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 59 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*