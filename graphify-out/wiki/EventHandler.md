# EventHandler

> 91 nodes · cohesion 0.04

## Key Concepts

- **MythosTickScheduler** (32 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **test_tick_scheduler.py** (18 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (16 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **asyncio** (9 connections)
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **._load_state()** (7 connections) — `server/time/time_service.py`
- **._persist_state()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._truncate_to_hour()** (5 connections) — `server/time/tick_scheduler.py`
- **.advance_mythos()** (5 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- *... and 66 more nodes in this community*

## Relationships

- [Room](Room.md) (12 shared connections)
- [MUD Disconnect Grace Period & Rest Command: Industry Comparison](MUD_Disconnect_Grace_Period_&_Rest_Command-_Industry_Comparison.md) (7 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (3 shared connections)
- [command_parser.py](command_parser.py.md) (3 shared connections)
- [command_error](command_error.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [Communities (11 total, 0 thin omitted)](Communities_11_total,_0_thin_omitted.md) (3 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [start_grace_period](start_grace_period.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 193 (91%)
- INFERRED: 19 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*