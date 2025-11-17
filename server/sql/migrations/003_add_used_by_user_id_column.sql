-- Migration: Add used_by_user_id column to invites table
-- This migration adds the used_by_user_id column to track which user consumed which invite
-- PostgreSQL version

-- Check if column exists before adding (PostgreSQL specific)
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'invites'
        AND column_name = 'used_by_user_id'
    ) THEN
        ALTER TABLE invites ADD COLUMN used_by_user_id UUID REFERENCES users(id) ON DELETE SET NULL;
        -- Create index for better query performance
        CREATE INDEX IF NOT EXISTS idx_invites_used_by_user_id ON invites(used_by_user_id);
        RAISE NOTICE 'Column used_by_user_id added to invites table';
    ELSE
        RAISE NOTICE 'Column used_by_user_id already exists in invites table';
    END IF;
END $$;
