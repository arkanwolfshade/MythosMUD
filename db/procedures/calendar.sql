-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f calendar.sql
--
-- Calendar holiday and NPC-schedule read procedures. Replaces raw SQL in
-- server/services/holiday_service.py and server/services/schedule_service.py (#633).

-- get_calendar_holidays: fetch all holiday definitions, ordered by month/day/name.
-- season is cast to text -- season_enum is schema-local and callers already treat it as a string.
CREATE OR REPLACE FUNCTION :schema_name.get_calendar_holidays() -- noqa: PRS
RETURNS TABLE (
    stable_id text,
    name text,
    tradition text,
    month smallint,
    day smallint,
    duration_hours smallint,
    season text,
    bonus_tags text[]
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        ch.stable_id,
        ch.name,
        ch.tradition,
        ch.month,
        ch.day,
        ch.duration_hours,
        ch.season::text,
        ch.bonus_tags
    FROM calendar_holidays ch
    ORDER BY ch.month, ch.day, ch.name;
END;
$$;


-- get_calendar_npc_schedules: fetch all NPC schedule definitions, ordered by category/start_hour/name
CREATE OR REPLACE FUNCTION :schema_name.get_calendar_npc_schedules() -- noqa: PRS
RETURNS TABLE (
    stable_id text,
    name text,
    category text,
    start_hour smallint,
    end_hour smallint,
    days text[],
    applies_to text[],
    effects text[],
    notes text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        cns.stable_id,
        cns.name,
        cns.category,
        cns.start_hour,
        cns.end_hour,
        cns.days,
        cns.applies_to,
        cns.effects,
        cns.notes
    FROM calendar_npc_schedules cns
    ORDER BY cns.category, cns.start_hour, cns.name;
END;
$$;
