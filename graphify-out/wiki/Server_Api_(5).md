# Server Api (5)

> 131 nodes

## Key Concepts

- **monitoring.py** (61 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **MovementMonitor** (21 connections) — `server/game/movement_monitor.py`
- **Request** (19 connections)
- **BaseModel** (19 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **get_movement_metrics()** (9 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (9 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (9 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (9 connections) — `server/api/monitoring.py`
- **_resolve_cache_manager_from_request()** (9 connections) — `server/api/monitoring.py`
- **get_system_alerts()** (8 connections) — `server/api/monitoring.py`
- **reset_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (8 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (8 connections) — `server/api/monitoring.py`
- **force_memory_cleanup()** (8 connections) — `server/api/monitoring.py`
- *... and 106 more nodes in this community*

## Relationships

- [Server Monitoring](Server_Monitoring.md) (24 shared connections)
- [Server Api](Server_Api.md) (20 shared connections)
- [Server Models (10)](Server_Models_%2810%29.md) (18 shared connections)
- [Server Commands](Server_Commands.md) (10 shared connections)
- [Server Game (32)](Server_Game_%2832%29.md) (9 shared connections)
- [Server Game (17)](Server_Game_%2817%29.md) (7 shared connections)
- [Server Admin](Server_Admin.md) (6 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (2 shared connections)
- [Server Middleware](Server_Middleware.md) (2 shared connections)
- [Server (6)](Server_%286%29.md) (2 shared connections)
- [Server Game (19)](Server_Game_%2819%29.md) (2 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/app/task_registry.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 687 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*