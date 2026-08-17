# server realtime monitoring statistics aggregator

> 9 nodes

## Key Concepts

- **._compose_memory_stats()** (7 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **MemoryStatsSnapshot** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_monitor_config_section()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **TypedDict** (1 connections)
- **Assemble memory stats from a snapshot dict (keeps call sites param-stable).** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Expose memory monitor configuration knobs for stats payload.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Connection-manager snapshot consumed by get_memory_stats.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive memory and connection statistics. Args: snap: Connection-…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [server realtime monitoring statistics aggregator](server_realtime_monitoring_statistics_aggregator.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*