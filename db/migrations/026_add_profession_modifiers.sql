-- Add stat_modifiers and skill_modifiers to professions (character creation revamp 4.4, 4.3)
-- Run with: psql -h <host> -p <port> -U <user> -d <database> -f 026_add_profession_modifiers.sql

ALTER TABLE professions
    ADD COLUMN IF NOT EXISTS stat_modifiers TEXT NOT NULL DEFAULT '[]';

ALTER TABLE professions
    ADD COLUMN IF NOT EXISTS skill_modifiers TEXT NOT NULL DEFAULT '[]';

COMMENT ON COLUMN professions.stat_modifiers IS 'JSON array of {stat, value} applied to rolled stats at creation (e.g. [{"stat":"intelligence","value":5}]).';
COMMENT ON COLUMN professions.skill_modifiers IS 'JSON array of {skill_key, value} delta applied to skills at creation (e.g. [{"skill_key":"library_use","value":5}]).';
