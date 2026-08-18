# server models health

> 106 nodes

## Key Concepts

- **HealthStatus** (48 connections) — `server/models/health.py`
- **test_health_service.py** (44 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health.py** (29 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **health.py** (15 connections) — `server/models/health.py`
- **patch** (15 connections)
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
- *... and 81 more nodes in this community*

## Relationships

- [healthstatus](healthstatus.md) (29 shared connections)
- [server api monitoring](server_api_monitoring.md) (19 shared connections)
- [fixturerequest](fixturerequest.md) (3 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (2 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 230 (84%)
- INFERRED: 44 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*