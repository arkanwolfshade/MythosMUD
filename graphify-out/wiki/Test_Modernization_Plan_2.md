# Test Modernization Plan

> 43 nodes

## Key Concepts

- **datetime** (15 connections)
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **.format_clock()** (4 connections) — `server/time/time_service.py`
- **.advance_mythos()** (4 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (3 connections) — `server/time/time_service.py`
- **.format_clock()** (3 connections) — `server/time/time_service.py`
- **.get_state_snapshot()** (3 connections) — `server/time/time_service.py`
- **.get_last_freeze_state()** (3 connections) — `server/time/time_service.py`
- **_season_for_month()** (3 connections) — `server/time/time_service.py`
- **Snapshot of the chronicle's reference timestamps.      The last frozen real time** (1 connections) — `server/time/time_service.py`
- **Normalize datetimes to UTC for deterministic math.** (1 connections) — `server/time/time_service.py`
- **Get the current Mythos datetime.          Returns:             datetime: The cur** (1 connections) — `server/time/time_service.py`
- *... and 18 more nodes in this community*

## Relationships

- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (23 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (1 shared connections)

## Source Files

- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 162 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*