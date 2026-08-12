# Error Handling Guide

> 29 nodes

## Key Concepts

- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections)
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **Namespace** (3 connections)
- **_print_errors()** (3 connections) — `scripts/validate_calendar.py`
- **main()** (3 connections) — `scripts/validate_calendar.py`
- **Get holidays and schedules paths.** (1 connections) — `scripts/validate_calendar.py`
- **Load and validate holidays.** (1 connections) — `scripts/validate_calendar.py`
- **Check if holidays cover documentation references.** (1 connections) — `scripts/validate_calendar.py`
- **Load and validate schedule files.** (1 connections) — `scripts/validate_calendar.py`
- **Print validation errors.** (1 connections) — `scripts/validate_calendar.py`
- **Print success message if not quiet.** (1 connections) — `scripts/validate_calendar.py`
- **Calendar domain schemas: holidays, schedules, and Mythos calendar.** (1 connections) — `server/schemas/calendar/__init__.py`
- *... and 4 more nodes in this community*

## Relationships

- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (10 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (7 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (7 shared connections)
- [Combat Messaging Base](Combat_Messaging_Base.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (2 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`

## Audit Trail

- EXTRACTED: 131 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*