# Quest Flow Integration

> 45 nodes · cohesion 0.07

## Key Concepts

- **datetime** (15 connections)
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **MythosCalendarComponents** (4 connections) — `server/time/time_service.py`
- **.advance_mythos()** (4 connections) — `server/time/time_service.py`
- **.format_clock()** (4 connections) — `server/time/time_service.py`
- **.format_clock()** (3 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (3 connections) — `server/time/time_service.py`
- **.get_last_freeze_state()** (3 connections) — `server/time/time_service.py`
- **.get_state_snapshot()** (3 connections) — `server/time/time_service.py`
- **_season_for_month()** (3 connections) — `server/time/time_service.py`
- **Get the current Mythos datetime.          Returns:             datetime: The cur** (1 connections) — `server/time/time_service.py`
- **Format the clock display string.          Args:             mythos_dt: Optional** (1 connections) — `server/time/time_service.py`
- *... and 20 more nodes in this community*

## Relationships

- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (17 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Holiday Persistence Models](Holiday_Persistence_Models.md) (2 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (2 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (1 shared connections)

## Source Files

- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 167 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*