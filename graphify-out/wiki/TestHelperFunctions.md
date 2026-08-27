# TestHelperFunctions

> 91 nodes

## Key Concepts

- **MemoryMonitor** (40 connections) — `server/realtime/memory_monitor.py`
- **memory_monitor.py** (35 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (32 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **collect_idle_memory_sample()** (13 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_path()** (7 connections) — `server/realtime/memory_monitor.py`
- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **._run_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **.start_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **_container_instance()** (6 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_interval_seconds()** (6 connections) — `server/realtime/memory_monitor.py`
- **ConnectionStatsSnapshot** (5 connections) — `server/realtime/memory_monitor.py`
- **IdleMemorySample** (5 connections) — `server/realtime/memory_monitor.py`
- **_append_sample_jsonl()** (5 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_enabled()** (5 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (5 connections) — `server/realtime/memory_monitor.py`
- **peek_log_aggregator()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **test_idle_sampler_interval_and_path()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_writes_jsonl_and_stops()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **AllocSiteSample** (4 connections) — `server/realtime/memory_monitor.py`
- **MemoryStatsSnapshot** (4 connections) — `server/realtime/memory_monitor.py`
- **_as_int()** (4 connections) — `server/realtime/memory_monitor.py`
- **_event_bus_queue_depth()** (4 connections) — `server/realtime/memory_monitor.py`
- **_log_hour_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **_npc_pending_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- *... and 66 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (17 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (3 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (3 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (2 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (2 shared connections)
- [test_message_handler_factory.py](test_message_handler_factory.py.md) (1 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/realtime/memory_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 185 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*