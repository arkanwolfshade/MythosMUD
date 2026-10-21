# NATSSubjectManager

> 106 nodes · cohesion 0.03

## Key Concepts

- **MemoryMonitor** (39 connections) — `server/realtime/memory_monitor.py`
- **memory_monitor.py** (37 connections) — `server/realtime/memory_monitor.py`
- **test_memory_monitor.py** (35 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **collect_idle_memory_sample()** (15 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_path()** (7 connections) — `server/realtime/memory_monitor.py`
- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **._run_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **.start_idle_sampler()** (7 connections) — `server/realtime/memory_monitor.py`
- **_container_instance()** (6 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_interval_seconds()** (6 connections) — `server/realtime/memory_monitor.py`
- **_task_qualname()** (6 connections) — `server/realtime/memory_monitor.py`
- **peek_performance_monitor()** (5 connections) — `server/monitoring/performance_monitor.py`
- **_append_sample_jsonl()** (5 connections) — `server/realtime/memory_monitor.py`
- **ConnectionStatsSnapshot** (5 connections) — `server/realtime/memory_monitor.py`
- **idle_sampler_enabled()** (5 connections) — `server/realtime/memory_monitor.py`
- **IdleMemorySample** (5 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (5 connections) — `server/realtime/memory_monitor.py`
- **peek_log_aggregator()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **test_idle_sampler_interval_and_path()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **test_idle_sampler_writes_jsonl_and_stops()** (5 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **AllocSiteSample** (4 connections) — `server/realtime/memory_monitor.py`
- **_as_int()** (4 connections) — `server/realtime/memory_monitor.py`
- **_event_bus_queue_depth()** (4 connections) — `server/realtime/memory_monitor.py`
- **_log_hour_key_count()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- *... and 81 more nodes in this community*

## Relationships

- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (8 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (4 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (3 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (2 shared connections)
- [ItemFactory](ItemFactory.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (2 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (2 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/monitoring/performance_monitor.py`
- `server/realtime/memory_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 207 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*