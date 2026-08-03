# services user manager

> 71 nodes

## Key Concepts

- **UserManager** (59 connections) — `server/services/user_manager.py`
- **UUID** (39 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **.is_admin_sync()** (7 connections) — `server/services/user_manager.py`
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
- **.is_channel_muted()** (5 connections) — `server/services/user_manager.py`
- **.is_globally_muted()** (5 connections) — `server/services/user_manager.py`
- **._convert_mute_info_timestamps()** (5 connections) — `server/services/user_manager.py`
- *... and 46 more nodes in this community*

## Relationships

- [services user manager](services_user_manager.md) (17 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (7 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [alias storage commands](alias_storage_commands.md) (3 shared connections)
- [holiday service services](holiday_service_services.md) (2 shared connections)
- [user manager services](user_manager_services.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)
- [chat services logger](chat_services_logger.md) (1 shared connections)
- [chat logger services](chat_logger_services.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 349 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*