# UUID

> 9 nodes

## Key Concepts

- **._memory_connections_section()** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (6 connections)
- **._memory_sessions_section()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._safe_ratio()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._count_orphaned_connections()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Count active connections not tied to any online player.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Build the connections subsection of memory stats.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Build the sessions subsection of memory stats.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Return numerator/denominator, or 0 when denominator is empty.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [StatisticsAggregator](StatisticsAggregator.md) (4 shared connections)
- [._build_connection_stats](_build_connection_stats.md) (3 shared connections)
- [._compose_memory_stats](_compose_memory_stats.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*