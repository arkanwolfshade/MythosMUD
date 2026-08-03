# schemas calendar rationale

> 24 nodes

## Key Concepts

- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_tradition()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_season()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_bonus_tags()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_id_map()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_ensure_unique_ids()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_slugify_observance()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_extract_observance_ids()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Unit tests for calendar schemas.  Tests the Pydantic models in calendar.py modul** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry validates tradition.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry validates season.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry validates bonus_tags format.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection.id_map property.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection.load_file() loads from JSON.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection.ensure_unique_ids() detects duplicates.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test ScheduleCollection.load_file() loads from JSON.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test slugify_observance() converts name to slug.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test extract_observance_ids() extracts IDs from markdown table lines.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`

## Relationships

- [project paths rationale](project_paths_rationale.md) (8 shared connections)
- [commands party examples](commands_party_examples.md) (7 shared connections)
- [holiday service services](holiday_service_services.md) (4 shared connections)
- [schedule services service](schedule_services_service.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)

## Source Files

- `server/tests/unit/schemas/test_calendar_schemas.py`

## Audit Trail

- EXTRACTED: 69 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*