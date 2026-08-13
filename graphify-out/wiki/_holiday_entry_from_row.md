# _holiday_entry_from_row

> 7 nodes

## Key Concepts

- **_holiday_entry_from_row()** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **_string_list_from_row()** (3 connections) — `server/services/holiday_service.py`
- **Record** (1 connections)
- **Async helper to load holidays from PostgreSQL database.** (1 connections) — `server/services/holiday_service.py`
- **Normalize nullable PostgreSQL array columns to string values.** (1 connections) — `server/services/holiday_service.py`
- **Build a HolidayEntry from a calendar_holidays row.** (1 connections) — `server/services/holiday_service.py`

## Relationships

- [DatabaseError](DatabaseError.md) (3 shared connections)
- [HolidayService](HolidayService.md) (2 shared connections)
- [HolidayCollection](HolidayCollection.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/services/holiday_service.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*