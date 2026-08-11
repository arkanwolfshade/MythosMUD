# Merge Refactoring Summary

> 52 nodes

## Key Concepts

- **ExceptionTracker** (24 connections) — `server/monitoring/exception_tracker.py`
- **exception_tracker.py** (20 connections) — `server/monitoring/exception_tracker.py`
- **track_exception()** (14 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **Exception** (7 connections)
- **track_exception_with_context()** (7 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionTrackInput** (6 connections) — `server/monitoring/exception_tracker.py`
- **._create_and_store_record()** (6 connections) — `server/monitoring/exception_tracker.py`
- **Any** (5 connections)
- **._log_tracked_exception()** (5 connections) — `server/monitoring/exception_tracker.py`
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
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
- **.get_critical_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- **.get_recent_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- *... and 27 more nodes in this community*

## Relationships

- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (9 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (4 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (3 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (3 shared connections)
- [Test Migration Mapping](Test_Migration_Mapping.md) (3 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (3 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`

## Audit Trail

- EXTRACTED: 201 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*