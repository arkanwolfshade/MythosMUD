# Statistics Aggregator

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

- [Statistics Aggregator](Statistics_Aggregator.md) (15 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [Test Statistics Aggregator](Test_Statistics_Aggregator.md) (2 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 45 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*