# holiday services service

> 7 nodes

## Key Concepts

- **_holiday_entry_from_row()** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **_string_list_from_row()** (3 connections) — `server/services/holiday_service.py`
- **Record** (2 connections)
- **Normalize nullable PostgreSQL array columns to string values.** (1 connections) — `server/services/holiday_service.py`
- **Build a HolidayEntry from a calendar_holidays row.** (1 connections) — `server/services/holiday_service.py`
- **Async helper to load holidays from PostgreSQL database.** (1 connections) — `server/services/holiday_service.py`

## Relationships

- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [project paths rationale](project_paths_rationale.md) (2 shared connections)
- [database config helpers](database_config_helpers.md) (1 shared connections)
- [holiday service services](holiday_service_services.md) (1 shared connections)

## Source Files

- `server/services/holiday_service.py`

## Audit Trail

- EXTRACTED: 19 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*