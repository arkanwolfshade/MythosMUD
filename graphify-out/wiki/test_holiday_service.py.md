# test_holiday_service.py

> 19 nodes

## Key Concepts

- **test_holiday_service.py** (10 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **_string_list_from_row()** (5 connections) — `server/services/holiday_service.py`
- **.test_async_load_from_database()** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_HolidayLoadResult** (3 connections) — `server/services/holiday_service.py`
- **.test_holiday_entry_from_row()** (3 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.test_string_list_from_row()** (3 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Record** (1 connections)
- **TypedDict** (1 connections)
- **asyncio** (1 connections)
- **MonkeyPatch** (1 connections)
- **Async helper to load holidays from PostgreSQL database.** (1 connections) — `server/services/holiday_service.py`
- **Normalize nullable PostgreSQL array columns to string values.** (1 connections) — `server/services/holiday_service.py`
- **Build a HolidayEntry from a calendar_holidays row.** (1 connections) — `server/services/holiday_service.py`
- **Unit tests for holiday service. Tests the HolidayService class for tracking…** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Helper normalizes nullable PostgreSQL array columns.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Row dict maps to HolidayEntry.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`
- **Regression: asyncpg load builds HolidayCollection from rows.** (1 connections) — `server/tests/unit/services/test_holiday_service.py`

## Relationships

- [HolidayService](HolidayService.md) (8 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [HolidayEntry](HolidayEntry.md) (2 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [.get_upcoming_holidays](get_upcoming_holidays.md) (1 shared connections)

## Source Files

- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*