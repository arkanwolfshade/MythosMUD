# server realtime monitoring statistics aggregator

> 19 nodes

## Key Concepts

- **StatisticsAggregator** (29 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_health_stats()** (8 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_stats_response()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_trends()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_types()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_session_health()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._calculate_session_health_percentages()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_alerts()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.__init__()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection types. Args: connection_metadata: Connection metadata…** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze session health. Args: connection_metadata: Connection metadata Returns:…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Calculate session health percentages. Args: session_health: Session health…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Build health trends statistics. Args: connection_ages: List of connection ages…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Build connection health statistics response. Args: total_connections: Total…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Aggregates statistics from connection management components. This class…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive connection health statistics. Args: connection_metadata:…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get memory-related alerts. Args: connection_timestamps: Connection timestamp…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Initialize the statistics aggregator. Args: memory_monitor: MemoryMonitor…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [server realtime monitoring statistics aggregator](server_realtime_monitoring_statistics_aggregator.md) (15 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server tests unit realtime monitoring](server_tests_unit_realtime_monitoring.md) (2 shared connections)
- [server realtime connection initialization initialize](server_realtime_connection_initialization_initialize.md) (1 shared connections)
- [server realtime monitoring performance tracker](server_realtime_monitoring_performance_tracker.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 45 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*