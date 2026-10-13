# Community 400

> 43 nodes

## Key Concepts

- **HealthService** (27 connections) — `server/services/health_service.py`
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager.py`
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
- **test_health_service_accepts_injected_async_persistence()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health_service_accepts_injected_room_service()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **HealthStatus** (3 connections)
- **Typed wrapper; utils stays free of ConnectionManager imports (import cycles).** (1 connections) — `server/realtime/connection_manager.py`
- *... and 18 more nodes in this community*

## Relationships

- [Community 70](Community_70.md) (13 shared connections)
- [Community 426](Community_426.md) (4 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 1508](Community_1508.md) (1 shared connections)
- [Community 180](Community_180.md) (1 shared connections)
- [Community 233](Community_233.md) (1 shared connections)
- [Community 467](Community_467.md) (1 shared connections)
- [Community 47](Community_47.md) (1 shared connections)
- [Community 106](Community_106.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 92 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*