# Community 830

> 19 nodes

## Key Concepts

- **HealthResponse** (16 connections) — `server/models/health.py`
- **get_health_status()** (13 connections) — `server/api/monitoring.py`
- **HealthErrorResponse** (9 connections) — `server/models/health.py`
- **test_get_health_status_healthy_returns_model()** (9 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **_assemble_health_response()** (5 connections) — `server/api/monitoring.py`
- **health_service()** (5 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health_error_response_creation()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_health_error_response_frozen()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_health_error_response_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_health.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **fixture** (2 connections)
- **Return aggregated health status for monitoring.** (1 connections) — `server/api/monitoring.py`
- **Error response for health check failures.** (1 connections) — `server/models/health.py`
- **Complete health response for the system.** (1 connections) — `server/models/health.py`
- **Test HealthErrorResponse can be created with required fields.** (1 connections) — `server/tests/unit/models/test_health.py`
- **Test HealthErrorResponse rejects unknown fields.** (1 connections) — `server/tests/unit/models/test_health.py`
- **Test HealthErrorResponse is frozen (immutable).** (1 connections) — `server/tests/unit/models/test_health.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/services/test_health_service.py`
- **Create a HealthService instance.** (1 connections) — `server/tests/unit/services/test_health_service.py`

## Relationships

- [Community 77](Community_77.md) (20 shared connections)
- [Community 178](Community_178.md) (9 shared connections)
- [Community 421](Community_421.md) (4 shared connections)
- [Community 408](Community_408.md) (2 shared connections)
- [Community 196](Community_196.md) (2 shared connections)
- [Community 147](Community_147.md) (1 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/models/health.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 51 (86%)
- INFERRED: 8 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*