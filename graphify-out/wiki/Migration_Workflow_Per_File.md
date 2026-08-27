# Migration Workflow (Per File)

> 9 nodes

## Key Concepts

- **._compose_memory_stats()** (7 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **MemoryStatsSnapshot** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_monitor_config_section()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **TypedDict** (1 connections)
- **Assemble memory stats from a snapshot dict (keeps call sites param-stable).** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Expose memory monitor configuration knobs for stats payload.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Connection-manager snapshot consumed by get_memory_stats.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive memory and connection statistics. Args: snap: Connection-…** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [_find_dead_connections](_find_dead_connections.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [Security Implementation](Security_Implementation.md) (2 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*