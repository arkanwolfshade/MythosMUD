# npc population control

> 34 nodes

## Key Concepts

- **MovementMonitor** (21 connections) — `server/game/movement_monitor.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
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
- **movement_monitor()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **UUID** (2 connections)
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **Movement monitoring and validation system for MythosMUD.  This module provides c** (1 connections) — `server/game/movement_monitor.py`
- **Comprehensive monitoring system for the movement system.      This class provide** (1 connections) — `server/game/movement_monitor.py`
- **Initialize the movement monitor with empty metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Record a movement attempt with metrics.** (1 connections) — `server/game/movement_monitor.py`
- **Record concurrent movement count.** (1 connections) — `server/game/movement_monitor.py`
- **Record an integrity check result.** (1 connections) — `server/game/movement_monitor.py`
- **Validate room data integrity.          Returns a dictionary with validation resu** (1 connections) — `server/game/movement_monitor.py`
- *... and 9 more nodes in this community*

## Relationships

- [health models rationale](health_models_rationale.md) (9 shared connections)
- [player model models](player_model_models.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [command combat models](command_combat_models.md) (2 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/game/movement_monitor.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 113 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*