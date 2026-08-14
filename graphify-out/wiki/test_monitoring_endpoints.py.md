# test_monitoring_endpoints.py

> 73 nodes

## Key Concepts

- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (19 connections)
- **asyncio** (15 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get** (14 connections)
- **get_health_status()** (13 connections) — `server/api/monitoring.py`
- **get_memory_stats()** (11 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_connection_health_stats()** (10 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (10 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **force_memory_cleanup()** (9 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (9 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (9 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (9 connections) — `server/api/monitoring.py`
- **get_system_alerts()** (9 connections) — `server/api/monitoring.py`
- **get_task_metrics()** (9 connections) — `server/api/monitoring.py`
- **reset_metrics()** (9 connections) — `server/api/monitoring.py`
- **_resolve_cache_manager_from_request()** (9 connections) — `server/api/monitoring.py`
- **test_dual_connection_and_performance_and_health_stats()** (7 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- *... and 48 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (34 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [test_health.py](test_health.py.md) (13 shared connections)
- [monitoring_models.py](monitoring_models.py.md) (11 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (4 shared connections)
- [MovementMonitor](MovementMonitor.md) (4 shared connections)
- [test_health_service.py](test_health_service.py.md) (1 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (1 shared connections)
- [get_cache_manager](get_cache_manager.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 258 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*