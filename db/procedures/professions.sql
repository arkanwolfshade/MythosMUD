-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f professions.sql
--
-- Profession procedures. Replaces ORM in ProfessionRepository.

-- get_all_professions: fetch all professions
CREATE OR REPLACE FUNCTION :schema_name.get_all_professions() -- noqa: PRS
RETURNS TABLE (
    id bigint,
    name character varying(50),
    description text,
    flavor_text text,
    stat_requirements text,
    mechanical_effects text,
    is_available boolean,
    stat_modifiers text,
    skill_modifiers text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.id,
        p.name,
        p.description,
        p.flavor_text,
        p.stat_requirements,
        p.mechanical_effects,
        p.is_available,
        p.stat_modifiers,
        p.skill_modifiers
    FROM professions p;
END;
$$;


-- get_profession_by_id: fetch single profession by id
CREATE OR REPLACE FUNCTION :schema_name.get_profession_by_id(p_profession_id bigint) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    name character varying(50),
    description text,
    flavor_text text,
    stat_requirements text,
    mechanical_effects text,
    is_available boolean,
    stat_modifiers text,
    skill_modifiers text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.id,
        p.name,
        p.description,
        p.flavor_text,
        p.stat_requirements,
        p.mechanical_effects,
        p.is_available,
        p.stat_modifiers,
        p.skill_modifiers
    FROM professions p
    WHERE p.id = p_profession_id;
END;
$$;
