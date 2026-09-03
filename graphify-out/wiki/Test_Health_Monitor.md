# Test Health Monitor

> 11 nodes

## Key Concepts

- **fixture** (5 connections)
- **health_monitor()** (4 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_cleanup_dead_websocket()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_is_websocket_open()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_performance_tracker()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_validate_token()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a mock is_websocket_open callback.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a mock validate_token callback.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a mock cleanup_dead_websocket callback.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a mock performance tracker.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Create a HealthMonitor instance.** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Relationships

- [Test Health Monitor](Test_Health_Monitor.md) (5 shared connections)
- [Health Monitor](Health_Monitor.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 15 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*