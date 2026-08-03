# realtime monitoring statistics

> 81 nodes

## Key Concepts

- **HealthMonitor** (22 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **PersonalMessageSender** (11 connections) — `server/realtime/messaging/personal_message_sender.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **UUID** (9 connections)
- **Any** (8 connections)
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **.send_message()** (8 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **UUID** (7 connections)
- **._prepare_payload()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **._send_to_websocket()** (5 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- *... and 56 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (23 shared connections)
- [Room Broadcast](Room_Broadcast.md) (8 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (3 shared connections)
- [health monitor realtime](health_monitor_realtime.md) (3 shared connections)
- [realtime messaging message](realtime_messaging_message.md) (2 shared connections)
- [npc populate databases](npc_populate_databases.md) (2 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)
- [realtime errors error](realtime_errors_error.md) (1 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)
- [services combat sync](services_combat_sync.md) (1 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 297 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*