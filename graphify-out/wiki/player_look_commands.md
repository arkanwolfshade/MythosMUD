# player look commands

> 54 nodes

## Key Concepts

- **test_health_service.py** (43 connections) — `server/tests/unit/services/test_health_service.py`
- **get_health_service()** (9 connections) — `server/services/health_service.py`
- **test_get_health_service_creates_instance()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_returns_singleton()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_service_updates_connection_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health_service_initialization()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_uptime()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_memory_usage_success()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_memory_usage_error()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_cpu_usage_success()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_cpu_usage_error()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_healthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_degraded()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_unhealthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_database_health_error()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_healthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_degraded()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_unhealthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_no_manager()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_check_connections_health_error()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_component_health_healthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_component_health_degraded()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_server_component_health_unhealthy()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_database_component_health()** (2 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 29 more nodes in this community*

## Relationships

- [grace period login](grace_period_login.md) (15 shared connections)
- [persistence container extended](persistence_container_extended.md) (4 shared connections)
- [command combat models](command_combat_models.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 132 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*