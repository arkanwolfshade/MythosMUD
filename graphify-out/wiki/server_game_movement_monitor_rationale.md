# server game movement monitor rationale

> 60 nodes

## Key Concepts

- **test_movement_monitor.py** (34 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **reset_movement_monitor()** (7 connections) — `server/game/movement_monitor.py`
- **movement_monitor()** (4 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_reset_movement_monitor()** (4 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **sample_player_id()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_movement_monitor_returns_singleton()** (3 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_alerts_high_concurrent()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_alerts_high_failure_rate()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_alerts_no_alerts()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_alerts_slow_movement_time()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_metrics_empty()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_metrics_integrity_rate()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_metrics_with_data()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_log_performance_summary()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_movement_monitor_init()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_concurrent_movement()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_concurrent_movement_updates_max()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_integrity_check_no_violation()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_integrity_check_with_violation()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_failure()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_multiple_players()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_string_player_id()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_success()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_uuid_player_id()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_reset_metrics()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- *... and 35 more nodes in this community*

## Relationships

- [server api monitoring](server_api_monitoring.md) (7 shared connections)
- [server game movement monitor movementmonitor](server_game_movement_monitor_movementmonitor.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/game/movement_monitor.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 72 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*