# IdleMemorySample

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

- [get_logger](get_logger.md) (4 shared connections)
- [collect_idle_memory_sample](collect_idle_memory_sample.md) (2 shared connections)
- [._run_idle_sampler](_run_idle_sampler.md) (1 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (1 shared connections)
- [.get_memory_alerts](get_memory_alerts.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*