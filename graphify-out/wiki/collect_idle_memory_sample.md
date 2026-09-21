# collect_idle_memory_sample

> 19 nodes

## Key Concepts

- **collect_idle_memory_sample()** (15 connections) — `server/realtime/memory_monitor.py`
- **_container_instance()** (6 connections) — `server/realtime/memory_monitor.py`
- **IdleMemorySample** (5 connections) — `server/realtime/memory_monitor.py`
- **_event_bus_queue_depth()** (4 connections) — `server/realtime/memory_monitor.py`
- **_log_hour_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **_npc_pending_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **_perf_metric_counts()** (4 connections) — `server/realtime/memory_monitor.py`
- **_sqlalchemy_pool_counts()** (4 connections) — `server/realtime/memory_monitor.py`
- **.peek_instance()** (3 connections) — `server/container/main.py`
- **test_collect_idle_sample_shape()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **Return the live singleton without constructing one.** (1 connections) — `server/container/main.py`
- **Return the live container without constructing a new singleton.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return EventBus queue depth, or -1 when the bus is unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return pending-message dictionary key count, or -1 when unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return (primary metrics, operation keys, retained operation metrics).** (1 connections) — `server/realtime/memory_monitor.py`
- **Return log-aggregator hourly bucket count, or -1 when unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return (pool_size, checkedout, overflow), or (-1, -1, -1) when unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Collect a count-based idle sample after a GC pass. No user payloads.** (1 connections) — `server/realtime/memory_monitor.py`
- **Bounded idle-memory snapshot. Counts only; no player or SQL payloads.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [connection_manager.py](connection_manager.py.md) (10 shared connections)
- [._run_idle_sampler](_run_idle_sampler.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (2 shared connections)
- [_task_qualname](_task_qualname.md) (1 shared connections)
- [.get_memory_alerts](get_memory_alerts.md) (1 shared connections)
- [idle_sampler_enabled](idle_sampler_enabled.md) (1 shared connections)
- [LogAggregator](LogAggregator.md) (1 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*