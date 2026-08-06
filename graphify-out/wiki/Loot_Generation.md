# Loot Generation

> 246 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_health_service.py** (43 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **MovementMonitor** (21 connections) — `server/game/movement_monitor.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (20 connections) — `server/services/health_service.py`
- **Request** (19 connections)
- **BaseModel** (19 connections)
- **HealthResponse** (17 connections) — `server/models/health.py`
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **health.py** (14 connections) — `server/models/health.py`
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **get_health_status()** (12 connections) — `server/api/monitoring.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **HealthStatus** (11 connections) — `server/models/health.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- *... and 221 more nodes in this community*

## Relationships

- [Magic Spell Service](Magic_Spell_Service.md) (22 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (19 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (14 shared connections)
- [Error Conversion](Error_Conversion.md) (12 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (10 shared connections)
- [services rescue service](services_rescue_service.md) (9 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (7 shared connections)
- [add used user](add_used_user.md) (7 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (5 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (4 shared connections)
- [follow service game](follow_service_game.md) (2 shared connections)
- [player event handlers](player_event_handlers.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/models/health.py`
- `server/realtime/connection_manager.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 1112 (99%)
- INFERRED: 16 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*