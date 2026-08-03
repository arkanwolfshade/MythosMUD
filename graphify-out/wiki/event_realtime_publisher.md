# event realtime publisher

> 144 nodes

## Key Concepts

- **StatisticsAggregator** (29 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **PerformanceTracker** (25 connections) — `server/realtime/monitoring/performance_tracker.py`
- **HealthMonitor** (22 connections) — `server/realtime/monitoring/health_monitor.py`
- **health_monitor.py** (14 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_statistics_aggregator.py** (14 connections) — `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`
- **performance_tracker.py** (11 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (9 connections)
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **._process_single_connection()** (8 connections) — `server/realtime/monitoring/health_monitor.py`
- **.get_connection_health_stats()** (8 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._compose_memory_stats()** (7 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.check_all_connections_health()** (6 connections) — `server/realtime/monitoring/health_monitor.py`
- **MemoryStatsSnapshot** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (6 connections)
- **._memory_connections_section()** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.periodic_health_check_task()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **.start_periodic_checks()** (5 connections) — `server/realtime/monitoring/health_monitor.py`
- **._memory_sessions_section()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._safe_ratio()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.check_player_connection_health()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._find_player_id_for_cleanup()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- **._cleanup_stale_connections()** (4 connections) — `server/realtime/monitoring/health_monitor.py`
- *... and 119 more nodes in this community*

## Relationships

- [connection disconnection realtime](connection_disconnection_realtime.md) (17 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [health monitor realtime](health_monitor_realtime.md) (4 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (2 shared connections)

## Source Files

- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 437 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*