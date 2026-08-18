# test_monitoring_endpoints.py

> 67 nodes

## Key Concepts

- **test_monitoring_endpoints.py** (59 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (19 connections)
- **asyncio** (15 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **get** (14 connections)
- **get_memory_stats()** (11 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (11 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_connection_health_stats()** (10 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (10 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (9 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (9 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (9 connections) — `server/api/monitoring.py`
- **get_system_alerts()** (9 connections) — `server/api/monitoring.py`
- **get_task_metrics()** (9 connections) — `server/api/monitoring.py`
- **_resolve_cache_manager_from_request()** (9 connections) — `server/api/monitoring.py`
- **test_dual_connection_and_performance_and_health_stats()** (7 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_memory_alerts_and_force_cleanup()** (6 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- *... and 42 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (41 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (15 shared connections)
- [HealthStatus](HealthStatus.md) (14 shared connections)
- [force_memory_cleanup](force_memory_cleanup.md) (8 shared connections)
- [MovementMonitor](MovementMonitor.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (2 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 247 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*