# server realtime monitoring statistics aggregator

> 10 nodes

## Key Concepts

- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._connection_age_extrema()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._session_connection_distribution()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Count how many sessions have each connection-count size.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Return (avg, max, min) connection ages; zeros when the list is empty.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Compose connection statistics payload (extracted to keep get_connection_stats…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive connection statistics. Args: player_websockets: Player to…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection health distribution. Args: connection_metadata: Connection…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [server realtime monitoring statistics aggregator](server_realtime_monitoring_statistics_aggregator.md) (11 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*