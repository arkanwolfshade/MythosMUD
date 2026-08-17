# ExceptionTracker

> 57 nodes

## Key Concepts

- **ExceptionTracker** (30 connections) — `server/monitoring/exception_tracker.py`
- **track_exception()** (15 connections) — `server/monitoring/exception_tracker.py`
- **test_exception_tracker.py** (13 connections) — `server/tests/unit/monitoring/test_exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_exception_tracker()** (12 connections) — `server/monitoring/exception_tracker.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **Exception** (7 connections)
- **ExceptionTrackInput** (6 connections) — `server/monitoring/exception_tracker.py`
- **._create_and_store_record()** (6 connections) — `server/monitoring/exception_tracker.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
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
- *... and 32 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (6 shared connections)
- [ErrorContext](ErrorContext.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (2 shared connections)
- [testing_examples.py](testing_examples.py.md) (2 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [bind_request_context](bind_request_context.md) (1 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [LogAggregator](LogAggregator.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/monitoring/test_exception_tracker.py`

## Audit Trail

- EXTRACTED: 116 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*