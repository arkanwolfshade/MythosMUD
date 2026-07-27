# Health Check Service

> 41 nodes · cohesion 0.07

## Key Concepts

- **HealthService** (20 connections) — `server/services/health_service.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **Any** (5 connections) — `server/services/health_service.py`
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (5 connections) — `server/services/health_service.py`
- **._create_health_response()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **.check_database_health()** (4 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **HealthComponents** (3 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **health_service()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **DatabaseComponent** (2 connections) — `server/services/health_service.py`
- **HealthStatus** (2 connections) — `server/services/health_service.py`
- **ConnectionsComponent** (1 connections) — `server/services/health_service.py`
- **HealthResponse** (1 connections) — `server/services/health_service.py`
- **ServerComponent** (1 connections) — `server/services/health_service.py`
- **Check database connectivity and health with actual query validation.          Th** (1 connections) — `server/services/health_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [[Health Service Tests]] (3 shared connections)
- [[Health Check Models]] (1 shared connections)
- [[Combat Player Broadcasts]] (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 126 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
