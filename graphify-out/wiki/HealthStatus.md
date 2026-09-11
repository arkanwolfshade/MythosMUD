# HealthStatus

> 167 nodes

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
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager.py`
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **test_get_health_status_healthy_returns_model()** (9 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_health_response_creation()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **.check_database_health_async()** (7 connections) — `server/services/health_service.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **test_health_components_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 142 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (22 shared connections)
- [Player](Player.md) (4 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (4 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [time.py](time.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [resolve_connection_manager](resolve_connection_manager.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/realtime/connection_manager.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 338 (87%)
- INFERRED: 49 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*