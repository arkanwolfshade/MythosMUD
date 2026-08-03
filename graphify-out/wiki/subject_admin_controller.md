# subject admin controller

> 9 nodes

## Key Concepts

- **._compose_memory_stats()** (7 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **MemoryStatsSnapshot** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_monitor_config_section()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **TypedDict** (1 connections)
- **Connection-manager snapshot consumed by get_memory_stats.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive memory and connection statistics.          Args:             s** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Assemble memory stats from a snapshot dict (keeps call sites param-stable).** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Expose memory monitor configuration knobs for stats payload.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [target services resolution](target_services_resolution.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [player game schema](player_game_schema.md) (2 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 24 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*