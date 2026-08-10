# Message Broadcaster Core

> 221 nodes

## Key Concepts

- **connection_initialization.py** (23 connections) — `server/realtime/connection_initialization.py`
- **HealthMonitor** (23 connections) — `server/realtime/monitoring/health_monitor.py`
- **MessageBroadcaster** (20 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.__init__()** (17 connections) — `server/realtime/connection_manager.py`
- **PerformanceTracker** (17 connections) — `server/realtime/monitoring/performance_tracker.py`
- **test_message_broadcaster.py** (17 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **message_broadcaster.py** (16 connections) — `server/realtime/messaging/message_broadcaster.py`
- **test_health_monitor.py** (16 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_connection_initialization.py** (14 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **ConnectionErrorHandler** (13 connections) — `server/realtime/errors/error_handler.py`
- **personal_message_sender.py** (13 connections) — `server/realtime/messaging/personal_message_sender.py`
- **health_monitor.py** (13 connections) — `server/realtime/monitoring/health_monitor.py`
- **PersonalMessageSender** (12 connections) — `server/realtime/messaging/personal_message_sender.py`
- **RoomEventHandler** (11 connections) — `server/realtime/integration/room_event_handler.py`
- **performance_tracker.py** (10 connections) — `server/realtime/monitoring/performance_tracker.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **error_handler.py** (9 connections) — `server/realtime/errors/error_handler.py`
- **UUID** (9 connections)
- **UUID** (9 connections)
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **UUID** (8 connections)
- *... and 196 more nodes in this community*

## Relationships

- [Room Occupant Events](Room_Occupant_Events.md) (18 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (16 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (14 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (8 shared connections)
- [Archive Environment Contamination](Archive_Environment_Contamination.md) (7 shared connections)
- [Connection Statistics Aggregator](Connection_Statistics_Aggregator.md) (3 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (3 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 741 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*