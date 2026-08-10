# Player Mute Persistence

> 57 nodes

## Key Concepts

- **UserManager** (57 connections) — `server/services/user_manager.py`
- **UUID** (39 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
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
- **._save_global_mutes_to_data()** (5 connections) — `server/services/user_manager.py`
- *... and 32 more nodes in this community*

## Relationships

- [Async Migration Gotchas](Async_Migration_Gotchas.md) (16 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (16 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Commands Time](Commands_Time.md) (4 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (3 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (2 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (2 shared connections)
- [Player Preferences Service](Player_Preferences_Service.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 294 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*