# StatisticsAggregator

> 117 nodes

## Key Concepts

- **StatisticsAggregator** (29 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **PerformanceTracker** (25 connections) — `server/realtime/monitoring/performance_tracker.py`
- **statistics_aggregator.py** (23 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **health_monitor.py** (16 connections) — `server/realtime/monitoring/health_monitor.py`
- **test_statistics_aggregator.py** (15 connections) — `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`
- **performance_tracker.py** (13 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **.get_connection_health_stats()** (8 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._compose_memory_stats()** (7 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **server/realtime/monitoring/__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **._memory_connections_section()** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (6 connections)
- **fixture** (6 connections)
- **MemoryStatsSnapshot** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_sessions_section()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._safe_ratio()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_stats_response()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_trends()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._count_orphaned_connections()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- *... and 92 more nodes in this community*

## Relationships

- [RoomSubscriptionManager](RoomSubscriptionManager.md) (12 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (4 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [test_health_monitor.py](test_health_monitor.py.md) (1 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (1 shared connections)
- [MessageQueue](MessageQueue.md) (1 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 203 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*