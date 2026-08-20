# ExceptionTracker

> 64 nodes

## Key Concepts

- **ExceptionTracker** (30 connections) — `server/monitoring/exception_tracker.py`
- **exception_tracker.py** (21 connections) — `server/monitoring/exception_tracker.py`
- **track_exception()** (15 connections) — `server/monitoring/exception_tracker.py`
- **test_exception_tracker.py** (13 connections) — `server/tests/unit/monitoring/test_exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_exception_tracker()** (12 connections) — `server/monitoring/exception_tracker.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **Exception** (7 connections)
- **ExceptionTrackInput** (6 connections) — `server/monitoring/exception_tracker.py`
- **._create_and_store_record()** (6 connections) — `server/monitoring/exception_tracker.py`
- **track_exception_with_context()** (6 connections) — `server/monitoring/exception_tracker.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **._log_tracked_exception()** (5 connections) — `server/monitoring/exception_tracker.py`
- **Any** (5 connections)
- **ExceptionContextTrackInput** (4 connections) — `server/monitoring/exception_tracker.py`
- **.add_exception_handler()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._parse_track_options()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._update_stats()** (4 connections) — `server/monitoring/exception_tracker.py`
- **.add_global_exception_handler()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_critical_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exception_record()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_correlation()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_type()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_user()** (3 connections) — `server/monitoring/exception_tracker.py`
- *... and 39 more nodes in this community*

## Relationships

- [PerformanceMonitor](PerformanceMonitor.md) (9 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [testing_examples.py](testing_examples.py.md) (3 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (2 shared connections)
- [LogAggregator](LogAggregator.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/monitoring/test_exception_tracker.py`

## Audit Trail

- EXTRACTED: 141 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*