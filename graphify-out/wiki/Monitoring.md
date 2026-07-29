# monitoring

> 74 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (19 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
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
- **get_performance_stats()** (8 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_task_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (8 connections) — `server/api/monitoring.py`
- **test_dual_connection_and_performance_and_health_stats()** (6 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- *... and 49 more nodes in this community*

## Relationships

- [monitoring models](monitoring_models.md) (27 shared connections)
- [APIRouter](APIRouter.md) (18 shared connections)
- [get health status()](get_health_status%28%29.md) (17 shared connections)
- [main()](main%28%29.md) (12 shared connections)
- [movement monitor](movement_monitor.md) (11 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (8 shared connections)
- [task registry](task_registry.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [test movement monitor](test_movement_monitor.md) (2 shared connections)
- [init](init.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 438 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*