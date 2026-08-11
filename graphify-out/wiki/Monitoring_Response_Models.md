# Monitoring Response Models

> 130 nodes

## Key Concepts

- **test_health_service.py** (43 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (19 connections) — `server/services/health_service.py`
- **HealthResponse** (18 connections) — `server/models/health.py`
- **health.py** (14 connections) — `server/models/health.py`
- **get_health_status()** (12 connections) — `server/api/monitoring.py`
- **HealthStatus** (11 connections) — `server/models/health.py`
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **memory_profiler.py** (10 connections) — `server/utils/memory_profiler.py`
- **get_health_service()** (9 connections) — `server/services/health_service.py`
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
- *... and 105 more nodes in this community*

## Relationships

- [Command Field Validators](Command_Field_Validators.md) (21 shared connections)
- [Config Model Tests](Config_Model_Tests.md) (13 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (7 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (6 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 498 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*