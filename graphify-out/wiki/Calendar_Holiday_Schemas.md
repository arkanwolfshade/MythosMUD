# Calendar Holiday Schemas

> 22 nodes · cohesion 0.03

## Key Concepts

- **validate_calendar.py** (16 connections) — `scripts/validate_calendar.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections) — `scripts/validate_calendar.py`
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- **main()** (3 connections) — `scripts/validate_calendar.py`
- **_print_errors()** (3 connections) — `scripts/validate_calendar.py`
- **Namespace** (3 connections) — `scripts/validate_calendar.py`
- **datetime** (3 connections) — `server/services/schedule_service.py`
- **Path** (3 connections) — `server/utils/project_paths.py`
- **Connection** (2 connections) — `server/services/schedule_service.py`
- **Path** (2 connections) — `server/services/schedule_service.py`
- **Record** (2 connections) — `server/services/schedule_service.py`
- **MonkeyPatch** (2 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Print validation errors.** (1 connections) — `scripts/validate_calendar.py`
- **Print success message if not quiet.** (1 connections) — `scripts/validate_calendar.py`
- **Get holidays and schedules paths.** (1 connections) — `scripts/validate_calendar.py`
- **Check if holidays cover documentation references.** (1 connections) — `scripts/validate_calendar.py`
- **Any** (1 connections) — `server/schemas/calendar/calendar.py`

## Relationships

- [Holiday Persistence Models](Holiday_Persistence_Models.md) (6 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (4 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 80 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*