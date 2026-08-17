# test_monitoring_endpoints.py

> 71 nodes

## Key Concepts

- **test_monitoring_endpoints.py** (59 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (19 connections)
- **asyncio** (15 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
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
- **MessageResponse** (6 connections) — `server/api/monitoring_models.py`
- *... and 46 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (44 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [HealthStatus](HealthStatus.md) (14 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (7 shared connections)
- [MovementMonitor](MovementMonitor.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 235 (92%)
- INFERRED: 20 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*