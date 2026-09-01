# api/monitoring.py

> 90 nodes

## Key Concepts

- **api/monitoring.py** (61 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (20 connections)
- **asyncio** (15 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **get** (14 connections)
- **_request_with_container()** (13 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **get_memory_stats()** (11 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (11 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager.py`
- **force_memory_cleanup()** (10 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (10 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (10 connections) — `server/api/monitoring.py`
- **reset_metrics()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector_from_request()** (10 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (10 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (9 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (9 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (9 connections) — `server/api/monitoring.py`
- *... and 65 more nodes in this community*

## Relationships

- [system_monitoring.py](system_monitoring.py.md) (31 shared connections)
- [HealthStatus](HealthStatus.md) (22 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (18 shared connections)
- [MovementMonitor](MovementMonitor.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (2 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 331 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*