# StatisticsAggregator

> 110 nodes

## Key Concepts

- **StatisticsAggregator** (31 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **PerformanceTracker** (26 connections) — `server/realtime/monitoring/performance_tracker.py`
- **statistics_aggregator.py** (25 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_statistics_aggregator.py** (15 connections) — `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`
- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **.get_connection_health_stats()** (8 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._compose_memory_stats()** (7 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **server/realtime/monitoring/__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **MemoryStatsSnapshot** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_connections_section()** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (6 connections)
- **fixture** (6 connections)
- **._memory_sessions_section()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._safe_ratio()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_stats_response()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_trends()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._count_orphaned_connections()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **statistics_aggregator()** (4 connections) — `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`
- **.get_stats()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- *... and 85 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (17 shared connections)
- [build_event](build_event.md) (8 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (6 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 191 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*