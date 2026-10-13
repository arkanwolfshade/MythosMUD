# Community 428

> 41 nodes

## Key Concepts

- **test_memory_monitor.py** (35 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **MemoryMonitor** (33 connections) — `server/realtime/memory_monitor.py`
- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_enabled()** (5 connections) — `server/realtime/memory_monitor.py`
- **test_idle_sampler_interval_and_path()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_writes_jsonl_and_stops()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_collect_idle_sample_task_qualnames_attributes_by_coroutine()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_disabled_by_default()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_stays_stopped_when_disabled()** (4 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **asyncio** (4 connections)
- **MonkeyPatch** (4 connections)
- **.__init__()** (3 connections) — `server/realtime/memory_monitor.py`
- **.force_garbage_collection()** (2 connections) — `server/realtime/memory_monitor.py`
- **.stop_idle_sampler()** (2 connections) — `server/realtime/memory_monitor.py`
- **.update_cleanup_time()** (2 connections) — `server/realtime/memory_monitor.py`
- **test_force_garbage_collection_runtime_error()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_alerts()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_alerts_error_path()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_alerts_warning_and_info_levels()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_stats()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_stats_error_returns_empty()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_usage_error_returns_zero()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_usage_invalid_type()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_get_memory_usage_success()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_max_connection_age_default()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- *... and 16 more nodes in this community*

## Relationships

- [Community 551](Community_551.md) (8 shared connections)
- [Community 1074](Community_1074.md) (8 shared connections)
- [Community 1329](Community_1329.md) (3 shared connections)
- [Community 1274](Community_1274.md) (3 shared connections)
- [Connection Manager Broadcast](Connection_Manager_Broadcast.md) (2 shared connections)
- [Community 563](Community_563.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 91 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*