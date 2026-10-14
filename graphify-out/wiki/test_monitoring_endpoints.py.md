# test_monitoring_endpoints.py

> 81 nodes

## Key Concepts

- **test_monitoring_endpoints.py** (55 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **HealthStatus** (48 connections) — `server/models/health.py`
- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **HealthResponse** (17 connections) — `server/models/health.py`
- **health_service.py** (16 connections) — `server/services/health_service.py`
- **health.py** (14 connections) — `server/models/health.py`
- **_request_with_container()** (13 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_health_status_healthy_returns_model()** (9 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_health_response_creation()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_dual_connection_and_performance_and_health_stats()** (7 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_health_components_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_unhealthy()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_no_alerts()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_with_alerts()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_status_version_fallback()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_memory_alerts_and_force_cleanup()** (6 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- *... and 56 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (47 shared connections)
- [test_health_service.py](test_health_service.py.md) (29 shared connections)
- [MovementMonitor](MovementMonitor.md) (16 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [HealthService](HealthService.md) (9 shared connections)
- [HealthErrorResponse](HealthErrorResponse.md) (6 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (4 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 266 (85%)
- INFERRED: 46 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*