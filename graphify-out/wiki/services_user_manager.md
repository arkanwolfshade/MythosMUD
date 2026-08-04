# services user manager

> 57 nodes

## Key Concepts

- **UserManager** (59 connections) — `server/services/user_manager.py`
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

- [services user manager](services_user_manager.md) (16 shared connections)
- [auth invites rationale](auth_invites_rationale.md) (16 shared connections)
- [error websocket handler](error_websocket_handler.md) (4 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (3 shared connections)
- [Exception Containers](Exception_Containers.md) (3 shared connections)
- [user manager services](user_manager_services.md) (2 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 296 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*