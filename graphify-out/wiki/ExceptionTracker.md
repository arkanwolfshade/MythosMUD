# ExceptionTracker

> 41 nodes

## Key Concepts

- **ExceptionTracker** (24 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **Exception** (7 connections)
- **ExceptionTrackInput** (6 connections) — `server/monitoring/exception_tracker.py`
- **._create_and_store_record()** (6 connections) — `server/monitoring/exception_tracker.py`
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **._log_tracked_exception()** (5 connections) — `server/monitoring/exception_tracker.py`
- **Any** (5 connections)
- **.add_exception_handler()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._parse_track_options()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._update_stats()** (4 connections) — `server/monitoring/exception_tracker.py`
- **.add_global_exception_handler()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_critical_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exception_record()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_correlation()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_type()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_user()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_recent_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_stats()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_unhandled_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.__init__()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.reset_records()** (3 connections) — `server/monitoring/exception_tracker.py`
- **Track an exception with full context information. Args: exception: The…** (1 connections) — `server/monitoring/exception_tracker.py`
- **Get an exception record by ID. Args: exception_id: Unique exception ID Returns:…** (1 connections) — `server/monitoring/exception_tracker.py`
- *... and 16 more nodes in this community*

## Relationships

- [MonitoringDashboard](MonitoringDashboard.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [testing_examples.py](testing_examples.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`

## Audit Trail

- EXTRACTED: 76 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*