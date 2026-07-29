# get health status()

> 71 nodes

## Key Concepts

- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **ServerComponent** (21 connections) — `server/models/health.py`
- **DatabaseComponent** (21 connections) — `server/models/health.py`
- **ConnectionsComponent** (20 connections) — `server/models/health.py`
- **HealthComponents** (17 connections) — `server/models/health.py`
- **HealthResponse** (15 connections) — `server/models/health.py`
- **health.py** (13 connections) — `server/models/health.py`
- **get_health_status()** (12 connections) — `server/api/monitoring.py`
- **HealthStatus** (10 connections) — `server/models/health.py`
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **test_get_health_status_healthy_returns_model()** (7 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_health_components_rejects_extra_fields()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (7 connections) — `server/tests/unit/models/test_health.py`
- **BaseModel** (6 connections)
- **test_health_components_creation()** (6 connections) — `server/tests/unit/models/test_health.py`
- **test_generate_alerts_no_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_with_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_degraded()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_unhealthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_status_version_fallback()** (5 connections) — `server/tests/unit/services/test_health_service.py`
- **test_server_component_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_server_component_frozen()** (4 connections) — `server/tests/unit/models/test_health.py`
- *... and 46 more nodes in this community*

## Relationships

- [monitoring](monitoring.md) (17 shared connections)
- [get health service()](get_health_service%28%29.md) (13 shared connections)
- [. init ()](_init_%28%29.md) (8 shared connections)
- [Base](Base.md) (4 shared connections)
- [test memory profiler](test_memory_profiler.md) (4 shared connections)
- [APIRouter](APIRouter.md) (1 shared connections)
- [benchmark model memory usage()](benchmark_model_memory_usage%28%29.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/models/health.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 314 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*