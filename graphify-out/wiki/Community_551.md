# Community 551

> 31 nodes

## Key Concepts

- **memory_monitor.py** (37 connections) — `server/realtime/memory_monitor.py`
- **collect_idle_memory_sample()** (15 connections) — `server/realtime/memory_monitor.py`
- **_container_instance()** (6 connections) — `server/realtime/memory_monitor.py`
- **IdleMemorySample** (5 connections) — `server/realtime/memory_monitor.py`
- **AllocSiteSample** (4 connections) — `server/realtime/memory_monitor.py`
- **MemoryStatsSnapshot** (4 connections) — `server/realtime/memory_monitor.py`
- **_as_int()** (4 connections) — `server/realtime/memory_monitor.py`
- **_event_bus_queue_depth()** (4 connections) — `server/realtime/memory_monitor.py`
- **_log_hour_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **_npc_pending_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **_perf_metric_counts()** (4 connections) — `server/realtime/memory_monitor.py`
- **_sqlalchemy_pool_counts()** (4 connections) — `server/realtime/memory_monitor.py`
- **_top_alloc_sites()** (4 connections) — `server/realtime/memory_monitor.py`
- **TypedDict** (4 connections)
- **.peek_instance()** (3 connections) — `server/container/main.py`
- **.get_memory_stats()** (3 connections) — `server/realtime/memory_monitor.py`
- **test_collect_idle_sample_shape()** (2 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **Return the live singleton without constructing one.** (1 connections) — `server/container/main.py`
- **Coerce a duck-typed counter to int without using typing.Any.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return the live container without constructing a new singleton.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return EventBus queue depth, or -1 when the bus is unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return pending-message dictionary key count, or -1 when unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return (primary metrics, operation keys, retained operation metrics).** (1 connections) — `server/realtime/memory_monitor.py`
- **Return log-aggregator hourly bucket count, or -1 when unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- **Return (pool_size, checkedout, overflow), or (-1, -1, -1) when unavailable.** (1 connections) — `server/realtime/memory_monitor.py`
- *... and 6 more nodes in this community*

## Relationships

- [Community 428](Community_428.md) (8 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (8 shared connections)
- [Community 1074](Community_1074.md) (5 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (3 shared connections)
- [Community 1329](Community_1329.md) (3 shared connections)
- [Community 1274](Community_1274.md) (2 shared connections)
- [Community 211](Community_211.md) (2 shared connections)
- [Community 285](Community_285.md) (2 shared connections)
- [Core Bundle & DB Init](Core_Bundle_&_DB_Init.md) (2 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (1 shared connections)
- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (1 shared connections)
- [Community 563](Community_563.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/realtime/memory_monitor.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 82 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*