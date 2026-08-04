# health models rationale

> 70 nodes

## Key Concepts

- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (19 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
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
- **get_task_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (8 connections) — `server/api/monitoring.py`
- **test_dual_connection_and_performance_and_health_stats()** (6 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Any** (5 connections)
- *... and 45 more nodes in this community*

## Relationships

- [command combat models](command_combat_models.md) (41 shared connections)
- [Exception Containers](Exception_Containers.md) (17 shared connections)
- [grace period login](grace_period_login.md) (11 shared connections)
- [npc population control](npc_population_control.md) (9 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [player model models](player_model_models.md) (2 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (1 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 369 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*