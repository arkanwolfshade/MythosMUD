# Test Health

> 64 nodes

## Key Concepts

- **HealthStatus** (48 connections) — `server/models/health.py`
- **test_health.py** (29 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **health.py** (15 connections) — `server/models/health.py`
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
- **test_connections_component_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_creation()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_without_last_query_time()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_server_component_creation()** (4 connections) — `server/tests/unit/models/test_health.py`
- *... and 39 more nodes in this community*

## Relationships

- [Test Health Service](Test_Health_Service.md) (27 shared connections)
- [Health Service](Health_Service.md) (22 shared connections)
- [Monitoring](Monitoring.md) (19 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (3 shared connections)
- [Test Memory Profiler](Test_Memory_Profiler.md) (2 shared connections)
- [Command Aliases](Command_Aliases.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 162 (79%)
- INFERRED: 44 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*