# grace period login

> 73 nodes

## Key Concepts

- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (20 connections) — `server/services/health_service.py`
- **HealthResponse** (17 connections) — `server/models/health.py`
- **health.py** (14 connections) — `server/models/health.py`
- **get_health_status()** (12 connections) — `server/api/monitoring.py`
- **HealthStatus** (11 connections) — `server/models/health.py`
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
- *... and 48 more nodes in this community*

## Relationships

- [player look commands](player_look_commands.md) (15 shared connections)
- [health models rationale](health_models_rationale.md) (11 shared connections)
- [persistence container extended](persistence_container_extended.md) (9 shared connections)
- [command combat models](command_combat_models.md) (8 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (8 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (5 shared connections)
- [task registry app](task_registry_app.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (1 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 350 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*