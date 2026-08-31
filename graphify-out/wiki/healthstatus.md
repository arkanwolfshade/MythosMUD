# HealthStatus

> 113 nodes

## Key Concepts

- **HealthStatus** (48 connections) — `server/models/health.py`
- **test_health_service.py** (43 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health.py** (29 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **HealthResponse** (17 connections) — `server/models/health.py`
- **health_service.py** (17 connections) — `server/services/health_service.py`
- **health.py** (15 connections) — `server/models/health.py`
- **patch** (14 connections)
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **test_health_response_creation()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_unhealthy()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_no_alerts()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_with_alerts()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_status_version_fallback()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **BaseModel** (6 connections)
- **test_connections_component_creation()** (4 connections) — `server/tests/unit/models/test_health.py`
- *... and 88 more nodes in this community*

## Relationships

- [api/monitoring.py](api-monitoring.py.md) (21 shared connections)
- [HealthService](HealthService.md) (12 shared connections)
- [Player](Player.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [_RaisesOnBool](_RaisesOnBool.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [health_service](health_service.md) (2 shared connections)
- [asyncio.md](asyncio.md.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 252 (85%)
- INFERRED: 46 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*