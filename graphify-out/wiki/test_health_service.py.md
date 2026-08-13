# test_health_service.py

> 67 nodes

## Key Concepts

- **test_health_service.py** (43 connections) — `server/tests/unit/services/test_health_service.py`
- **health_service.py** (19 connections) — `server/services/health_service.py`
- **patch** (15 connections)
- **health.py** (14 connections) — `server/models/health.py`
- **HealthStatus** (11 connections) — `server/models/health.py`
- **get_health_service()** (9 connections) — `server/services/health_service.py`
- **test_get_health_status_version_fallback()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **health_service()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_no_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_degraded()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_error()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_healthy()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_unhealthy()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_cpu_usage_error()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_cpu_usage_success()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_database_component_health()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_creates_instance()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_returns_singleton()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_updates_connection_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_status_success()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_memory_usage_error()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_memory_usage_success()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_component_health_degraded()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_component_health_healthy()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 42 more nodes in this community*

## Relationships

- [test_health.py](test_health.py.md) (29 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 135 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*