# ScheduleEntry

> 26 nodes

## Key Concepts

- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **field_validator** (6 connections)
- **.validate_duration()** (4 connections) — `server/schemas/calendar/calendar.py`
- **test_schedule_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.apply_schedule_state()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.validate_bonus_tags()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.validate_season()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.validate_tradition()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.validate_days()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.validate_slug_list()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **test_schedule_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_entry_validation_days()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Any** (1 connections)
- **Record the schedule categories currently active for NPC routines.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Single schedule block describing routine availability…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate schedule entry days are standard English weekday names (Sunday,…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate slug-formatted list entries. Args: value: Sequence of strings to…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Ensure the schedule window moves time forward like the Chronology Tablets…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate tradition value. Args: value: The tradition string to validate…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate season value. Args: value: The season string to validate Returns: str:…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate bonus tags format.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Get all schedule entries. Returns: list[ScheduleEntry]: List of all schedule…** (1 connections) — `server/services/schedule_service.py`
- **Test ScheduleEntry can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test ScheduleEntry validates days.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- *... and 1 more nodes in this community*

## Relationships

- [server/services/__init__.py](server-services-__init__.py.md) (15 shared connections)
- [HolidayEntry](HolidayEntry.md) (7 shared connections)
- [ScheduleCollection](ScheduleCollection.md) (4 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*