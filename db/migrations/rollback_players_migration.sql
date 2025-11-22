-- Rollback: Restore players table from backup
-- This script restores the players table from the backup created during migration
-- WARNING: This will lose any data created after the migration
SET client_min_messages = WARNING;
SET search_path = public;
BEGIN;
-- Check if backup exists
DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
        AND table_name = 'players_backup_migration'
) THEN RAISE EXCEPTION 'Backup table players_backup_migration does not exist. Cannot rollback.';
END IF;
END $$;
-- Drop current players table
DROP TABLE IF EXISTS players CASCADE;
-- Restore from backup
CREATE TABLE players AS
SELECT *
FROM players_backup_migration;
-- Restore indexes if they existed (adjust based on original schema)
-- Note: This is a basic restoration. You may need to adjust indexes based on your original schema.
COMMIT;
-- Note: After rollback, you may want to drop the backup table:
-- DROP TABLE IF EXISTS players_backup_migration;
