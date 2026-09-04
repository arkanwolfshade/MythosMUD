-- Requires -v schema_name=<target_schema> (e.g. mythos_unit, mythos_dev).
-- Apply with: psql -d <db> -v schema_name=<schema> -f skills.sql
--
-- Skill, player_skill, and skill_use_log procedures. Replaces ORM in SkillRepository,
-- PlayerSkillRepository, and SkillUseLogRepository.

-- get_all_skills: fetch all skills ordered by key
CREATE OR REPLACE FUNCTION :schema_name.get_all_skills() -- noqa: PRS
RETURNS TABLE (
    id bigint,
    key text,
    name text,
    description text,
    base_value integer,
    allow_at_creation boolean,
    category text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.id,
        s.key,
        s.name,
        s.description,
        s.base_value,
        s.allow_at_creation,
        s.category
    FROM skills s
    ORDER BY s.key;
END;
$$;


-- get_skill_by_id: fetch single skill by id
CREATE OR REPLACE FUNCTION :schema_name.get_skill_by_id(p_skill_id bigint) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    key text,
    name text,
    description text,
    base_value integer,
    allow_at_creation boolean,
    category text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.id,
        s.key,
        s.name,
        s.description,
        s.base_value,
        s.allow_at_creation,
        s.category
    FROM skills s
    WHERE s.id = p_skill_id;
END;
$$;


-- get_skill_by_key: fetch single skill by key
CREATE OR REPLACE FUNCTION :schema_name.get_skill_by_key(p_key text) -- noqa: PRS
RETURNS TABLE (
    id bigint,
    key text,
    name text,
    description text,
    base_value integer,
    allow_at_creation boolean,
    category text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.id,
        s.key,
        s.name,
        s.description,
        s.base_value,
        s.allow_at_creation,
        s.category
    FROM skills s
    WHERE s.key = p_key;
END;
$$;


-- delete_player_skills_for_player: delete all player_skills for a player
CREATE OR REPLACE FUNCTION :schema_name.delete_player_skills_for_player(p_player_id UUID) -- noqa: PRS
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM player_skills WHERE player_skills.player_id = p_player_id;
END;
$$;


-- insert_player_skills_many: insert multiple (skill_id, value) rows for one player
CREATE OR REPLACE FUNCTION :schema_name.insert_player_skills_many( -- noqa: PRS
    p_player_id UUID,
    p_skill_ids bigint[],
    p_values integer[]
)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO player_skills (player_id, skill_id, value)
    SELECT p_player_id, t.skill_id, LEAST(100, GREATEST(0, t.value))
    FROM unnest(p_skill_ids, p_values) AS t(skill_id, value);
END;
$$;


-- get_player_skills_with_skill: fetch player_skills joined with skills
CREATE OR REPLACE FUNCTION :schema_name.get_player_skills_with_skill(p_player_id UUID) -- noqa: PRS
RETURNS TABLE (
    player_id uuid,
    skill_id bigint,
    value integer,
    skill_key text,
    skill_name text,
    skill_description text,
    skill_base_value integer,
    skill_allow_at_creation boolean,
    skill_category text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        ps.player_id,
        ps.skill_id,
        ps.value,
        s.key AS skill_key,
        s.name AS skill_name,
        s.description AS skill_description,
        s.base_value AS skill_base_value,
        s.allow_at_creation AS skill_allow_at_creation,
        s.category AS skill_category
    FROM player_skills ps
    JOIN skills s ON s.id = ps.skill_id
    WHERE ps.player_id = p_player_id;
END;
$$;


-- update_player_skill_value: update value for one player_skill (clamp 0-99)
CREATE OR REPLACE FUNCTION :schema_name.update_player_skill_value( -- noqa: PRS
    p_player_id UUID,
    p_skill_id bigint,
    p_value integer
)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE player_skills
    SET value = LEAST(99, GREATEST(0, p_value))
    WHERE player_skills.player_id = p_player_id
      AND player_skills.skill_id = p_skill_id;
END;
$$;


-- record_skill_use: insert one skill_use_log row
CREATE OR REPLACE FUNCTION :schema_name.record_skill_use( -- noqa: PRS
    p_player_id UUID,
    p_skill_id bigint,
    p_character_level_at_use integer
)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO skill_use_log (player_id, skill_id, character_level_at_use, used_at)
    VALUES (p_player_id, p_skill_id, p_character_level_at_use, NOW());
END;
$$;


-- get_skill_ids_used_at_level: distinct skill_ids used at character level
CREATE OR REPLACE FUNCTION :schema_name.get_skill_ids_used_at_level( -- noqa: PRS
    p_player_id UUID,
    p_character_level integer
)
RETURNS TABLE (skill_id bigint)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT sul.skill_id
    FROM skill_use_log sul
    WHERE sul.player_id = p_player_id
      AND sul.character_level_at_use = p_character_level;
END;
$$;
