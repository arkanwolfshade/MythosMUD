# Memory Leak Metrics

> 50 nodes

## Key Concepts

- **websocket_integration.py** (22 connections) — `docs/examples/logging/websocket_integration.py`
- **measure_performance()** (20 connections) — `server/monitoring/performance_monitor.py`
- **handle_websocket_message()** (8 connections) — `docs/examples/logging/websocket_integration.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket_endpoint()** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_text()** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **.disconnect()** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **handle_game_action()** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **.connect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **handle_chat_message()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_message()** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **.broadcast_message()** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **authenticate_websocket_connection()** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **WebSocketRateLimiter** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **handle_websocket_error()** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket_heartbeat()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **parse_websocket_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.broadcast_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.verify_token()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.check_rate_limit()** (2 connections) — `docs/examples/logging/websocket_integration.py`
- **validate_websocket_message()** (2 connections) — `docs/examples/logging/websocket_integration.py`
- **Exception** (2 connections)
- **WebSocketDisconnect** (2 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket_manager** (2 connections) — `docs/examples/logging/websocket_integration.py`
- *... and 25 more nodes in this community*

## Relationships

- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (6 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (5 shared connections)
- [Merge Refactoring Summary](Merge_Refactoring_Summary.md) (3 shared connections)
- [Test Migration Mapping](Test_Migration_Mapping.md) (3 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (2 shared connections)
- [Archive Environment Contamination](Archive_Environment_Contamination.md) (2 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Async Code Review Docs](Async_Code_Review_Docs.md) (1 shared connections)

## Source Files

- `docs/examples/logging/websocket_integration.py`
- `server/monitoring/performance_monitor.py`

## Audit Trail

- EXTRACTED: 166 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*