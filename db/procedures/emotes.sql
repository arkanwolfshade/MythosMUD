-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f emotes.sql
--
-- Predefined emote and emote-alias read procedures. Replaces raw SQL in
-- server/persistence/repositories/emote_repository.py (#633).

-- get_emotes: fetch all predefined emotes, ordered by stable_id
CREATE OR REPLACE FUNCTION :schema_name.get_emotes() -- noqa: PRS
RETURNS TABLE (
    stable_id text,
    self_message text,
    other_message text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        e.stable_id,
        e.self_message,
        e.other_message
    FROM emotes e
    ORDER BY e.stable_id;
END;
$$;


-- get_emote_aliases: fetch all emote aliases joined to their owning emote's stable_id,
-- ordered by stable_id then alias
CREATE OR REPLACE FUNCTION :schema_name.get_emote_aliases() -- noqa: PRS
RETURNS TABLE (
    stable_id text,
    alias text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        e.stable_id,
        ea.alias
    FROM emote_aliases ea
    JOIN emotes e ON ea.emote_id = e.id
    ORDER BY e.stable_id, ea.alias;
END;
$$;
