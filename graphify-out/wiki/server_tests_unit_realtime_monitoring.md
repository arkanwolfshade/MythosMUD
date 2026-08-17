# server tests unit realtime monitoring

> 40 nodes

## Key Concepts

- **test_health_monitor.py** (27 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **asyncio** (12 connections)
- **fixture** (5 connections)
- **health_monitor()** (4 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_cleanup_dead_websocket()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_is_websocket_open()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_performance_tracker()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_validate_token()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_all_connections_health()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health_no_websockets()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health_unhealthy()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_health_monitor_init_custom_intervals()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_start_periodic_checks()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_stop_periodic_checks()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_all_connections_health_with_metadata()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_cleanup_stale_connections()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_health_monitor_init()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_periodic_health_check_task_cancel()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_process_single_connection_paths()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_validate_and_update_token()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_wait_for_task_cancellation()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_connection_stale()** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_websocket_open()** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_find_player_id_for_cleanup()** (1 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- *... and 15 more nodes in this community*

## Relationships

- [server realtime monitoring health monitor](server_realtime_monitoring_health_monitor.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 57 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*