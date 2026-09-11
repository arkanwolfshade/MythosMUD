# MemoryMonitor

> 108 nodes

## Key Concepts

- **MemoryMonitor** (39 connections) — `server/realtime/memory_monitor.py`
- **memory_monitor.py** (37 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (35 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **collect_idle_memory_sample()** (15 connections) — `server/realtime/memory_monitor.py`
- **get_engine()** (9 connections) — `server/database.py`
- **._run_idle_sampler()** (8 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_path()** (7 connections) — `server/realtime/memory_monitor.py`
- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **.start_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **_container_instance()** (6 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_interval_seconds()** (6 connections) — `server/realtime/memory_monitor.py`
- **_task_qualname()** (6 connections) — `server/realtime/memory_monitor.py`
- **ConnectionStatsSnapshot** (5 connections) — `server/realtime/memory_monitor.py`
- **IdleMemorySample** (5 connections) — `server/realtime/memory_monitor.py`
- **peek_performance_monitor()** (5 connections) — `server/monitoring/performance_monitor.py`
- **_append_sample_jsonl()** (5 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_enabled()** (5 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (5 connections) — `server/realtime/memory_monitor.py`
- **peek_log_aggregator()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **test_idle_sampler_interval_and_path()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_writes_jsonl_and_stops()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **AllocSiteSample** (4 connections) — `server/realtime/memory_monitor.py`
- **MemoryStatsSnapshot** (4 connections) — `server/realtime/memory_monitor.py`
- **_FakeTask** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **_as_int()** (4 connections) — `server/realtime/memory_monitor.py`
- *... and 83 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (2 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (2 shared connections)
- [LogAggregator](LogAggregator.md) (2 shared connections)
- [time.py](time.py.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/database.py`
- `server/monitoring/performance_monitor.py`
- `server/realtime/memory_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 214 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*