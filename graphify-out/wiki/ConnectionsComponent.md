# ConnectionsComponent

> 39 nodes

## Key Concepts

- **HealthService** (21 connections) — `server/services/health_service.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **Any** (5 connections)
- **._create_health_response()** (5 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (5 connections) — `server/services/health_service.py`
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **.check_database_health()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **HealthComponents** (3 connections)
- **HealthStatus** (2 connections)
- **DatabaseComponent** (2 connections)
- **ServerComponent** (1 connections)
- **ConnectionsComponent** (1 connections)
- **HealthResponse** (1 connections)
- **Health monitoring service for MythosMUD server.      Provides comprehensive heal** (1 connections) — `server/services/health_service.py`
- **Initialize the health service.          Args:             connection_manager: Co** (1 connections) — `server/services/health_service.py`
- *... and 14 more nodes in this community*

## Relationships

- [get health service()](get_health_service%28%29.md) (4 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (2 shared connections)

## Source Files

- `server/services/health_service.py`

## Audit Trail

- EXTRACTED: 123 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*