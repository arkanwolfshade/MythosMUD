# StatisticsAggregator

> 28 nodes

## Key Concepts

- **StatisticsAggregator** (20 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_health_stats()** (9 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Any** (8 connections)
- **._build_health_stats_response()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_types()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_session_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_trends()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._calculate_session_health_percentages()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (3 connections)
- **.get_memory_alerts()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.__init__()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive connection statistics. Args: player_websockets: Player to…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection health distribution. Args: connection_metadata: Connection…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Aggregates statistics from connection management components. This class…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection types. Args: connection_metadata: Connection metadata…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection ages. Args: connection_metadata: Connection metadata now:…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze session health. Args: connection_metadata: Connection metadata Returns:…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Calculate session health percentages. Args: session_health: Session health…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Build health trends statistics. Args: connection_ages: List of connection ages…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Build connection health statistics response. Args: total_connections: Total…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Initialize the statistics aggregator. Args: memory_monitor: MemoryMonitor…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- *... and 3 more nodes in this community*

## Relationships

- [connection_initialization.py](connection_initialization.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_statistics_aggregator.py](test_statistics_aggregator.py.md) (2 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 49 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*