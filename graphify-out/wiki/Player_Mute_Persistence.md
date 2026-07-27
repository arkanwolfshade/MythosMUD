# Player Mute Persistence

> 79 nodes · cohesion 0.06

## Key Concepts

- **UserManager** (73 connections) — `server/services/user_manager.py`
- **UUID** (40 connections) — `server/services/user_manager.py`
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **._get_player_mute_file()** (7 connections) — `server/services/user_manager.py`
- **.get_player_mutes()** (7 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **.can_send_message()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted()** (6 connections) — `server/services/user_manager.py`
- **._load_global_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **._load_player_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **.mute_global()** (6 connections) — `server/services/user_manager.py`
- **.mute_player()** (6 connections) — `server/services/user_manager.py`
- **.unmute_global()** (6 connections) — `server/services/user_manager.py`
- **.unmute_player()** (6 connections) — `server/services/user_manager.py`
- **._convert_mute_info_timestamps()** (5 connections) — `server/services/user_manager.py`
- **._convert_mute_info_uuids()** (5 connections) — `server/services/user_manager.py`
- **._get_active_channel_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_global_mutes()** (5 connections) — `server/services/user_manager.py`
- **._get_active_player_mutes()** (5 connections) — `server/services/user_manager.py`
- **._is_cache_valid()** (5 connections) — `server/services/user_manager.py`
- **.is_channel_muted()** (5 connections) — `server/services/user_manager.py`
- *... and 54 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (14 shared connections)
- [[Services User Manager]] (13 shared connections)
- [[Game Service Bundle]] (7 shared connections)
- [[NPC Admin API]] (4 shared connections)
- [[Chat Channel Logger]] (2 shared connections)
- [[User Manager Mute Tests]] (2 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 376 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
