# Monitoring API Endpoints

> 71 nodes · cohesion 0.06

## Key Concepts

- **monitoring.py** (60 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (53 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (33 connections) — `server/api/monitoring.py`
- **_resolve_connection_manager_from_request()** (15 connections) — `server/api/monitoring.py`
- **get_health_status()** (12 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (9 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (9 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (9 connections) — `server/api/monitoring.py`
- **_resolve_cache_manager_from_request()** (9 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (9 connections) — `server/api/monitoring.py`
- **force_memory_cleanup()** (8 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (8 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (8 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (8 connections) — `server/api/monitoring.py`
- **get_system_alerts()** (8 connections) — `server/api/monitoring.py`
- **get_task_metrics()** (8 connections) — `server/api/monitoring.py`
- **reset_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_registry()** (7 connections) — `server/app/task_registry.py`
- *... and 46 more nodes in this community*

## Relationships

- [[Monitoring Response Models]] (52 shared connections)
- [[Container Exception Handlers]] (18 shared connections)
- [[Health Check Models]] (14 shared connections)
- [[Movement Performance Monitor]] (12 shared connections)
- [[NPC Admin API]] (8 shared connections)
- [[Memory Leak Metrics]] (4 shared connections)
- [[Database Manager Tests]] (3 shared connections)
- [[Cache and NPC Cache]] (2 shared connections)
- [[Memory Profiler Tools]] (2 shared connections)
- [[Room Occupant Events]] (2 shared connections)
- [[Health Service Tests]] (2 shared connections)
- [[System Monitoring API]] (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/app/task_registry.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 428 (96%)
- INFERRED: 18 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
