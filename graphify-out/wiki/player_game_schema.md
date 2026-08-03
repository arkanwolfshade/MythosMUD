# player game schema

> 9 nodes

## Key Concepts

- **UUID** (6 connections)
- **._memory_connections_section()** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_sessions_section()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._safe_ratio()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._count_orphaned_connections()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Count active connections not tied to any online player.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Build the connections subsection of memory stats.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Build the sessions subsection of memory stats.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Return numerator/denominator, or 0 when denominator is empty.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [target services resolution](target_services_resolution.md) (4 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (3 shared connections)
- [subject admin controller](subject_admin_controller.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 30 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*