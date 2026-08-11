# Test Modernization Plan

> 77 nodes

## Key Concepts

- **.state()** (36 connections) — `server/realtime/connection_state_machine.py`
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
- *... and 52 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (7 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (6 shared connections)
- [Combat Messaging Base](Combat_Messaging_Base.md) (5 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (4 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (4 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (3 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [Game State Provider](Game_State_Provider.md) (3 shared connections)
- [Command Parser](Command_Parser.md) (3 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (3 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (3 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/realtime/connection_state_machine.py`
- `server/tests/unit/commands/test_time_commands.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 321 (88%)
- INFERRED: 45 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*