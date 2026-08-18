# server realtime memory monitor collect

> 15 nodes

## Key Concepts

- **collect_idle_memory_sample()** (13 connections) — `server/realtime/memory_monitor.py`
- **IdleMemorySample** (5 connections) — `server/realtime/memory_monitor.py`
- **_event_bus_queue_depth()** (4 connections) — `server/realtime/memory_monitor.py`
- **_log_hour_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **_npc_pending_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **_perf_metric_counts()** (4 connections) — `server/realtime/memory_monitor.py`
- **_sqlalchemy_pool_counts()** (4 connections) — `server/realtime/memory_monitor.py`
- **test_collect_idle_sample_shape()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **Return EventBus queue depth, or -1 when the bus is unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return pending-message dictionary key count, or -1 when unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return (primary metrics, operation keys, retained operation metrics).** (1 connections) — `server/realtime/memory_monitor.py`
- **Return log-aggregator hourly bucket count, or -1 when unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return (pool_size, checkedout, overflow), or (-1, -1, -1) when unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Collect a count-based idle sample after a GC pass. No user payloads.** (1 connections) — `server/realtime/memory_monitor.py`
- **Bounded idle-memory snapshot. Counts only; no player or SQL payloads.** (1 connections) — `server/realtime/memory_monitor.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server realtime memory monitor append](server_realtime_memory_monitor_append.md) (2 shared connections)
- [server realtime memory monitor memorymonitor](server_realtime_memory_monitor_memorymonitor.md) (2 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (2 shared connections)
- [server realtime memory monitor as](server_realtime_memory_monitor_as.md) (1 shared connections)
- [logentry](logentry.md) (1 shared connections)
- [server monitoring monitoring dashboard monitoringdashboard](server_monitoring_monitoring_dashboard_monitoringdashboard.md) (1 shared connections)
- [server database close db](server_database_close_db.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*