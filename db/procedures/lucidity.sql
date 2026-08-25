-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f lucidity.sql
--
-- Passive lucidity flux rate-override reads. Replaces raw SQL in
-- server/services/passive_lucidity_flux/rate_overrides.py (#633).

-- get_lucidity_rate_overrides: fetch zone- and subzone-level special_rules overrides in one
-- polymorphic result set. subzone_stable_id IS NULL marks a zone-level row; callers already key
-- on that sentinel (server/services/passive_lucidity_flux/rate_overrides.py's
-- _process_override_row). Preserves the original single-round-trip UNION ALL shape.
CREATE OR REPLACE FUNCTION :schema_name.get_lucidity_rate_overrides() -- noqa: PRS
RETURNS TABLE (
    zone_stable_id text,
    subzone_stable_id text,
    special_rules jsonb
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        z.stable_id AS zone_stable_id,
        NULL::text AS subzone_stable_id,
        z.special_rules
    FROM zones z
    WHERE z.special_rules IS NOT NULL
    UNION ALL
    SELECT
        z.stable_id AS zone_stable_id,
        sz.stable_id AS subzone_stable_id,
        sz.special_rules
    FROM subzones sz
    JOIN zones z ON sz.zone_id = z.id
    WHERE sz.special_rules IS NOT NULL
    ORDER BY zone_stable_id, subzone_stable_id;
END;
$$;
