# test_health_service.py

> 58 nodes

## Key Concepts

- **test_health_service.py** (44 connections) — `server/tests/unit/services/test_health_service.py`
- **patch** (15 connections)
- **get_health_service()** (9 connections) — `server/services/health_service.py`
- **health_service()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_no_manager()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_degraded()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_error()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_healthy()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_unhealthy()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_database_component_health()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_creates_instance()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_status_success()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_component_health_degraded()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_component_health_healthy()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_component_health_unhealthy()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_degraded()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_error()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_healthy()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_unhealthy()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_connections_component_health()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_cpu_usage_error()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_cpu_usage_success()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_returns_singleton()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_updates_connection_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 33 more nodes in this community*

## Relationships

- [HealthStatus](HealthStatus.md) (30 shared connections)
- [HealthService](HealthService.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 95 (85%)
- INFERRED: 17 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*