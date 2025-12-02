-- Migration: Rename sanity system to lucidity system
-- Date: 2025-12-02
-- Description: Systematically rename all sanity-related tables, columns, indexes, and constraints to lucidity
-- This is a pure terminology change with no structural modifications

-- Begin transaction
BEGIN;

-- ============================================================================
-- STEP 1: Rename Tables
-- ============================================================================

ALTER TABLE IF EXISTS sanity_cooldowns RENAME TO lucidity_cooldowns;
ALTER TABLE IF EXISTS sanity_exposure_state RENAME TO lucidity_exposure_state;
ALTER TABLE IF EXISTS sanity_adjustment_log RENAME TO lucidity_adjustment_log;
ALTER TABLE IF EXISTS player_sanity RENAME TO player_lucidity;

-- ============================================================================
-- STEP 2: Rename Columns in player_lucidity
-- ============================================================================

ALTER TABLE IF EXISTS player_lucidity RENAME COLUMN current_san TO current_lcd;

-- Note: Other columns (current_tier, liabilities, etc.) do not contain "san" in their names

-- ============================================================================
-- STEP 3: Rename Indexes
-- ============================================================================

-- Player lucidity indexes
ALTER INDEX IF EXISTS idx_player_sanity_tier RENAME TO idx_player_lucidity_tier;

-- Adjustment log indexes
ALTER INDEX IF EXISTS idx_sanity_adjustment_player_id RENAME TO idx_lucidity_adjustment_player_id;
ALTER INDEX IF EXISTS idx_sanity_adjustment_player_created RENAME TO idx_lucidity_adjustment_player_created;

-- Exposure state indexes
ALTER INDEX IF EXISTS idx_sanity_exposure_player_id RENAME TO idx_lucidity_exposure_player_id;

-- Cooldowns indexes
ALTER INDEX IF EXISTS idx_sanity_cooldowns_player_id RENAME TO idx_lucidity_cooldowns_player_id;

-- ============================================================================
-- STEP 4: Rename Constraints
-- ============================================================================

-- Player lucidity constraints (use actual constraint names from database)
ALTER TABLE IF EXISTS player_lucidity RENAME CONSTRAINT player_sanity_current_san_check TO player_lucidity_current_luc_check;
ALTER TABLE IF EXISTS player_lucidity RENAME CONSTRAINT player_sanity_current_tier_check TO player_lucidity_current_tier_check;
ALTER TABLE IF EXISTS player_lucidity RENAME CONSTRAINT player_sanity_player_id_fkey TO player_lucidity_player_id_fkey;
ALTER TABLE IF EXISTS player_lucidity RENAME CONSTRAINT player_sanity_pkey TO player_lucidity_pkey;

-- Adjustment log constraints
ALTER TABLE IF EXISTS lucidity_adjustment_log RENAME CONSTRAINT sanity_adjustment_log_pkey TO lucidity_adjustment_log_pkey;
ALTER TABLE IF EXISTS lucidity_adjustment_log RENAME CONSTRAINT sanity_adjustment_log_player_id_fkey TO lucidity_adjustment_log_player_id_fkey;

-- Exposure state constraints
ALTER TABLE IF EXISTS lucidity_exposure_state RENAME CONSTRAINT sanity_exposure_state_pkey TO lucidity_exposure_state_pkey;
ALTER TABLE IF EXISTS lucidity_exposure_state RENAME CONSTRAINT sanity_exposure_state_player_id_fkey TO lucidity_exposure_state_player_id_fkey;
ALTER TABLE IF EXISTS lucidity_exposure_state RENAME CONSTRAINT sanity_exposure_state_player_id_entity_archetype_key TO lucidity_exposure_state_player_id_entity_archetype_key;

-- Cooldowns constraints
ALTER TABLE IF EXISTS lucidity_cooldowns RENAME CONSTRAINT sanity_cooldowns_pkey TO lucidity_cooldowns_pkey;
ALTER TABLE IF EXISTS lucidity_cooldowns RENAME CONSTRAINT sanity_cooldowns_player_id_fkey TO lucidity_cooldowns_player_id_fkey;
ALTER TABLE IF EXISTS lucidity_cooldowns RENAME CONSTRAINT sanity_cooldowns_player_id_action_code_key TO lucidity_cooldowns_player_id_action_code_key;

-- ============================================================================
-- STEP 5: Update Check Constraint Definitions (requires DROP/ADD)
-- ============================================================================

-- Update the range check constraint to use new column name
-- Drop the renamed constraint from Step 4
ALTER TABLE IF EXISTS player_lucidity DROP CONSTRAINT IF EXISTS player_lucidity_current_luc_check;
ALTER TABLE IF EXISTS player_lucidity ADD CONSTRAINT player_lucidity_current_lcd_check
    CHECK (current_lcd BETWEEN -100 AND 100);

-- Tier constraint already references tier values (not column names), so just keep it
-- No need to recreate since current_tier column name didn't change

-- ============================================================================
-- STEP 6: Update Comments (if any exist)
-- ============================================================================

COMMENT ON TABLE player_lucidity IS 'Authoritative lucidity state for a single investigator';
COMMENT ON TABLE lucidity_adjustment_log IS 'Immutable ledger for every lucidity gain or loss event';
COMMENT ON TABLE lucidity_exposure_state IS 'Tracks repeated exposure to particular eldritch archetypes';
COMMENT ON TABLE lucidity_cooldowns IS 'Cooldown tracker for recovery rituals and hallucination timers';

COMMENT ON COLUMN player_lucidity.current_lcd IS 'Current lucidity value (-100 to +100)';
COMMENT ON COLUMN player_lucidity.current_tier IS 'Current lucidity tier (lucid/uneasy/fractured/deranged/catatonic)';

-- Commit transaction
COMMIT;

-- ============================================================================
-- Verification Queries
-- ============================================================================

-- Uncomment these to verify the migration
-- \dt player_lucidity
-- \dt lucidity_*
-- \d player_lucidity
-- SELECT COUNT(*) FROM player_lucidity;
-- SELECT COUNT(*) FROM lucidity_adjustment_log;
