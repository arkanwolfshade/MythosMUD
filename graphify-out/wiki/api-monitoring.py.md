# api/monitoring.py

> 114 nodes

## Key Concepts

- **api/monitoring.py** (64 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (59 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **monitoring_models.py** (23 connections) — `server/api/monitoring_models.py`
- **BaseModel** (19 connections)
- **Request** (19 connections)
- **asyncio** (15 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **get** (14 connections)
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **get_memory_stats()** (11 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (11 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **force_memory_cleanup()** (10 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (10 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (10 connections) — `server/api/monitoring.py`
- **reset_metrics()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (10 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (9 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (9 connections) — `server/api/monitoring.py`
- *... and 89 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (23 shared connections)
- [HealthStatus](HealthStatus.md) (23 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (12 shared connections)
- [MovementMonitor](MovementMonitor.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (5 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (2 shared connections)
- [HealthService](HealthService.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [MovementService](MovementService.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 360 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*