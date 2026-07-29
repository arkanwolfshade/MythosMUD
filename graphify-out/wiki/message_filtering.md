# message filtering

> 23 nodes

## Key Concepts

- **user_manager.py** (19 connections) — `server/services/user_manager.py`
- **message_filtering.py** (11 connections) — `server/realtime/message_filtering.py`
- **._cleanup_player_mutes()** (8 connections) — `server/services/user_manager.py`
- **datetime** (7 connections)
- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **._cleanup_expired_mutes()** (6 connections) — `server/services/user_manager.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_channel_mutes()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_global_mutes()** (4 connections) — `server/services/user_manager.py`
- **_get_proper_data_dir()** (4 connections) — `server/services/user_manager.py`
- **Path** (3 connections)
- **.get_system_stats()** (3 connections) — `server/services/user_manager.py`
- **Message filtering utilities for NATS message handler.  This module handles room** (1 connections) — `server/realtime/message_filtering.py`
- **User management service for MythosMUD chat system.  This module provides compr** (1 connections) — `server/services/user_manager.py`
- **Initialize the user manager.          Args:             data_dir: Directory f** (1 connections) — `server/services/user_manager.py`
- **Get system-wide user management statistics.          Returns:             Dic** (1 connections) — `server/services/user_manager.py`
- **Clean up expired player mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired channel mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired global mutes.** (1 connections) — `server/services/user_manager.py`
- **Clean up expired mutes from all storage.** (1 connections) — `server/services/user_manager.py`
- **Remove mute data for a player from memory and optionally delete their file.** (1 connections) — `server/services/user_manager.py`
- **Get the proper environment-aware data directory for user management.      Uses** (1 connections) — `server/services/user_manager.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`

## Relationships

- [UUID](UUID.md) (18 shared connections)
- [main()](main%28%29.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (5 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (2 shared connections)
- [ChatLogger](ChatLogger.md) (2 shared connections)
- [test message filtering](test_message_filtering.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [.shutdown()](shutdown%28%29.md) (1 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (1 shared connections)
- [message formatters](message_formatters.md) (1 shared connections)
- [test user manager](test_user_manager.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/services/user_manager.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 86 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*