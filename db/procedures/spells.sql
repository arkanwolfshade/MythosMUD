-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f spells.sql
--
-- Spell and player_spell procedures. Replaces ORM in SpellRepository and PlayerSpellRepository.

-- get_all_spells: fetch all spells
CREATE OR REPLACE FUNCTION :schema_name.get_all_spells() -- noqa: PRS
RETURNS TABLE (
    spell_id character varying(255),
    name character varying(100),
    description text,
    school character varying(50),
    mp_cost integer,
    lucidity_cost integer,
    corruption_on_learn integer,
    corruption_on_cast integer,
    casting_time_seconds integer,
    target_type character varying(50),
    range_type character varying(50),
    effect_type character varying(50),
    effect_data jsonb,
    materials jsonb,
    created_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.spell_id,
        s.name,
        s.description,
        s.school,
        s.mp_cost,
        s.lucidity_cost,
        s.corruption_on_learn,
        s.corruption_on_cast,
        s.casting_time_seconds,
        s.target_type,
        s.range_type,
        s.effect_type,
        s.effect_data,
        s.materials,
        s.created_at
    FROM spells s;
END;
$$;


-- get_spell_by_id: fetch single spell by id
CREATE OR REPLACE FUNCTION :schema_name.get_spell_by_id(p_spell_id character varying) -- noqa: PRS
RETURNS TABLE (
    spell_id character varying(255),
    name character varying(100),
    description text,
    school character varying(50),
    mp_cost integer,
    lucidity_cost integer,
    corruption_on_learn integer,
    corruption_on_cast integer,
    casting_time_seconds integer,
    target_type character varying(50),
    range_type character varying(50),
    effect_type character varying(50),
    effect_data jsonb,
    materials jsonb,
    created_at timestamp with time zone
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.spell_id,
        s.name,
        s.description,
        s.school,
        s.mp_cost,
        s.lucidity_cost,
        s.corruption_on_learn,
        s.corruption_on_cast,
        s.casting_time_seconds,
        s.target_type,
        s.range_type,
        s.effect_type,
        s.effect_data,
        s.materials,
        s.created_at
    FROM spells s
    WHERE s.spell_id = p_spell_id;
END;
$$;


-- get_player_spells: fetch all spells learned by player
CREATE OR REPLACE FUNCTION :schema_name.get_player_spells(p_player_id UUID) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    player_id uuid,
    spell_id character varying(255),
    mastery integer,
    learned_at timestamp with time zone,
    last_cast_at timestamp with time zone,
    times_cast integer
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        ps.id,
        ps.player_id,
        ps.spell_id,
        ps.mastery,
        ps.learned_at,
        ps.last_cast_at,
        ps.times_cast
    FROM player_spells ps
    WHERE ps.player_id = p_player_id;
END;
$$;


-- get_player_spell: fetch single player spell
CREATE OR REPLACE FUNCTION :schema_name.get_player_spell(p_player_id UUID, p_spell_id character varying) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    player_id uuid,
    spell_id character varying(255),
    mastery integer,
    learned_at timestamp with time zone,
    last_cast_at timestamp with time zone,
    times_cast integer
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        ps.id,
        ps.player_id,
        ps.spell_id,
        ps.mastery,
        ps.learned_at,
        ps.last_cast_at,
        ps.times_cast
    FROM player_spells ps
    WHERE ps.player_id = p_player_id
      AND ps.spell_id = p_spell_id;
END;
$$;


-- learn_spell: insert or return existing (ON CONFLICT DO UPDATE no-op to get RETURNING)
CREATE OR REPLACE FUNCTION :schema_name.learn_spell( -- noqa: PRS
    p_player_id UUID,
    p_spell_id character varying,
    p_initial_mastery integer DEFAULT 0
)
RETURNS TABLE (
    id bigint,
    player_id uuid,
    spell_id character varying(255),
    mastery integer,
    learned_at timestamp with time zone,
    last_cast_at timestamp with time zone,
    times_cast integer
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    INSERT INTO player_spells (player_id, spell_id, mastery, times_cast)
    VALUES (p_player_id, p_spell_id, LEAST(100, GREATEST(0, p_initial_mastery)), 0)
    ON CONFLICT (player_id, spell_id) DO UPDATE SET mastery = player_spells.mastery
    RETURNING
        player_spells.id,
        player_spells.player_id,
        player_spells.spell_id,
        player_spells.mastery,
        player_spells.learned_at,
        player_spells.last_cast_at,
        player_spells.times_cast;
END;
$$;


-- update_mastery: update mastery for player spell
CREATE OR REPLACE FUNCTION :schema_name.update_player_spell_mastery( -- noqa: PRS
    p_player_id UUID,
    p_spell_id character varying,
    p_new_mastery integer
)
RETURNS TABLE (
    id bigint,
    player_id uuid,
    spell_id character varying(255),
    mastery integer,
    learned_at timestamp with time zone,
    last_cast_at timestamp with time zone,
    times_cast integer
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    UPDATE player_spells
    SET mastery = LEAST(100, GREATEST(0, p_new_mastery))
    WHERE player_spells.player_id = p_player_id
      AND player_spells.spell_id = p_spell_id
    RETURNING
        player_spells.id,
        player_spells.player_id,
        player_spells.spell_id,
        player_spells.mastery,
        player_spells.learned_at,
        player_spells.last_cast_at,
        player_spells.times_cast;
END;
$$;


-- record_spell_cast: increment times_cast and set last_cast_at
CREATE OR REPLACE FUNCTION :schema_name.record_spell_cast(p_player_id UUID, p_spell_id character varying) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    player_id uuid,
    spell_id character varying(255),
    mastery integer,
    learned_at timestamp with time zone,
    last_cast_at timestamp with time zone,
    times_cast integer
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    UPDATE player_spells
    SET times_cast = player_spells.times_cast + 1,
        last_cast_at = NOW()
    WHERE player_spells.player_id = p_player_id
      AND player_spells.spell_id = p_spell_id
    RETURNING
        player_spells.id,
        player_spells.player_id,
        player_spells.spell_id,
        player_spells.mastery,
        player_spells.learned_at,
        player_spells.last_cast_at,
        player_spells.times_cast;
END;
$$;
