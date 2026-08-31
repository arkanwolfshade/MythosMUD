# UserManager

> 65 nodes

## Key Concepts

- **UserManager** (61 connections) — `server/services/user_manager.py`
- **UUID** (37 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **.is_admin()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **.mute_global()** (6 connections) — `server/services/user_manager.py`
- **.mute_player()** (6 connections) — `server/services/user_manager.py`
- **.unmute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_player()** (6 connections) — `server/services/user_manager.py`
- **._is_cache_valid()** (5 connections) — `server/services/user_manager.py`
- **.is_channel_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_globally_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_player_muted_async()** (5 connections) — `server/services/user_manager.py`
- **._load_channel_mutes_from_data()** (5 connections) — `server/services/user_manager.py`
- **.mute_channel()** (5 connections) — `server/services/user_manager.py`
- **._save_channel_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- **._save_global_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- **._save_player_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- *... and 40 more nodes in this community*

## Relationships

- [._cleanup_player_mutes](_cleanup_player_mutes.md) (17 shared connections)
- [._load_player_mutes_from_data](_load_player_mutes_from_data.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [FollowService](FollowService.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (1 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)
- [user_manager](user_manager.md) (1 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 182 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*