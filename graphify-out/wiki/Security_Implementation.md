# Security Implementation

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

- [_find_dead_connections](_find_dead_connections.md) (4 shared connections)
- [Step 2: Ask UX-Focused Questions](Step_2-_Ask_UX-Focused_Questions.md) (3 shared connections)
- [Migration Workflow (Per File)](Migration_Workflow_Per_File.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*