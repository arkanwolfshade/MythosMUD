# Monitoring

> 82 nodes

## Key Concepts

- **api/monitoring.py** (61 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (20 connections)
- **HealthResponse** (17 connections) — `server/models/health.py`
- **asyncio** (15 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **get** (14 connections)
- **get_health_status()** (13 connections) — `server/api/monitoring.py`
- **_request_with_container()** (13 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (11 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (11 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
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
- *... and 57 more nodes in this community*

## Relationships

- [Monitoring Models](Monitoring_Models.md) (32 shared connections)
- [Test Health](Test_Health.md) (19 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (19 shared connections)
- [Movement Monitor](Movement_Monitor.md) (11 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [Health Service](Health_Service.md) (4 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Test Memory Profiler](Test_Memory_Profiler.md) (2 shared connections)
- [Cache Service](Cache_Service.md) (2 shared connections)
- [Task Registry](Task_Registry.md) (2 shared connections)
- [Async Persistence](Async_Persistence.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/models/health.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 318 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*