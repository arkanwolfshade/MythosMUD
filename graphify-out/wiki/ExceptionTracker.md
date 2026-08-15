# ExceptionTracker

> 51 nodes

## Key Concepts

- **ExceptionTracker** (30 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **test_exception_tracker.py** (12 connections) — `server/tests/unit/monitoring/test_exception_tracker.py`
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
- **test_reset_records_and_module_helper()** (3 connections) — `server/tests/unit/monitoring/test_exception_tracker.py`
- *... and 26 more nodes in this community*

## Relationships

- [MonitoringDashboard](MonitoringDashboard.md) (12 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`
- `server/tests/unit/monitoring/test_exception_tracker.py`

## Audit Trail

- EXTRACTED: 91 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*