# test_health.py

> 68 nodes

## Key Concepts

- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (20 connections) — `server/services/health_service.py`
- **HealthResponse** (16 connections) — `server/models/health.py`
- **health.py** (14 connections) — `server/models/health.py`
- **HealthStatus** (11 connections) — `server/models/health.py`
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **test_health_response_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_creation()** (6 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (6 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_unhealthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_no_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_with_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **BaseModel** (6 connections)
- **test_connections_component_creation()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_connections_component_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_creation()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_health.py`
- *... and 43 more nodes in this community*

## Relationships

- [test_health_service.py](test_health_service.py.md) (16 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (13 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [HealthService](HealthService.md) (9 shared connections)
- [Player](Player.md) (4 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 192 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*