-- Migration: Add Partial Indexes for Active Player Queries
-- Description: Adds partial indexes with WHERE is_deleted = FALSE for better
--              query performance when filtering active players only
-- Date: 2025-01-XX
--
-- This migration adds partial indexes to optimize queries that filter by:
-- 1. user_id with is_deleted = FALSE (for active player lookups)
-- 2. current_room_id with is_deleted = FALSE (for room occupant queries)
--
-- These partial indexes are more efficient than full indexes when most queries
-- filter for active players only, as they exclude deleted players from the index.

-- Step 1: Add partial index for user_id lookups on active players only
-- This optimizes queries like: SELECT * FROM players WHERE user_id = ? AND is_deleted = FALSE
CREATE INDEX IF NOT EXISTS idx_players_user_id_active
ON players (user_id)
WHERE is_deleted = FALSE;

-- Step 2: Add partial index for current_room_id queries on active players only
-- This optimizes queries like: SELECT * FROM players WHERE current_room_id = ? AND is_deleted = FALSE
-- This is critical for room occupant queries which should only return active players
CREATE INDEX IF NOT EXISTS idx_players_current_room_id_active
ON players (current_room_id)
WHERE is_deleted = FALSE;

-- Step 3: Add comments to document the indexes
COMMENT ON INDEX idx_players_user_id_active IS
'Partial index for efficient user_id lookups on active (non-deleted) players only. '
'Optimizes queries filtering by user_id where is_deleted = FALSE.';

COMMENT ON INDEX idx_players_current_room_id_active IS
'Partial index for efficient current_room_id queries on active (non-deleted) players only. '
'Optimizes room occupant queries which should only return active players. '
'Critical for get_players_in_room() performance.';
