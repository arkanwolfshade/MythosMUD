# UserManager

> 63 nodes

## Key Concepts

- **UserManager** (57 connections) — `server/services/user_manager.py`
- **UUID** (37 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **.is_admin()** (9 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **.mute_global()** (6 connections) — `server/services/user_manager.py`
- **.mute_player()** (6 connections) — `server/services/user_manager.py`
- **.unmute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_player()** (6 connections) — `server/services/user_manager.py`
- **.add_admin()** (5 connections) — `server/services/user_manager.py`
- **._is_cache_valid()** (5 connections) — `server/services/user_manager.py`
- **.is_channel_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_globally_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_player_muted_async()** (5 connections) — `server/services/user_manager.py`
- **.mute_channel()** (5 connections) — `server/services/user_manager.py`
- **.remove_admin()** (5 connections) — `server/services/user_manager.py`
- **._save_channel_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- **._save_global_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- *... and 38 more nodes in this community*

## Relationships

- [._cleanup_player_mutes](_cleanup_player_mutes.md) (17 shared connections)
- [._load_player_mutes_from_data](_load_player_mutes_from_data.md) (10 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [ContainerService](ContainerService.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [user_manager](user_manager.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (1 shared connections)
- [chat_logger](chat_logger.md) (1 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 319 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*