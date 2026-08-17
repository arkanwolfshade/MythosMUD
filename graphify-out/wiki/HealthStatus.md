# HealthStatus

> 168 nodes

## Key Concepts

- **HealthStatus** (48 connections) — `server/models/health.py`
- **test_health_service.py** (44 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health.py** (29 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **HealthService** (24 connections) — `server/services/health_service.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (21 connections) — `server/services/health_service.py`
- **HealthResponse** (17 connections) — `server/models/health.py`
- **health.py** (15 connections) — `server/models/health.py`
- **patch** (15 connections)
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **get_health_service()** (9 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (9 connections) — `server/services/health_service.py`
- **test_get_health_status_healthy_returns_model()** (9 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_health_response_creation()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **test_health_components_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 143 more nodes in this community*

## Relationships

- [api/monitoring.py](api-monitoring.py.md) (24 shared connections)
- [get_session_maker](get_session_maker.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (4 shared connections)
- [.get_instance](get_instance.md) (2 shared connections)
- [test_room_service.py](test_room_service.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 292 (74%)
- INFERRED: 105 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*