# Cursor Subagents Docs

> 26 nodes

## Key Concepts

- **test_movement_monitor.py** (33 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **sample_player_id()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_failure()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_string_player_id()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_movement_attempt_uuid_player_id()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_concurrent_movement()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_record_integrity_check_no_violation()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_validate_room_integrity_duplicate_players()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_validate_room_integrity_empty_rooms()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_metrics_empty()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_get_alerts_high_concurrent()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_reset_metrics()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_log_performance_summary()** (2 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Unit tests for movement monitor.  Tests the MovementMonitor class for monitoring** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Create a sample player ID.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test record_movement_attempt() records failed movement.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test record_movement_attempt() handles string player_id.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test record_movement_attempt() handles UUID player_id.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test record_concurrent_movement() updates concurrent count.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test record_integrity_check() records check without violation.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test validate_room_integrity() detects duplicate players.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test validate_room_integrity() handles empty rooms dict.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test get_metrics() returns metrics for empty monitor.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test get_alerts() alerts on high concurrent movements.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **Test reset_metrics() resets all metrics.** (1 connections) — `server/tests/unit/game/test_movement_monitor.py`
- *... and 1 more nodes in this community*

## Relationships

- [Monitoring Response Models](Monitoring_Response_Models.md) (4 shared connections)
- [Movement Performance Monitor](Movement_Performance_Monitor.md) (1 shared connections)
- [test_profession_meets_stat_requirements_invalid_json](test_profession_meets_stat_requirements_invalid_json.md) (1 shared connections)
- [test_get_alerts_high_failure_rate](test_get_alerts_high_failure_rate.md) (1 shared connections)
- [test_get_alerts_no_alerts](test_get_alerts_no_alerts.md) (1 shared connections)
- [test_get_alerts_slow_movement_time](test_get_alerts_slow_movement_time.md) (1 shared connections)
- [test_get_metrics_integrity_rate](test_get_metrics_integrity_rate.md) (1 shared connections)
- [test_get_metrics_with_data](test_get_metrics_with_data.md) (1 shared connections)
- [test_get_movement_monitor_returns_singleton](test_get_movement_monitor_returns_singleton.md) (1 shared connections)
- [test_movement_monitor_init](test_movement_monitor_init.md) (1 shared connections)
- [test_record_concurrent_movement_updates_max](test_record_concurrent_movement_updates_max.md) (1 shared connections)
- [test_record_integrity_check_with_violation](test_record_integrity_check_with_violation.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 70 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*