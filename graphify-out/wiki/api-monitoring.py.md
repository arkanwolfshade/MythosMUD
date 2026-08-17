# api/monitoring.py

> 173 nodes

## Key Concepts

- **api/monitoring.py** (64 connections) — `server/api/monitoring.py`
- **HealthStatus** (48 connections) — `server/models/health.py`
- **test_health_service.py** (44 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health.py** (29 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **monitoring_models.py** (23 connections) — `server/api/monitoring_models.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (21 connections) — `server/services/health_service.py`
- **BaseModel** (19 connections)
- **HealthResponse** (17 connections) — `server/models/health.py`
- **health.py** (15 connections) — `server/models/health.py`
- **patch** (15 connections)
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **get_health_service()** (9 connections) — `server/services/health_service.py`
- **test_health_response_creation()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **reset_movement_monitor()** (7 connections) — `server/game/movement_monitor.py`
- **test_health_components_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 148 more nodes in this community*

## Relationships

- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (54 shared connections)
- [get_logger](get_logger.md) (28 shared connections)
- [HealthService](HealthService.md) (13 shared connections)
- [pytest.md](pytest.md.md) (6 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [memory_profiler.py](memory_profiler.py.md) (4 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (4 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [health_service](health_service.md) (2 shared connections)
- [MovementMonitor](MovementMonitor.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/models/health.py`
- `server/realtime/connection_manager.py`
- `server/services/health_service.py`
- `server/tests/unit/game/test_movement_monitor.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 359 (75%)
- INFERRED: 121 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*