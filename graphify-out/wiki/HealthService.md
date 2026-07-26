# HealthService

> 36 nodes · cohesion 0.08

## Key Concepts

- **HealthService** (21 connections) — `server/services/health_service.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **.check_database_health()** (6 connections) — `server/services/health_service.py`
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **._create_health_response()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **Any** (5 connections)
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **health_service()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **HealthStatus** (2 connections)
- **Check database connectivity and health with actual query validation.          Th** (1 connections) — `server/services/health_service.py`
- **Check database connectivity and health (sync wrapper).          For async contex** (1 connections) — `server/services/health_service.py`
- **Check connection manager health.** (1 connections) — `server/services/health_service.py`
- **Get server component health status.** (1 connections) — `server/services/health_service.py`
- **Get database component health status (async version with actual validation).** (1 connections) — `server/services/health_service.py`
- **Get database component health status (sync version).** (1 connections) — `server/services/health_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [test_health_service.py](test_health_service.py.md) (13 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_room_service.py](test_room_service.py.md) (2 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 120 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*