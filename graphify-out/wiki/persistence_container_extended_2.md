# persistence container extended

> 34 nodes

## Key Concepts

- **HealthService** (21 connections) — `server/services/health_service.py`
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
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **HealthStatus** (2 connections)
- **Health monitoring service for MythosMUD server.      Provides comprehensive heal** (1 connections) — `server/services/health_service.py`
- **Initialize the health service.          Args:             connection_manager: Co** (1 connections) — `server/services/health_service.py`
- **Get server uptime in seconds.** (1 connections) — `server/services/health_service.py`
- **Get current memory usage in MB.** (1 connections) — `server/services/health_service.py`
- **Get current CPU usage percentage.** (1 connections) — `server/services/health_service.py`
- **Create a standardized health check response dictionary.          Args:** (1 connections) — `server/services/health_service.py`
- **Check database connectivity and health with actual query validation.          Th** (1 connections) — `server/services/health_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [grace period login](grace_period_login.md) (9 shared connections)
- [player look commands](player_look_commands.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [room service game](room_service_game.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`

## Audit Trail

- EXTRACTED: 117 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*