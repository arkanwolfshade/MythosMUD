# health monitor realtime

> 68 nodes

## Key Concepts

- **test_health_monitor.py** (26 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **HealthMonitor** (22 connections) — `server/realtime/monitoring/health_monitor.py`
- **UUID** (9 connections)
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._wait_for_task_cancellation()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_connection_stale()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._check_websocket_open()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **._validate_and_update_token()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **.stop_periodic_checks()** (3 connections) — `server/realtime/monitoring/health_monitor.py`
- **health_monitor()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_health_monitor_init_custom_intervals()** (3 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **Any** (2 connections)
- **mock_is_websocket_open()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_validate_token()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_cleanup_dead_websocket()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **mock_performance_tracker()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_health_monitor_init()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- **test_check_player_connection_health()** (2 connections) — `server/tests/unit/realtime/monitoring/test_health_monitor.py`
- *... and 43 more nodes in this community*

## Relationships

- [services chat logger](services_chat_logger.md) (5 shared connections)
- [services npc startup](services_npc_startup.md) (2 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/health_monitor.py`
- `server/tests/unit/realtime/monitoring/test_health_monitor.py`

## Audit Trail

- EXTRACTED: 179 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*