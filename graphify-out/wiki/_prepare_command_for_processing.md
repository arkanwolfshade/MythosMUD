# _prepare_command_for_processing

> 104 nodes · cohesion 0.03

## Key Concepts

- **PerformanceMonitor** (35 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (24 connections) — `server/monitoring/performance_monitor.py`
- **websocket_integration.py** (22 connections) — `docs/examples/logging/websocket_integration.py`
- **measure_performance()** (20 connections) — `server/monitoring/performance_monitor.py`
- **test_performance_monitor.py** (18 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **get_performance_monitor()** (16 connections) — `server/monitoring/performance_monitor.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **PerformanceStats** (10 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **handle_websocket_message()** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **.record_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **record_performance_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **reset_performance_metrics()** (6 connections) — `server/monitoring/performance_monitor.py`
- **WebSocket** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **get_performance_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.get_operation_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- **handle_game_action()** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket_endpoint()** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **WebSocketRateLimiter** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **ExportMetrics** (4 connections) — `server/monitoring/performance_monitor.py`
- **._evict_operation_stats()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_all_stats()** (4 connections) — `server/monitoring/performance_monitor.py`
- *... and 79 more nodes in this community*

## Relationships

- [Room](Room.md) (10 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (7 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (4 shared connections)
- [PlayerMute](PlayerMute.md) (4 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (3 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (3 shared connections)
- [ExitEdge.tsx](ExitEdge.tsx.md) (3 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (2 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)

## Source Files

- `docs/examples/logging/websocket_integration.py`
- `server/monitoring/__init__.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 199 (93%)
- INFERRED: 15 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*