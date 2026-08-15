# MemoryMonitor

> 37 nodes

## Key Concepts

- **MemoryMonitor** (27 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (21 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
- **.__init__()** (3 connections) — `server/realtime/memory_monitor.py`
- **.should_cleanup()** (3 connections) — `server/realtime/memory_monitor.py`
- **.force_garbage_collection()** (2 connections) — `server/realtime/memory_monitor.py`
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
- **test_max_connection_age_e2e()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_max_connection_age_local()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_should_cleanup_memory_threshold()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_should_cleanup_returns_false()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_should_cleanup_time_based()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- *... and 12 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 50 (78%)
- INFERRED: 14 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*