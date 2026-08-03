# health models rationale

> 63 nodes

## Key Concepts

- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (19 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (9 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (9 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (9 connections) — `server/api/monitoring.py`
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
- **test_dual_connection_and_performance_and_health_stats()** (6 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Any** (5 connections)
- **_resolve_task_registry()** (5 connections) — `server/api/monitoring.py`
- **_connection_manager_stub()** (5 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_memory_alerts_and_force_cleanup()** (5 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- *... and 38 more nodes in this community*

## Relationships

- [command combat models](command_combat_models.md) (45 shared connections)
- [Exception Containers](Exception_Containers.md) (15 shared connections)
- [grace period login](grace_period_login.md) (11 shared connections)
- [npc population control](npc_population_control.md) (9 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [player model models](player_model_models.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (1 shared connections)
- [System Metrics](System_Metrics.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 337 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*