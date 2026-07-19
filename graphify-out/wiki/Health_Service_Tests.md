# Health Service Tests

> 49 nodes · cohesion 0.05

## Key Concepts

- **test_health_service.py** (40 connections) — `server/tests/unit/services/test_health_service.py`
- **get_health_service()** (9 connections) — `server/services/health_service.py`
- **test_get_health_service_creates_instance()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_returns_singleton()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_updates_connection_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **Test check_connections_health returns healthy status.** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **Test get_server_component_health returns healthy status.** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **Test check_database_health returns healthy status.** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_degraded()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_healthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_no_manager()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_unhealthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_degraded()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_error()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_healthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_unhealthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_connections_component_health()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_cpu_usage_error()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_cpu_usage_success()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_database_component_health()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_status_success()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_memory_usage_error()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_memory_usage_success()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_component_health_degraded()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 24 more nodes in this community*

## Relationships

- [[Health Check Models]] (11 shared connections)
- [[Health Check Service]] (3 shared connections)
- [[Monitoring API Endpoints]] (2 shared connections)
- [[Memory Profiler Tools]] (1 shared connections)
- [[Command Request App State]] (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 126 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
