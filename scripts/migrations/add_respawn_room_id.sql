-- Migration: Add respawn_room_id to players table
-- Date: 2025-10-27
-- Purpose: Enable player death/respawn system
BEGIN TRANSACTION;
-- Add respawn_room_id column with default value
ALTER TABLE players
ADD COLUMN respawn_room_id VARCHAR(100) DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001';
-- Verify column was added
SELECT name,
    type,
    dflt_value,
    pk
FROM pragma_table_info('players')
WHERE name = 'respawn_room_id';
COMMIT;
-- Expected output:
-- name              | type        | dflt_value                                      | pk
-- respawn_room_id   | VARCHAR(100)| 'earth_arkhamcity_sanitarium_room_foyer_001'   | 0
