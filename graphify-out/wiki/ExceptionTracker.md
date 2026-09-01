# ExceptionTracker

> 75 nodes

## Key Concepts

- **ExceptionTracker** (30 connections) — `server/monitoring/exception_tracker.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **exception_tracker.py** (21 connections) — `server/monitoring/exception_tracker.py`
- **track_exception()** (15 connections) — `server/monitoring/exception_tracker.py`
- **test_exception_tracker.py** (13 connections) — `server/tests/unit/monitoring/test_exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_exception_tracker()** (12 connections) — `server/monitoring/exception_tracker.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **ExceptionStats** (10 connections) — `server/monitoring/exception_tracker.py`
- **PerformanceStats** (10 connections) — `server/monitoring/performance_monitor.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **Exception** (7 connections)
- **ExceptionTrackInput** (6 connections) — `server/monitoring/exception_tracker.py`
- **MonitoringSummary** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **._create_and_store_record()** (6 connections) — `server/monitoring/exception_tracker.py`
- **track_exception_with_context()** (6 connections) — `server/monitoring/exception_tracker.py`
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **._log_tracked_exception()** (5 connections) — `server/monitoring/exception_tracker.py`
- **Any** (5 connections)
- **ExceptionContextTrackInput** (4 connections) — `server/monitoring/exception_tracker.py`
- **.add_exception_handler()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._parse_track_options()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._update_stats()** (4 connections) — `server/monitoring/exception_tracker.py`
- **.add_global_exception_handler()** (3 connections) — `server/monitoring/exception_tracker.py`
- *... and 50 more nodes in this community*

## Relationships

- [MonitoringDashboard](MonitoringDashboard.md) (12 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (10 shared connections)
- [lifespan.py](lifespan.py.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (4 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [testing_examples.py](testing_examples.py.md) (3 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [log_with_context](log_with_context.md) (2 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (2 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (2 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_exception_tracker.py`

## Audit Trail

- EXTRACTED: 179 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*