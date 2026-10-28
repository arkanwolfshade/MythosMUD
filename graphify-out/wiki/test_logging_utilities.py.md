# test_logging_utilities.py

> 100 nodes · cohesion 0.04

## Key Concepts

- **HealthService** (27 connections) — `server/services/health_service.py`
- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (16 connections) — `server/services/health_service.py`
- **health.py** (14 connections) — `server/models/health.py`
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **test_health_response_creation()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **.check_database_health_async()** (7 connections) — `server/services/health_service.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **Any** (7 connections)
- **test_health_components_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_unhealthy()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_no_alerts()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_with_alerts()** (7 connections) — `server/tests/unit/services/test_health_service.py`
- **BaseModel** (6 connections)
- *... and 75 more nodes in this community*

## Relationships

- [✅ POSITIVE FINDINGS](✅_POSITIVE_FINDINGS.md) (41 shared connections)
- [Player](Player.md) (22 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [ItemFactory](ItemFactory.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (1 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 237 (89%)
- INFERRED: 28 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*