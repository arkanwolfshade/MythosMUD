# Community 1138

> 11 nodes

## Key Concepts

- **IdleMemorySample** (5 connections) — `server/realtime/memory_monitor.py`
- **AllocSiteSample** (4 connections) — `server/realtime/memory_monitor.py`
- **MemoryStatsSnapshot** (4 connections) — `server/realtime/memory_monitor.py`
- **_top_alloc_sites()** (4 connections) — `server/realtime/memory_monitor.py`
- **TypedDict** (4 connections)
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
- **Return the largest allocation sites. File:line and size only.** (1 connections) — `server/realtime/memory_monitor.py`
- **Get detailed memory statistics. Returns: dict: Memory statistics including RSS,…** (1 connections) — `server/realtime/memory_monitor.py`
- **Count-only allocation site (no object payloads).** (1 connections) — `server/realtime/memory_monitor.py`
- **Bounded idle-memory snapshot. Counts only; no player or SQL payloads.** (1 connections) — `server/realtime/memory_monitor.py`
- **Process memory counters exposed to connection stats.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [Community 42](Community_42.md) (5 shared connections)
- [Community 891](Community_891.md) (2 shared connections)
- [Community 931](Community_931.md) (1 shared connections)
- [Community 730](Community_730.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*