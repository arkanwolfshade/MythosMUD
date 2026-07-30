# get health status()

> 75 nodes

## Key Concepts

- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **time_service.py** (25 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **datetime** (15 connections)
- **handle_time_command()** (14 connections) — `server/commands/time_commands.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **test_time_commands.py** (8 connections) — `server/tests/unit/commands/test_time_commands.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **__init__.py** (8 connections) — `server/time/__init__.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.__init__()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **MythosCalendarComponents** (4 connections) — `server/time/time_service.py`
- *... and 50 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (11 shared connections)
- [HolidayCollection](HolidayCollection.md) (5 shared connections)
- [.shutdown()](shutdown%28%29.md) (4 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (4 shared connections)
- [process all status effects()](process_all_status_effects%28%29.md) (4 shared connections)
- [test find item in room](test_find_item_in_room.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [test magic commands](test_magic_commands.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [Player Position Service](Player_Position_Service.md) (2 shared connections)
- [metrics](metrics.md) (2 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (2 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/tests/unit/commands/test_time_commands.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 317 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*