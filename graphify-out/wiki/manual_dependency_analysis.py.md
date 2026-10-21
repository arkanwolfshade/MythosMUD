# manual_dependency_analysis.py

> 61 nodes · cohesion 0.05

## Key Concepts

- **ExceptionTracker** (30 connections) — `server/monitoring/exception_tracker.py`
- **track_exception()** (19 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_exception_tracker()** (12 connections) — `server/monitoring/exception_tracker.py`
- **test_exception_tracker.py** (12 connections) — `server/tests/unit/monitoring/test_exception_tracker.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **Exception** (7 connections)
- **._create_and_store_record()** (6 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionTrackInput** (6 connections) — `server/monitoring/exception_tracker.py`
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
- **.get_recent_exceptions()** (3 connections) — `server/monitoring/exception_tracker.py`
- *... and 36 more nodes in this community*

## Relationships

- [Room](Room.md) (12 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [test_player_event_handlers_room.py](test_player_event_handlers_room.py.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (2 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (2 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (2 shared connections)
- [PlayerMute](PlayerMute.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/monitoring/test_exception_tracker.py`

## Audit Trail

- EXTRACTED: 131 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*