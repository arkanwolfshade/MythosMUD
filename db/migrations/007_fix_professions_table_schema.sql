-- Migration: Fix professions table schema to match SQLAlchemy model
-- This migration adds missing columns (flavor_text, stat_requirements, mechanical_effects, is_available)
-- and removes old columns (stable_id, attributes) if they exist
-- Status: ⚠️ DEPRECATED - Professions table already matches schema in db/authoritative_schema.sql
-- This migration is kept for historical reference only.

DO $$
BEGIN
    -- Add flavor_text column if missing
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public' AND table_name = 'professions' AND column_name = 'flavor_text'
    ) THEN
        ALTER TABLE professions ADD COLUMN flavor_text TEXT NOT NULL DEFAULT '';
        RAISE NOTICE 'Added flavor_text column to professions table';
    END IF;

    -- Add stat_requirements column if missing
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public' AND table_name = 'professions' AND column_name = 'stat_requirements'
    ) THEN
        ALTER TABLE professions ADD COLUMN stat_requirements TEXT NOT NULL DEFAULT '{}';
        RAISE NOTICE 'Added stat_requirements column to professions table';
    END IF;

    -- Add mechanical_effects column if missing
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public' AND table_name = 'professions' AND column_name = 'mechanical_effects'
    ) THEN
        ALTER TABLE professions ADD COLUMN mechanical_effects TEXT NOT NULL DEFAULT '{}';
        RAISE NOTICE 'Added mechanical_effects column to professions table';
    END IF;

    -- Add is_available column if missing
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public' AND table_name = 'professions' AND column_name = 'is_available'
    ) THEN
        ALTER TABLE professions ADD COLUMN is_available BOOLEAN NOT NULL DEFAULT true;
        RAISE NOTICE 'Added is_available column to professions table';
    END IF;

    -- Update existing rows with defaults if needed
    UPDATE professions
    SET flavor_text = COALESCE(flavor_text, ''),
        stat_requirements = COALESCE(stat_requirements, '{}'),
        mechanical_effects = COALESCE(mechanical_effects, '{}'),
        is_available = COALESCE(is_available, true)
    WHERE flavor_text IS NULL
       OR stat_requirements IS NULL
       OR mechanical_effects IS NULL
       OR is_available IS NULL;

    -- Create index on is_available if it doesn't exist
    IF NOT EXISTS (
        SELECT 1 FROM pg_indexes
        WHERE schemaname = 'public'
        AND tablename = 'professions'
        AND indexname = 'idx_professions_available'
    ) THEN
        CREATE INDEX idx_professions_available ON professions(is_available);
        RAISE NOTICE 'Created index idx_professions_available on professions table';
    END IF;

    RAISE NOTICE 'Professions table schema migration completed';
END $$;
