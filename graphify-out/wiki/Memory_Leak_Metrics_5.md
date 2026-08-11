# Memory Leak Metrics

> 84 nodes

## Key Concepts

- **PerformanceMonitor** (25 connections) — `server/monitoring/performance_monitor.py`
- **websocket_integration.py** (22 connections) — `docs/examples/logging/websocket_integration.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (20 connections) — `server/monitoring/performance_monitor.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **handle_websocket_message()** (8 connections) — `docs/examples/logging/websocket_integration.py`
- **.record_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket_endpoint()** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_text()** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **get_performance_stats()** (7 connections) — `server/monitoring/performance_monitor.py`
- **.disconnect()** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **handle_game_action()** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **chat_service** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **Any** (6 connections)
- **.get_operation_stats()** (6 connections) — `server/monitoring/performance_monitor.py`
- **record_performance_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **.connect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **handle_chat_message()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **.get_all_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- **reset_performance_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- *... and 59 more nodes in this community*

## Relationships

- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (8 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (7 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (6 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (5 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (5 shared connections)
- [Test Migration Mapping](Test_Migration_Mapping.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (2 shared connections)
- [test_process_exits_for_room_no_direction](test_process_exits_for_room_no_direction.md) (1 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (1 shared connections)

## Source Files

- `docs/examples/logging/websocket_integration.py`
- `server/monitoring/performance_monitor.py`

## Audit Trail

- EXTRACTED: 311 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*