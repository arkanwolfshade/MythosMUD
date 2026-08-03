# npc spawn validator

> 37 nodes

## Key Concepts

- **ExceptionTracker** (23 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **Exception** (5 connections)
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **.add_exception_handler()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._update_stats()** (4 connections) — `server/monitoring/exception_tracker.py`
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
- **Initialize monitoring services. No dependencies.** (1 connections) — `server/container/bundles/monitoring.py`
- **Represents a tracked exception with full context.** (1 connections) — `server/monitoring/exception_tracker.py`
- **Comprehensive exception tracking system.      This class provides 100% exception** (1 connections) — `server/monitoring/exception_tracker.py`
- **Initialize the exception tracker.          Args:             max_records: Maximu** (1 connections) — `server/monitoring/exception_tracker.py`
- **Track an exception with full context information.          Args:             exc** (1 connections) — `server/monitoring/exception_tracker.py`
- **Get an exception record by ID.          Args:             exception_id: Unique e** (1 connections) — `server/monitoring/exception_tracker.py`
- *... and 12 more nodes in this community*

## Relationships

- [System Metrics](System_Metrics.md) (15 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [log structured logging](log_structured_logging.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/container/bundles/monitoring.py`
- `server/monitoring/exception_tracker.py`

## Audit Trail

- EXTRACTED: 117 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*