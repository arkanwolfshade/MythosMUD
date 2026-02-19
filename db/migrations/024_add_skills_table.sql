-- Add skills table (character creation revamp 4.2 -  skills catalog)
-- Run with: psql -h <host> -p <port> -U <user> -d <database> -f 024_add_skills_table.sql

CREATE TABLE IF NOT EXISTS skills (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    key TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    base_value INTEGER NOT NULL DEFAULT 0 CHECK (base_value >= 0 AND base_value <= 100),
    allow_at_creation BOOLEAN NOT NULL DEFAULT true,
    category TEXT
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_skills_key ON skills (key);
CREATE INDEX IF NOT EXISTS idx_skills_allow_at_creation ON skills (allow_at_creation);

COMMENT ON TABLE skills IS 'Skills catalog; base_value is sheet minimum %; allow_at_creation false for Cthulhu Mythos.';
COMMENT ON COLUMN skills.key IS 'Stable identifier e.g. accounting, cthulhu_mythos.';
COMMENT ON COLUMN skills.base_value IS 'Base percentage (0-100); Own Language uses EDU at creation.';
COMMENT ON COLUMN skills.allow_at_creation IS 'If false, skill cannot be chosen in occupation/personal slots (e.g. Cthulhu Mythos).';
