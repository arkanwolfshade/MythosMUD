# nats retry handler

> 45 nodes

## Key Concepts

- **ExceptionTracker** (23 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **create_enhanced_error_context()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **track_exception_with_context()** (8 connections) — `server/monitoring/exception_tracker.py`
- **Exception** (5 connections)
- **Any** (5 connections)
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **create_context_from_websocket()** (5 connections) — `server/utils/error_logging.py`
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
- **Represents a tracked exception with full context.** (1 connections) — `server/monitoring/exception_tracker.py`
- **Comprehensive exception tracking system.      This class provides 100% exception** (1 connections) — `server/monitoring/exception_tracker.py`
- **Initialize the exception tracker.          Args:             max_records: Maximu** (1 connections) — `server/monitoring/exception_tracker.py`
- *... and 20 more nodes in this community*

## Relationships

- [.shutdown()](shutdown%28%29.md) (9 shared connections)
- [websocket integration](websocket_integration.md) (4 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [fetch schedule entries()](fetch_schedule_entries%28%29.md) (3 shared connections)
- [useRoomMapData.test](useRoomMapData.test.md) (2 shared connections)
- [real time](real_time.md) (2 shared connections)
- [fastapi integration](fastapi_integration.md) (1 shared connections)
- [Request](Request.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 145 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*