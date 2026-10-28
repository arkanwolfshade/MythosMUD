# asyncio

> 60 nodes · cohesion 0.07

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
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **.is_admin()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **.mute_channel()** (6 connections) — `server/services/user_manager.py`
- **._get_active_channel_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_global_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_player_mutes()** (5 connections) — `server/services/user_manager.py`
- **.is_channel_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_globally_muted()** (5 connections) — `server/services/user_manager.py`
- **.add_admin()** (4 connections) — `server/services/user_manager.py`
- **.get_who_muted_player()** (4 connections) — `server/services/user_manager.py`
- **.is_player_muted_async()** (4 connections) — `server/services/user_manager.py`
- **.is_player_muted_by_others()** (4 connections) — `server/services/user_manager.py`
- **._log_mute_applied()** (4 connections) — `server/services/user_manager.py`
- **._mute_info()** (4 connections) — `server/services/user_manager.py`
- **.remove_admin()** (4 connections) — `server/services/user_manager.py`
- *... and 35 more nodes in this community*

## Relationships

- [Stats](Stats.md) (25 shared connections)
- [asyncio](asyncio.md) (16 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (10 shared connections)
- [Claims by cluster](Claims_by_cluster.md) (8 shared connections)
- [Room](Room.md) (6 shared connections)
- [test_aggression.py](test_aggression.py.md) (6 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [MythosMUD Database Placement](MythosMUD_Database_Placement.md) (2 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Berlin_-_The_Wicked_City__2026-08-11.md) (1 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (1 shared connections)
- [_CombatServiceDeps](_CombatServiceDeps.md) (1 shared connections)
- [test_party_service.py](test_party_service.py.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 144 (71%)
- INFERRED: 59 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*