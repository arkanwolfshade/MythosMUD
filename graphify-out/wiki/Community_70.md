# Community 70

> 115 nodes

## Key Concepts

- **HealthStatus** (48 connections) — `server/models/health.py`
- **test_health_service.py** (42 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **HealthResponse** (17 connections) — `server/models/health.py`
- **health_service.py** (16 connections) — `server/services/health_service.py`
- **health.py** (14 connections) — `server/models/health.py`
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
- **_RaisesOnBool** (4 connections) — `server/tests/unit/services/test_health_service.py`
- *... and 90 more nodes in this community*

## Relationships

- [Community 180](Community_180.md) (15 shared connections)
- [Community 400](Community_400.md) (13 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (9 shared connections)
- [Community 467](Community_467.md) (5 shared connections)
- [Community 216](Community_216.md) (4 shared connections)
- [Community 1508](Community_1508.md) (2 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 251 (85%)
- INFERRED: 46 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*