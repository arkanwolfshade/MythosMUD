# Community 891

> 17 nodes

## Key Concepts

- **collect_idle_memory_sample()** (15 connections) — `server/realtime/memory_monitor.py`
- **_container_instance()** (6 connections) — `server/realtime/memory_monitor.py`
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

## Relationships

- [Community 42](Community_42.md) (7 shared connections)
- [Community 93](Community_93.md) (2 shared connections)
- [Community 1138](Community_1138.md) (2 shared connections)
- [Community 730](Community_730.md) (2 shared connections)
- [Community 1240](Community_1240.md) (1 shared connections)
- [Community 1301](Community_1301.md) (1 shared connections)
- [Community 931](Community_931.md) (1 shared connections)
- [Community 1306](Community_1306.md) (1 shared connections)
- [Community 205](Community_205.md) (1 shared connections)
- [Community 239](Community_239.md) (1 shared connections)
- [Database Manager](Database_Manager.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*