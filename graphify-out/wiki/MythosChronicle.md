# MythosChronicle

> 51 nodes

## Key Concepts

- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **.__init__()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **.advance_mythos()** (4 connections) — `server/time/time_service.py`
- **.format_clock()** (4 connections) — `server/time/time_service.py`
- **.format_clock()** (3 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (3 connections) — `server/time/time_service.py`
- **.get_instance()** (3 connections) — `server/time/time_service.py`
- **.get_last_freeze_state()** (3 connections) — `server/time/time_service.py`
- **.get_state_snapshot()** (3 connections) — `server/time/time_service.py`
- *... and 26 more nodes in this community*

## Relationships

- [test_time_bundle.py](test_time_bundle.py.md) (7 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (5 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (4 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [HolidayService](HolidayService.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 115 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*