# Merge Refactoring Summary

> 59 nodes

## Key Concepts

- **ExceptionTracker** (24 connections) — `server/monitoring/exception_tracker.py`
- **exception_tracker.py** (20 connections) — `server/monitoring/exception_tracker.py`
- **track_exception()** (14 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **create_enhanced_error_context()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **Exception** (7 connections)
- **track_exception_with_context()** (7 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionTrackInput** (6 connections) — `server/monitoring/exception_tracker.py`
- **._create_and_store_record()** (6 connections) — `server/monitoring/exception_tracker.py`
- **Any** (5 connections)
- **._log_tracked_exception()** (5 connections) — `server/monitoring/exception_tracker.py`
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **create_context_from_websocket()** (5 connections) — `server/utils/error_logging.py`
- **ExceptionContextTrackInput** (4 connections) — `server/monitoring/exception_tracker.py`
- **._parse_track_options()** (4 connections) — `server/monitoring/exception_tracker.py`
- **.add_exception_handler()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._update_stats()** (4 connections) — `server/monitoring/exception_tracker.py`
- **.__init__()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exception_record()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_type()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_user()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_exceptions_by_correlation()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_unhandled_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- *... and 34 more nodes in this community*

## Relationships

- [Memory Leak Metrics](Memory_Leak_Metrics.md) (11 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (10 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (3 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (3 shared connections)
- [Test Migration Mapping](Test_Migration_Mapping.md) (3 shared connections)
- [Mythos Time HUD](Mythos_Time_HUD.md) (3 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (3 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 223 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*