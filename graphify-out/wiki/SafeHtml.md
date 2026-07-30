# SafeHtml

> 40 nodes

## Key Concepts

- **HealthService** (21 connections) — `server/services/health_service.py`
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **.check_database_health()** (6 connections) — `server/services/health_service.py`
- **Any** (5 connections)
- **._create_health_response()** (5 connections) — `server/services/health_service.py`
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **room_service()** (5 connections) — `server/tests/unit/game/test_room_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **health_service()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **HealthStatus** (2 connections)
- **Typed wrapper; utils stays free of ConnectionManager imports (import cycles).** (1 connections) — `server/realtime/connection_manager.py`
- **Health monitoring service for MythosMUD server.      Provides comprehensive heal** (1 connections) — `server/services/health_service.py`
- **Initialize the health service.          Args:             connection_manager: Co** (1 connections) — `server/services/health_service.py`
- **Get server uptime in seconds.** (1 connections) — `server/services/health_service.py`
- *... and 15 more nodes in this community*

## Relationships

- [alias](alias.md) (14 shared connections)
- [Any](Any.md) (5 shared connections)
- [fetch container items()](fetch_container_items%28%29.md) (2 shared connections)
- [follow commands](follow_commands.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [circuit breaker](circuit_breaker.md) (1 shared connections)
- [ExitStack](ExitStack.md) (1 shared connections)
- [test room service](test_room_service.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/services/health_service.py`
- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 139 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*