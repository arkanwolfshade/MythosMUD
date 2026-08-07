# nats exceptions services

> 86 nodes

## Key Concepts

- **test_movement_monitor.py** (33 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **MovementMonitor** (21 connections) — `server/game/movement_monitor.py`
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
- **test_get_movement_monitor_returns_singleton()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **UUID** (2 connections)
- **.record_concurrent_movement()** (2 connections) — `server/game/movement_monitor.py`
- **sample_player_id()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_movement_monitor_init()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_success()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_failure()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_string_player_id()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_uuid_player_id()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- *... and 61 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (14 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)

## Source Files

- `server/game/movement_monitor.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 213 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*