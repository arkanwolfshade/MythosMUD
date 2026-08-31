# .get_upcoming_holidays

> 22 nodes

## Key Concepts

- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **_ensure_utc()** (6 connections) — `server/services/holiday_service.py`
- **datetime** (6 connections)
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- **._day_ordinal()** (3 connections) — `server/services/holiday_service.py`
- **.get_active_holiday_names()** (3 connections) — `server/services/holiday_service.py`
- **.get_upcoming_summary()** (3 connections) — `server/services/holiday_service.py`
- **.last_refresh()** (3 connections) — `server/services/holiday_service.py`
- **.test_ensure_utc_naive_and_aware()** (3 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Update the active holiday window for the provided Mythos timestamp.** (1 connections) — `server/services/holiday_service.py`
- **Return currently active holiday entries.** (1 connections) — `server/services/holiday_service.py`
- **Get active holidays and serialize them for API responses. This method…** (1 connections) — `server/services/holiday_service.py`
- **Get upcoming holidays and serialize them for API responses. This method…** (1 connections) — `server/services/holiday_service.py`
- **Convenience helper for formatted admin output.** (1 connections) — `server/services/holiday_service.py`
- **Return the next N holidays, wrapping around the calendar.** (1 connections) — `server/services/holiday_service.py`
- **Return formatted strings describing upcoming holidays.** (1 connections) — `server/services/holiday_service.py`
- **Convert month/day into a monotonically increasing ordinal (1-indexed).** (1 connections) — `server/services/holiday_service.py`
- **Get the last refresh timestamp. Returns: datetime | None: The timestamp of the…** (1 connections) — `server/services/holiday_service.py`
- **Naive datetimes gain UTC; aware datetimes convert to UTC.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`

## Relationships

- [HolidayService](HolidayService.md) (10 shared connections)
- [HolidayEntry](HolidayEntry.md) (5 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_holiday_service.py](test_holiday_service.py.md) (1 shared connections)

## Source Files

- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*