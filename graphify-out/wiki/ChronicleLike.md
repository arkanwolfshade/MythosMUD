# ChronicleLike

> 16 nodes

## Key Concepts

- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **_holiday_entry_from_row()** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **_HolidayLoadResult** (5 connections) — `server/services/holiday_service.py`
- **_string_list_from_row()** (3 connections) — `server/services/holiday_service.py`
- **.format_clock()** (3 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (3 connections) — `server/time/time_service.py`
- **Record** (1 connections)
- **TypedDict** (1 connections)
- **Protocol** (1 connections)
- **Async helper to load holidays from PostgreSQL database.** (1 connections) — `server/services/holiday_service.py`
- **Normalize nullable PostgreSQL array columns to string values.** (1 connections) — `server/services/holiday_service.py`
- **Build a HolidayEntry from a calendar_holidays row.** (1 connections) — `server/services/holiday_service.py`
- **Get the current Mythos datetime. Returns: datetime: The current Mythos datetime** (1 connections) — `server/time/time_service.py`
- **Format the clock display string. Args: mythos_dt: Optional Mythos datetime to…** (1 connections) — `server/time/time_service.py`
- **Minimal chronicle contract required by downstream systems. The canonical…** (1 connections) — `server/time/time_service.py`

## Relationships

- [HolidayService](HolidayService.md) (8 shared connections)
- [MythosChronicle](MythosChronicle.md) (4 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/services/holiday_service.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 29 (88%)
- INFERRED: 4 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*