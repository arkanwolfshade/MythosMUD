# npc population control

> 46 nodes

## Key Concepts

- **MovementMonitor** (21 connections) — `server/game/movement_monitor.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **validate_room_integrity()** (9 connections) — `server/api/monitoring.py`
- **get_system_alerts()** (8 connections) — `server/api/monitoring.py`
- **reset_metrics()** (8 connections) — `server/api/monitoring.py`
- **reset_movement_monitor()** (8 connections) — `server/game/movement_monitor.py`
- **.get_metrics()** (6 connections) — `server/game/movement_monitor.py`
- **.get_alerts()** (6 connections) — `server/game/movement_monitor.py`
- **.get_performance_summary()** (5 connections) — `server/game/movement_monitor.py`
- **.record_movement_attempt()** (4 connections) — `server/game/movement_monitor.py`
- **.validate_room_integrity()** (4 connections) — `server/game/movement_monitor.py`
- **._check_alerts()** (4 connections) — `server/game/movement_monitor.py`
- **.log_performance_summary()** (4 connections) — `server/game/movement_monitor.py`
- **test_reset_movement_monitor()** (4 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **.__init__()** (3 connections) — `server/game/movement_monitor.py`
- **.record_integrity_check()** (3 connections) — `server/game/movement_monitor.py`
- **Any** (3 connections)
- **.reset_metrics()** (3 connections) — `server/game/movement_monitor.py`
- **test_validate_room_integrity_builds_room_map()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_system_alerts_returns_counts()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **movement_monitor()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_movement_monitor_returns_singleton()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **MessageResponse** (2 connections)
- **UUID** (2 connections)
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- *... and 21 more nodes in this community*

## Relationships

- [command combat models](command_combat_models.md) (12 shared connections)
- [health models rationale](health_models_rationale.md) (9 shared connections)
- [player model models](player_model_models.md) (6 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [Exception Containers](Exception_Containers.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [schedule services service](schedule_services_service.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 157 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*