# StatisticsAggregator

> 18 nodes

## Key Concepts

- **StatisticsAggregator** (31 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._connection_age_extrema()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._session_connection_distribution()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_alerts()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.__init__()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Count how many sessions have each connection-count size.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Return (avg, max, min) connection ages; zeros when the list is empty.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Compose connection statistics payload (extracted to keep get_connection_stats…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive connection statistics. Args: player_websockets: Player to…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection health distribution. Args: connection_metadata: Connection…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection ages. Args: connection_metadata: Connection metadata now:…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get memory-related alerts. Args: connection_timestamps: Connection timestamp…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Aggregates statistics from connection management components. This class…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Initialize the statistics aggregator. Args: memory_monitor: MemoryMonitor…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [connection_manager.py](connection_manager.py.md) (7 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [.get_connection_health_stats](get_connection_health_stats.md) (6 shared connections)
- [._compose_memory_stats](_compose_memory_stats.md) (3 shared connections)
- [._build_health_stats_response](_build_health_stats_response.md) (3 shared connections)
- [test_statistics_aggregator.py](test_statistics_aggregator.py.md) (2 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 48 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*