# nats retry handler

> 44 nodes

## Key Concepts

- **ExceptionTracker** (23 connections) — `server/monitoring/exception_tracker.py`
- **track_exception()** (15 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **track_exception_with_context()** (8 connections) — `server/monitoring/exception_tracker.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **Exception** (5 connections)
- **Any** (5 connections)
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **.add_exception_handler()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._update_stats()** (4 connections) — `server/monitoring/exception_tracker.py`
- **test_exception_tracking()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **.__init__()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exception_record()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_type()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_user()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_correlation()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_unhandled_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_critical_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_recent_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_stats()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.add_global_exception_handler()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.reset_records()** (3 connections) — `server/monitoring/exception_tracker.py`
- **Test exception tracking functionality.** (1 connections) — `docs/examples/logging/testing_examples.py`
- **Initialize monitoring services. No dependencies.** (1 connections) — `server/container/bundles/monitoring.py`
- *... and 19 more nodes in this community*

## Relationships

- [PerformanceStats](PerformanceStats.md) (11 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [testing examples](testing_examples.md) (2 shared connections)
- [item](item.md) (2 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (2 shared connections)
- [websocket integration](websocket_integration.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [. is npc in combat()](_is_npc_in_combat%28%29.md) (1 shared connections)
- [aggregate log entry()](aggregate_log_entry%28%29.md) (1 shared connections)
- [world](world.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `docs/examples/logging/testing_examples.py`
- `server/container/bundles/monitoring.py`
- `server/monitoring/exception_tracker.py`

## Audit Trail

- EXTRACTED: 151 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*