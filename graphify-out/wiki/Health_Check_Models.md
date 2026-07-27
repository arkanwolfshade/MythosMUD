# Health Check Models

> 66 nodes · cohesion 0.06

## Key Concepts

- **test_health.py** (26 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (22 connections) — `server/models/health.py`
- **ServerComponent** (22 connections) — `server/models/health.py`
- **ConnectionsComponent** (21 connections) — `server/models/health.py`
- **HealthComponents** (18 connections) — `server/models/health.py`
- **health_service.py** (17 connections) — `server/services/health_service.py`
- **HealthResponse** (15 connections) — `server/models/health.py`
- **health.py** (12 connections) — `server/models/health.py`
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **test_health_response_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_creation()** (6 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (6 connections) — `server/tests/unit/models/test_health.py`
- **test_determine_overall_status_degraded()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_unhealthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_no_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_with_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_status_version_fallback()** (5 connections) — `server/tests/unit/services/test_health_service.py`
- **test_connections_component_creation()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_connections_component_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_creation()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_without_last_query_time()** (3 connections) — `server/tests/unit/models/test_health.py`
- *... and 41 more nodes in this community*

## Relationships

- [[Monitoring API Endpoints]] (14 shared connections)
- [[Health Service Tests]] (11 shared connections)
- [[Memory Profiler Tools]] (7 shared connections)
- [[Admin NPC Schemas]] (6 shared connections)
- [[NPC Admin API]] (4 shared connections)
- [[SQLAlchemy Model Base]] (3 shared connections)
- [[Room Occupant Events]] (2 shared connections)
- [[Application DI Bundles]] (1 shared connections)
- [[Health Check Service]] (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 298 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
