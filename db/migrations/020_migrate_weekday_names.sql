-- Migration: Convert Mythos weekday names (Primus-Sextus) to standard weekday names (Monday-Sunday)
-- Date: 2025-01-XX
-- Description: Updates calendar_npc_schedules.days array values to use standard weekday names
--              as part of the temporal system conversion from custom calendar to real-world Gregorian calendar

-- codacy:ignore=sql:RAC_TABLE_REQUIRED
-- Reason: PostgreSQL configuration command, not a data query targeting RAC_* tables
SET client_min_messages = WARNING;
SET search_path = public;

-- Update calendar_npc_schedules.days array values
-- Map: Primus→Monday, Secundus→Tuesday, Tertius→Wednesday, Quartus→Thursday, Quintus→Friday, Sextus→Saturday
-- Note: 6-day week becomes 7-day week - schedules that had all 6 days now get Saturday only
--       (Sunday is not added by default, as schedules may have intentionally excluded it)

-- codacy:ignore=sql:RAC_TABLE_REQUIRED
-- Reason: Migration file updates calendar_npc_schedules table (not RAC_* table), which is a valid migration operation
UPDATE calendar_npc_schedules
SET days = (
    -- codacy:ignore=sql:RAC_TABLE_REQUIRED
    -- Reason: Subquery within UPDATE statement for calendar_npc_schedules migration
    SELECT array_agg(
        CASE
            WHEN day_value = 'Primus' THEN 'Monday'
            WHEN day_value = 'Secundus' THEN 'Tuesday'
            WHEN day_value = 'Tertius' THEN 'Wednesday'
            WHEN day_value = 'Quartus' THEN 'Thursday'
            WHEN day_value = 'Quintus' THEN 'Friday'
            WHEN day_value = 'Sextus' THEN 'Saturday'
            ELSE day_value  -- Keep any unexpected values as-is (shouldn't happen)
        END
        ORDER BY CASE
            WHEN day_value = 'Primus' THEN 1
            WHEN day_value = 'Secundus' THEN 2
            WHEN day_value = 'Tertius' THEN 3
            WHEN day_value = 'Quartus' THEN 4
            WHEN day_value = 'Quintus' THEN 5
            WHEN day_value = 'Sextus' THEN 6
            ELSE 99
        END
    )
    FROM unnest(days) AS day_value
    WHERE day_value IN ('Primus', 'Secundus', 'Tertius', 'Quartus', 'Quintus', 'Sextus')
    OR day_value NOT IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
)
WHERE days && ARRAY['Primus', 'Secundus', 'Tertius', 'Quartus', 'Quintus', 'Sextus']::text [];

-- Verify the migration
-- codacy:ignore=sql:RAC_TABLE_REQUIRED
-- Reason: PostgreSQL anonymous block for verification, not a data query targeting RAC_* tables
DO $$
DECLARE
    remaining_old_weekdays int;
BEGIN
    -- codacy:ignore=sql:RAC_TABLE_REQUIRED
    -- Reason: Verification query in DO block checks migration success, not a data query targeting RAC_* tables
    SELECT COUNT(*) INTO remaining_old_weekdays
    FROM calendar_npc_schedules
    WHERE days && ARRAY['Primus', 'Secundus', 'Tertius', 'Quartus', 'Quintus', 'Sextus']::text [];

    IF remaining_old_weekdays > 0 THEN
        RAISE WARNING 'Migration incomplete: % schedule(s) still contain old weekday names', remaining_old_weekdays;
    ELSE
        RAISE NOTICE 'Migration successful: All weekday names converted to standard format';
    END IF;
END $$;
