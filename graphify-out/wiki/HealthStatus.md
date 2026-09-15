# HealthStatus

> 146 nodes

## Key Concepts

- **HealthStatus** (48 connections) — `server/models/health.py`
- **test_health_service.py** (42 connections) — `server/tests/unit/services/test_health_service.py`
- **HealthService** (27 connections) — `server/services/health_service.py`
- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **HealthResponse** (17 connections) — `server/models/health.py`
- **health_service.py** (16 connections) — `server/services/health_service.py`
- **health.py** (14 connections) — `server/models/health.py`
- **patch** (14 connections)
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **test_health_response_creation()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **.check_database_health_async()** (7 connections) — `server/services/health_service.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **test_health_components_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_unhealthy()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_no_alerts()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 121 more nodes in this community*

## Relationships

- [api/monitoring.py](api-monitoring.py.md) (20 shared connections)
- [HealthErrorResponse](HealthErrorResponse.md) (6 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [_RaisesOnBool](_RaisesOnBool.md) (3 shared connections)
- [health_service](health_service.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 307 (86%)
- INFERRED: 48 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*