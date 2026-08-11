# Player Mute Persistence

> 59 nodes

## Key Concepts

- **UserManager** (57 connections) — `server/services/user_manager.py`
- **UUID** (39 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.is_admin()** (10 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **.add_admin()** (6 connections) — `server/services/user_manager.py`
- **.remove_admin()** (6 connections) — `server/services/user_manager.py`
- **.mute_player()** (6 connections) — `server/services/user_manager.py`
- **.unmute_player()** (6 connections) — `server/services/user_manager.py`
- **.mute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_global()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **.mute_channel()** (5 connections) — `server/services/user_manager.py`
- **.unmute_channel()** (5 connections) — `server/services/user_manager.py`
- **.is_player_muted_async()** (5 connections) — `server/services/user_manager.py`
- **.is_channel_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_globally_muted()** (5 connections) — `server/services/user_manager.py`
- **._update_cache_on_error()** (5 connections) — `server/services/user_manager.py`
- **._serialize_mute_info_for_json()** (5 connections) — `server/services/user_manager.py`
- **._save_player_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- **._save_channel_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- *... and 34 more nodes in this community*

## Relationships

- [Game Magic Spell](Game_Magic_Spell.md) (17 shared connections)
- [Async Migration Gotchas](Async_Migration_Gotchas.md) (16 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (6 shared connections)
- [Commands Time](Commands_Time.md) (4 shared connections)
- [Player Effects API](Player_Effects_API.md) (4 shared connections)
- [Player Respawn Handlers](Player_Respawn_Handlers.md) (1 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (1 shared connections)
- [Player Preferences Service](Player_Preferences_Service.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 300 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*