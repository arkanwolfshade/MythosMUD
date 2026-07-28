# Server Models (10)

> 73 nodes

## Key Concepts

- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (19 connections) — `server/services/health_service.py`
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

- [Server Api (5)](Server_Api_%285%29.md) (18 shared connections)
- [Server Services (33)](Server_Services_%2833%29.md) (15 shared connections)
- [Server Services (48)](Server_Services_%2848%29.md) (9 shared connections)
- [Server Utils](Server_Utils.md) (7 shared connections)
- [Server Utils (11)](Server_Utils_%2811%29.md) (5 shared connections)
- [Server Models (14)](Server_Models_%2814%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (1 shared connections)
- [Server Api](Server_Api.md) (1 shared connections)
- [Server App](Server_App.md) (1 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 349 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*