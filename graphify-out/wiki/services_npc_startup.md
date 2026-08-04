# services npc startup

> 72 nodes

## Key Concepts

- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **PersonalMessageSender** (21 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **personal_message_sender.py** (15 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_personal_message_sender.py** (14 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **Any** (8 connections)
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **.send_message()** (8 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (7 connections)
- **._prepare_payload()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **._send_to_websocket()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_send_to_websocket_accept_first_is_debug_not_warning()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- *... and 47 more nodes in this community*

## Relationships

- [connection disconnection realtime](connection_disconnection_realtime.md) (13 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (9 shared connections)
- [combat configuration service](combat_configuration_service.md) (5 shared connections)
- [Database Config](Database_Config.md) (5 shared connections)
- [services chat logger](services_chat_logger.md) (4 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [realtime errors error](realtime_errors_error.md) (3 shared connections)
- [subject admin controller](subject_admin_controller.md) (3 shared connections)
- [commands communication channels](commands_communication_channels.md) (3 shared connections)
- [nats services metrics](nats_services_metrics.md) (2 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 322 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*