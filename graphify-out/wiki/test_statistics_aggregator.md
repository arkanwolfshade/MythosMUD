# test statistics aggregator

> 99 nodes

## Key Concepts

- **StatisticsAggregator** (29 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **statistics_aggregator.py** (22 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **PerformanceTracker** (18 connections) — `server/realtime/monitoring/performance_tracker.py`
- **test_statistics_aggregator.py** (14 connections) — `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_health_stats()** (8 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._compose_memory_stats()** (7 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **MemoryStatsSnapshot** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (6 connections)
- **._memory_connections_section()** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_sessions_section()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._safe_ratio()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._count_orphaned_connections()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_trends()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_stats_response()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.record_connection_establishment()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_message_delivery()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_disconnection()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- *... and 74 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (14 shared connections)
- [test connection cleaner](test_connection_cleaner.md) (4 shared connections)
- [mock async persistence()](mock_async_persistence%28%29.md) (2 shared connections)
- [nats config()](nats_config%28%29.md) (2 shared connections)
- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [GameConfig](GameConfig.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [connection disconnection](connection_disconnection.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 304 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*