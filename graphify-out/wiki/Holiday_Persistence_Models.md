# Holiday Persistence Models

> 8 nodes · cohesion 0.02

## Key Concepts

- **datetime** (8 connections) — `server/services/holiday_service.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **_load_and_validate_holidays()** (5 connections) — `scripts/validate_calendar.py`
- **Path** (3 connections) — `server/schemas/calendar/calendar.py`
- **Path** (3 connections) — `server/services/holiday_service.py`
- **Record** (3 connections) — `server/services/holiday_service.py`
- **Load and validate holidays.** (1 connections) — `scripts/validate_calendar.py`
- **Load and validate schedule files.** (1 connections) — `scripts/validate_calendar.py`

## Relationships

- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (6 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (3 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`

## Audit Trail

- EXTRACTED: 24 (80%)
- INFERRED: 6 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*