# HealthService

> 44 nodes

## Key Concepts

- **HealthService** (24 connections) — `server/services/health_service.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (9 connections) — `server/services/health_service.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **Any** (7 connections)
- **.check_database_health()** (6 connections) — `server/services/health_service.py`
- **room_service()** (6 connections) — `server/tests/unit/game/test_room_service.py`
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **._health_from_pool()** (5 connections) — `server/services/health_service.py`
- **._ping_database()** (5 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **._status_from_query_ms()** (4 connections) — `server/services/health_service.py`
- **health_service()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **HealthStatus** (3 connections)
- **fixture** (2 connections)
- *... and 19 more nodes in this community*

## Relationships

- [HealthStatus](HealthStatus.md) (14 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_room_service.py](test_room_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 86 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*