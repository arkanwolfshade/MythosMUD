# Room Broadcast

> 365 nodes

## Key Concepts

- **ConnectionManager** (233 connections) — `server/realtime/connection_manager.py`
- **connection_manager.py** (161 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (80 connections) — `server/realtime/connection_manager_methods.py`
- **test_connection_delegates.py** (51 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **UUID** (41 connections)
- **connection_delegates.py** (38 connections) — `server/realtime/connection_delegates.py`
- **UUID** (21 connections)
- **validate_token_impl()** (15 connections) — `server/realtime/connection_delegates.py`
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_message_broadcaster()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_connection_cleaner()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **connection_statistics.py** (11 connections) — `server/realtime/connection_statistics.py`
- **validate_player_presence_impl()** (11 connections) — `server/realtime/connection_statistics.py`
- **UUID** (10 connections)
- **delegate_health_monitor_sync()** (10 connections) — `server/realtime/connection_delegates.py`
- **get_online_player_by_display_name_impl()** (10 connections) — `server/realtime/connection_statistics.py`
- **delegate_connection_cleaner_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **get_player_presence_info_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **get_session_stats_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **_async_callable()** (8 connections) — `server/realtime/connection_delegates.py`
- *... and 340 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (30 shared connections)
- [persistence rationale room](persistence_rationale_room.md) (24 shared connections)
- [container service services](container_service_services.md) (23 shared connections)
- [game chat service](game_chat_service.md) (23 shared connections)
- [connection realtime error](connection_realtime_error.md) (22 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (20 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (18 shared connections)
- [realtime connection helpers](realtime_connection_helpers.md) (12 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (12 shared connections)
- [room look commands](room_look_commands.md) (11 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (10 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (9 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_statistics.py`
- `server/tests/unit/realtime/test_connection_delegates.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 1662 (98%)
- INFERRED: 38 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*