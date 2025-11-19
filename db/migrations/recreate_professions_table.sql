-- Migration: Recreate professions table to match SQLAlchemy model
-- The current table has UUID id and extra columns that don't match the model

BEGIN;

-- Drop the existing table (this will cascade to any foreign keys)
DROP TABLE IF EXISTS professions CASCADE;

-- Recreate with correct structure matching SQLAlchemy model
CREATE TABLE professions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    flavor_text TEXT NOT NULL,
    stat_requirements TEXT NOT NULL DEFAULT '{}',
    mechanical_effects TEXT NOT NULL DEFAULT '{}',
    is_available BOOLEAN NOT NULL DEFAULT true
);

-- Create index on is_available for filtering
CREATE INDEX IF NOT EXISTS idx_professions_available ON professions(is_available);

COMMIT;
