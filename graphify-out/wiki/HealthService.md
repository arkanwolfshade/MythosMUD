# HealthService

> 41 nodes

## Key Concepts

- **HealthService** (27 connections) — `server/services/health_service.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (7 connections) — `server/services/health_service.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **Any** (7 connections)
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **._health_from_pool()** (5 connections) — `server/services/health_service.py`
- **._ping_database()** (5 connections) — `server/services/health_service.py`
- **.check_database_health()** (4 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **._status_from_query_ms()** (4 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **test_health_service_accepts_injected_async_persistence()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health_service_accepts_injected_room_service()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **HealthStatus** (3 connections)
- **Create a standardized health check response dictionary. Args: status: Health…** (1 connections) — `server/services/health_service.py`
- **Async database health check.** (1 connections) — `server/services/health_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [HealthStatus](HealthStatus.md) (12 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [health_service](health_service.md) (1 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 82 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*