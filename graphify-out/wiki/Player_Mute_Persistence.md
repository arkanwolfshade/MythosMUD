# Player Mute Persistence

> 83 nodes

## Key Concepts

- **UserManager** (57 connections) — `server/services/user_manager.py`
- **UUID** (39 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **._cleanup_player_mutes()** (8 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **datetime** (7 connections)
- **.get_player_mutes()** (7 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **.add_admin()** (6 connections) — `server/services/user_manager.py`
- **.remove_admin()** (6 connections) — `server/services/user_manager.py`
- **.mute_player()** (6 connections) — `server/services/user_manager.py`
- **.unmute_player()** (6 connections) — `server/services/user_manager.py`
- **.mute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_global()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **._load_player_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **._load_global_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **.mute_channel()** (5 connections) — `server/services/user_manager.py`
- **.unmute_channel()** (5 connections) — `server/services/user_manager.py`
- **.is_player_muted_async()** (5 connections) — `server/services/user_manager.py`
- *... and 58 more nodes in this community*

## Relationships

- [Async Migration Gotchas](Async_Migration_Gotchas.md) (7 shared connections)
- [Commands Time](Commands_Time.md) (5 shared connections)
- [Player Effects API](Player_Effects_API.md) (3 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (2 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (2 shared connections)
- [Player Preferences Service](Player_Preferences_Service.md) (2 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (2 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)
- [Performance Optimization Summary](Performance_Optimization_Summary.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 390 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*