---
name: Convert Temporal System to 4:1 Ratio with Real-World Calendar
overview: Convert the temporal system from 9.6:1 compression ratio to 4:1 ratio and switch from custom Mythos calendar (starting 1930) to real-world Gregorian calendar starting January 1, 1920. This includes updating configuration, weekday calculations, state migration, and all dependent systems.
todos:

  - id: update-config

    content: "Update TimeConfig defaults: compression_ratio 9.6→4.0, mythos_epoch 1930→1920"
    status: completed

  - id: update-weekdays

    content: Replace custom weekday calculation with standard Python calendar.weekday() and day_name
    status: completed

  - id: update-schemas

    content: Update calendar schemas to use standard weekday names (Monday-Sunday)
    status: completed

  - id: migrate-schedules

    content: Migrate all schedule JSON files and database records from Primus-Sextus to Monday-Sunday
    status: completed

  - id: migrate-state

    content: Add state file migration logic or reset to new epoch
    status: completed

  - id: update-tests

    content: Update all time-related tests for new ratio and calendar
    status: completed

  - id: update-docs

    content: Update TEMPORAL_SYSTEM_RESEARCH.md with new calculations and calendar description
    status: completed

  - id: verify-client

    content: Verify client correctly displays real-world calendar dates and weekdays
    status: completed
isProject: false
---

# Convert Temporal System to 4:1 Ratio with Real-World Calendar

## Overview

Convert the MythosChronicle temporal system to use:

**Compression ratio**: 4.0 in-game hours per real hour (changed from 9.6)

**Calendar**: Real-world Gregorian calendar starting January 1, 1920 (changed from custom calendar starting 1930)

**Weekdays**: Standard weekday names (Monday-Sunday) instead of custom Mythos weekdays (Primus-Sextus)

## Impact Analysis

**Time Calculations:**

- Current: 1 in-game day = 2.5 real hours, 1 in-game year = ~38 real days
- New: 1 in-game day = 6 real hours, 1 in-game year = ~91.25 real days
- 90 real days = 360 in-game days (still in 1920, not 1921)

**Affected Systems:**

- Time service core (`server/time/time_service.py`)
- Configuration (`server/config/models.py`)
- Holiday service (uses calendar dates)
- Schedule service (uses weekday names)
- Client UI (displays time/calendar)
- State persistence (`data/system/time_state.json`)
- Tests
- Documentation

## Implementation Steps

### 1. Update Configuration Defaults

**File**: `server/config/models.py`

- Change `compression_ratio` default from `9.6` to `4.0`
- Change `mythos_epoch` default from `datetime(1930, 1, 1, tzinfo=UTC)` to `datetime(1920, 1, 1, tzinfo=UTC)`
- Update field description to reflect real-world calendar usage

### 2. Update Weekday Calculation

**File**: `server/time/time_service.py`

- Remove `_MYTHOS_WEEKDAY_NAMES` constant
- Update `get_calendar_components()` to use Python's `calendar.day_name[normalized.weekday()]` instead of custom calculation
- Remove `week_of_month` calculation (based on 6-day weeks) or update to use standard calendar weeks
- Update `day_of_week` to use standard `datetime.weekday()` (0=Monday, 6=Sunday)

### 3. Update Schedule Service

**File**: `server/services/schedule_service.py`

- Update validation to accept standard weekday names (Monday-Sunday) instead of Mythos weekdays
- Update any weekday matching logic

### 4. Update Calendar Schema

**File**: `server/schemas/calendar.py`

- Update `_MYTHOS_WEEKDAYS` to standard weekday names: `["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]`
- Update validation logic

### 5. Update Schedule JSON Schema

**File**: `schemas/calendar/schedule.schema.json`

- Update weekday enum from `["Primus", "Secundus", ...]` to `["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]`

### 6. Migrate Existing Schedule Data

**Files**:

- `data/local/calendar/schedules/npc.json`
- `data/e2e_test/calendar/schedules/npc.json`
- `data/unit_test/calendar/schedules/npc.json`
- Database records in `calendar_npc_schedules` table

- Convert all `"days": ["Primus", ...]` to standard weekday names
- Map: Primus→Monday, Secundus→Tuesday, Tertius→Wednesday, Quartus→Thursday, Quintus→Friday, Sextus→Saturday
- Note: 6-day week becomes 7-day week, may need to add Sunday or adjust schedules

### 7. Handle State File Migration

**File**: `server/time/time_service.py` (in `_load_state()`)

- Add migration logic to detect old state format and convert:
- Recalculate `mythos_timestamp` based on new epoch (1920-01-01) and compression ratio (4.0)
- Or reset to epoch defaults if conversion is too complex
- Consider adding a version field to state file for future migrations

### 8. Update Documentation

**File**: `docs/TEMPORAL_SYSTEM_RESEARCH.md`

- Update compression ratio from 9.6 to 4.0
- Update all time calculations (1 in-game hour = 15 real minutes, 1 in-game day = 6 real hours, 1 in-game year = ~91.25 real days)
- Update calendar description to reflect real-world Gregorian calendar
- Remove references to custom 6-day weeks and 30-day months
- Update day-night cadence calculations

### 9. Update Tests

**Files**:

- `server/tests/unit/commands/test_time_commands.py`
- Any other time-related tests

- Update test expectations for new compression ratio
- Update test dates to use 1920+ instead of 1930+
- Update weekday assertions to use standard names
- Update any hardcoded time calculations

### 10. Update Database Schedule Records

**File**: SQL migration script (new file in `db/migrations/`)

- Create migration to update `calendar_npc_schedules.days` array values
- Convert Primus→Monday, Secundus→Tuesday, etc.
- Handle any schedules that need Sunday added

### 11. Verify Client Integration

**Files**:

- `client/src/components/MythosTimeHud.tsx`
- `client/src/components/ui-v2/eventHandlers/systemHandlers.ts`

- Verify client correctly displays real-world calendar dates
- Ensure weekday names display correctly
- Test time progression in UI

## Migration Strategy

**Option A: Reset State (Recommended for Development)**

- Delete or backup `data/system/time_state.json`
- System will reinitialize with new epoch (1920-01-01) and compression ratio (4.0)
- Simple but loses current in-game time position

**Option B: Convert Existing State**

- Calculate equivalent time in new system
- More complex but preserves relative time position
- Formula: `new_mythos_time = 1920-01-01 + (old_mythos_time - 1930-01-01) * (4.0 / 9.6)`

## Testing Checklist

[ ] Verify compression ratio is 4.0

- [ ] Verify epoch is 1920-01-01
- [ ] Verify weekday names are standard (Monday-Sunday)
- [ ] Verify time calculations: 1 real day = 4 in-game days
- [ ] Verify holidays trigger on correct dates
- [ ] Verify NPC schedules work with new weekday names
- [ ] Verify client displays correct time/date
- [ ] Verify state persistence and loading
- [ ] Run all time-related tests
- [ ] Verify documentation is updated

## Notes

The custom 6-day week system (Primus-Sextus) will be replaced with standard 7-day week

- NPC schedules using the old weekday names must be migrated
- The `week_of_month` calculation may need adjustment or removal
- Consider whether to keep `week_of_month` or remove it entirely with real-world calendar
