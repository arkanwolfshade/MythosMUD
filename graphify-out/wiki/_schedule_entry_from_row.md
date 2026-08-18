# _schedule_entry_from_row

> 34 nodes

## Key Concepts

- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_DatabaseLoadResult** (4 connections) — `server/services/schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url_missing()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_lower_string_list_from_row()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_schedule_entry_from_row()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_string_list_from_row()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **MonkeyPatch** (3 connections)
- **Connection** (1 connections)
- **Record** (1 connections)
- **TypedDict** (1 connections)
- **asyncio** (1 connections)
- **Load and normalize schedule rows from PostgreSQL.** (1 connections) — `server/services/schedule_service.py`
- **Async helper to load schedules from PostgreSQL database.** (1 connections) — `server/services/schedule_service.py`
- **Map Latin weekday names to standard English (Sunday, Monday, ...); pass-through…** (1 connections) — `server/services/schedule_service.py`
- **Normalize nullable PostgreSQL array columns to string values.** (1 connections) — `server/services/schedule_service.py`
- **Normalize nullable PostgreSQL array columns to lowercase slug strings.** (1 connections) — `server/services/schedule_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [HolidayService](HolidayService.md) (9 shared connections)
- [GameBundle](GameBundle.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (1 shared connections)

## Source Files

- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*