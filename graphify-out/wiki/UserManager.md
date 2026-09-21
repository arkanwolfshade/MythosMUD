# UserManager

> 81 nodes

## Key Concepts

- **UserManager** (65 connections) — `server/services/user_manager.py`
- **UUID** (41 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **.mute_player()** (8 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.get_player_mutes()** (7 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **._filter_players_needing_mute_load()** (6 connections) — `server/services/user_manager.py`
- **.is_admin()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **.mute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_player()** (6 connections) — `server/services/user_manager.py`
- **._get_active_channel_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_global_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_player_mutes()** (5 connections) — `server/services/user_manager.py`
- **._is_cache_valid()** (5 connections) — `server/services/user_manager.py`
- **.is_channel_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_globally_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_player_muted_async()** (5 connections) — `server/services/user_manager.py`
- *... and 56 more nodes in this community*

## Relationships

- [._cleanup_player_mutes](_cleanup_player_mutes.md) (11 shared connections)
- [._load_player_mutes_from_data](_load_player_mutes_from_data.md) (8 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (2 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (1 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (1 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [follow_service.py](follow_service.py.md) (1 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (1 shared connections)
- [FollowService](FollowService.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 208 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*