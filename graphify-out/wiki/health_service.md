# Health Service

> 41 nodes

## Key Concepts

- **HealthService** (27 connections) — `server/services/health_service.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (17 connections) — `server/services/health_service.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (7 connections) — `server/services/health_service.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **Any** (7 connections)
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **._health_from_pool()** (5 connections) — `server/services/health_service.py`
- **._ping_database()** (5 connections) — `server/services/health_service.py`
- **.check_database_health()** (4 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **._status_from_query_ms()** (4 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **HealthStatus** (3 connections)
- **Health status for all system components.** (1 connections) — `server/models/health.py`
- **Health monitoring service for MythosMUD. This module provides comprehensive…** (1 connections) — `server/services/health_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [Test Health](Test_Health.md) (22 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (7 shared connections)
- [Test Health Service](Test_Health_Service.md) (6 shared connections)
- [Monitoring](Monitoring.md) (4 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (3 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/services/health_service.py`

## Audit Trail

- EXTRACTED: 111 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*