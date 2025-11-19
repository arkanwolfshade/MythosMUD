-- Migration: Fix professions table structure to match schema
-- This ensures the table has all required columns before loading seed data

DO $$
BEGIN
    -- Add flavor_text if missing
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'professions' AND column_name = 'flavor_text'
    ) THEN
        ALTER TABLE professions ADD COLUMN flavor_text TEXT NOT NULL DEFAULT '';
        RAISE NOTICE 'Added flavor_text column';
    END IF;

    -- Add stat_requirements if missing
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'professions' AND column_name = 'stat_requirements'
    ) THEN
        ALTER TABLE professions ADD COLUMN stat_requirements TEXT NOT NULL DEFAULT '{}';
        RAISE NOTICE 'Added stat_requirements column';
    END IF;

    -- Add mechanical_effects if missing
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'professions' AND column_name = 'mechanical_effects'
    ) THEN
        ALTER TABLE professions ADD COLUMN mechanical_effects TEXT NOT NULL DEFAULT '{}';
        RAISE NOTICE 'Added mechanical_effects column';
    END IF;

    -- Add is_available if missing
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'professions' AND column_name = 'is_available'
    ) THEN
        ALTER TABLE professions ADD COLUMN is_available BOOLEAN NOT NULL DEFAULT true;
        RAISE NOTICE 'Added is_available column';
    END IF;

    -- Ensure id is SERIAL (auto-increment) if it's not already
    -- Check if id column exists and is the right type
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'professions' AND column_name = 'id'
        AND data_type != 'integer'
    ) THEN
        RAISE EXCEPTION 'id column exists but is not INTEGER type';
    END IF;

    -- Ensure primary key exists on id
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE table_name = 'professions'
        AND constraint_type = 'PRIMARY KEY'
    ) THEN
        ALTER TABLE professions ADD PRIMARY KEY (id);
        RAISE NOTICE 'Added PRIMARY KEY constraint on id';
    END IF;

    -- Ensure unique constraint on name
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE table_name = 'professions'
        AND constraint_name = 'professions_name_key'
    ) THEN
        ALTER TABLE professions ADD CONSTRAINT professions_name_key UNIQUE (name);
        RAISE NOTICE 'Added UNIQUE constraint on name';
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

    RAISE NOTICE 'Professions table structure verified and fixed';
END $$;
