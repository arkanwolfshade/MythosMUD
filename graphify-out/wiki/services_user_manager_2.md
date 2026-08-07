# services user manager

> 59 nodes

## Key Concepts

- **UserManager** (59 connections) — `server/services/user_manager.py`
- **UUID** (39 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.is_admin()** (8 connections) — `server/services/user_manager.py`
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

- [realtime monitoring performance](realtime_monitoring_performance.md) (17 shared connections)
- [room persistence loader](room_persistence_loader.md) (16 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (6 shared connections)
- [nats services service](nats_services_service.md) (4 shared connections)
- [services rescue service](services_rescue_service.md) (4 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [party service game](party_service_game.md) (2 shared connections)
- [add used user](add_used_user.md) (2 shared connections)
- [chat services logger](chat_services_logger.md) (1 shared connections)
- [user manager services](user_manager_services.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 302 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*