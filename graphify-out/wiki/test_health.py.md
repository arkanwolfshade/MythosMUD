# test_health.py

> 100 nodes

## Key Concepts

- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **HealthService** (23 connections) — `server/services/health_service.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **HealthResponse** (16 connections) — `server/models/health.py`
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (9 connections) — `server/services/health_service.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **test_health_response_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (7 connections) — `server/tests/unit/models/test_health.py`
- **Any** (7 connections)
- **.check_database_health()** (6 connections) — `server/services/health_service.py`
- **room_service()** (6 connections) — `server/tests/unit/game/test_room_service.py`
- **test_health_components_creation()** (6 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (6 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_unhealthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_no_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_with_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 75 more nodes in this community*

## Relationships

- [test_health_service.py](test_health_service.py.md) (29 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (14 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [fixture](fixture.md) (1 shared connections)
- [test_room_service.py](test_room_service.py.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 237 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*