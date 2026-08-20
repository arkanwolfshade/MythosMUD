# api/monitoring.py

> 106 nodes

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
- **get_performance_summary()** (9 connections) — `server/api/monitoring.py`
- *... and 81 more nodes in this community*

## Relationships

- [HealthStatus](HealthStatus.md) (23 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (18 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [get_monitoring_dashboard](get_monitoring_dashboard.md) (11 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (7 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (5 shared connections)
- [MovementMonitor](MovementMonitor.md) (5 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [MovementService](MovementService.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 355 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*