# MemoryMonitor

> 89 nodes

## Key Concepts

- **MemoryMonitor** (39 connections) — `server/realtime/memory_monitor.py`
- **memory_monitor.py** (37 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (32 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **collect_idle_memory_sample()** (13 connections) — `server/realtime/memory_monitor.py`
- **._run_idle_sampler()** (8 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_path()** (7 connections) — `server/realtime/memory_monitor.py`
- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **.start_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **_container_instance()** (6 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_interval_seconds()** (6 connections) — `server/realtime/memory_monitor.py`
- **ConnectionStatsSnapshot** (5 connections) — `server/realtime/memory_monitor.py`
- **IdleMemorySample** (5 connections) — `server/realtime/memory_monitor.py`
- **_append_sample_jsonl()** (5 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_enabled()** (5 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (5 connections) — `server/realtime/memory_monitor.py`
- **test_idle_sampler_interval_and_path()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_writes_jsonl_and_stops()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **AllocSiteSample** (4 connections) — `server/realtime/memory_monitor.py`
- **MemoryStatsSnapshot** (4 connections) — `server/realtime/memory_monitor.py`
- **_as_int()** (4 connections) — `server/realtime/memory_monitor.py`
- **_event_bus_queue_depth()** (4 connections) — `server/realtime/memory_monitor.py`
- **_log_hour_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **_npc_pending_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **_perf_metric_counts()** (4 connections) — `server/realtime/memory_monitor.py`
- *... and 64 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (10 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [LogAggregator](LogAggregator.md) (2 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 184 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*