# UserManager

> 71 nodes

## Key Concepts

- **UserManager** (104 connections) — `server/services/user_manager.py`
- **UUID** (26 connections)
- **._normalize_to_uuid()** (20 connections) — `server/services/user_manager.py`
- **._index_mute()** (8 connections) — `server/services/user_manager.py`
- **.mute_player()** (8 connections) — `server/services/user_manager.py`
- **._new_mute()** (8 connections) — `server/services/user_manager.py`
- **.get_player_mutes()** (7 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **.mute_global()** (7 connections) — `server/services/user_manager.py`
- **datetime** (7 connections)
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **._cleanup_expired_mutes()** (6 connections) — `server/services/user_manager.py`
- **.is_admin()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.mute_channel()** (6 connections) — `server/services/user_manager.py`
- **._get_active_channel_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_global_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_player_mutes()** (5 connections) — `server/services/user_manager.py`
- **.is_channel_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_globally_muted()** (5 connections) — `server/services/user_manager.py`
- **.add_admin()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_channel_mutes()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_global_mutes()** (4 connections) — `server/services/user_manager.py`
- **._cleanup_player_mutes()** (4 connections) — `server/services/user_manager.py`
- **.get_who_muted_player()** (4 connections) — `server/services/user_manager.py`
- *... and 46 more nodes in this community*

## Relationships

- [test_user_manager.py](test_user_manager.py.md) (51 shared connections)
- [PlayerMute](PlayerMute.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (3 shared connections)
- [FollowService](FollowService.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (1 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (1 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 157 (73%)
- INFERRED: 59 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*