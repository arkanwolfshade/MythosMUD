# services user manager

> 98 nodes

## Key Concepts

- **UserManager** (59 connections) — `server/services/user_manager.py`
- **UUID** (39 connections)
- **._normalize_to_uuid()** (26 connections) — `server/services/user_manager.py`
- **.save_player_mutes()** (14 connections) — `server/services/user_manager.py`
- **.load_player_mutes()** (12 connections) — `server/services/user_manager.py`
- **.is_admin()** (8 connections) — `server/services/user_manager.py`
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
- **._cleanup_expired_mutes()** (6 connections) — `server/services/user_manager.py`
- **._load_player_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **._load_global_mutes_from_data()** (6 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **.mute_channel()** (5 connections) — `server/services/user_manager.py`
- *... and 73 more nodes in this community*

## Relationships

- [follow game service](follow_game_service.md) (8 shared connections)
- [player event handlers](player_event_handlers.md) (3 shared connections)
- [realtime player connection](realtime_player_connection.md) (3 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [party service game](party_service_game.md) (2 shared connections)
- [user manager services](user_manager_services.md) (2 shared connections)
- [task registry app](task_registry_app.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [chat services logger](chat_services_logger.md) (1 shared connections)
- [game chat whisper](game_chat_whisper.md) (1 shared connections)
- [tools generate invite](tools_generate_invite.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 431 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*