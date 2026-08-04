# health models rationale

> 107 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **Request** (19 connections)
- **BaseModel** (19 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (9 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (9 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (9 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (9 connections) — `server/api/monitoring.py`
- **_resolve_cache_manager_from_request()** (9 connections) — `server/api/monitoring.py`
- **get_system_alerts()** (8 connections) — `server/api/monitoring.py`
- **reset_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (8 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (8 connections) — `server/api/monitoring.py`
- **force_memory_cleanup()** (8 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (8 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (8 connections) — `server/api/monitoring.py`
- *... and 82 more nodes in this community*

## Relationships

- [grace period login](grace_period_login.md) (20 shared connections)
- [Exception Containers](Exception_Containers.md) (18 shared connections)
- [System Metrics](System_Metrics.md) (13 shared connections)
- [npc population control](npc_population_control.md) (11 shared connections)
- [command combat models](command_combat_models.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [follow service game](follow_service_game.md) (2 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [message nats handler](message_nats_handler.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 576 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*