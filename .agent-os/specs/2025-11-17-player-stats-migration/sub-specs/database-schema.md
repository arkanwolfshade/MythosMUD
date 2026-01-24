# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-11-17-player-stats-migration/spec.md

## Changes

### Player Stats Reset Migration

**Purpose:** Reset all existing player stats to new defaults (50 for all core attributes) as part of the 1-20 to 1-100 range migration.

**Migration File:** `server/sql/migrations/XXX_reset_player_stats_to_1_100_range.sql`

## Specifications

### SQL Migration Script

```sql
-- Migration: Reset Player Stats to 1-100 Range Defaults
-- Description: Updates all player stats to new defaults (50 for core attributes)
--              as part of migrating from 1-20 to 1-100 range

-- Update all existing player stats to new defaults
UPDATE players
SET stats = jsonb_set(
    jsonb_set(
        jsonb_set(
            jsonb_set(
                jsonb_set(
                    jsonb_set(
                        stats,
                        '{strength}',
                        '50'::jsonb
                    ),
                    '{dexterity}',
                    '50'::jsonb
                ),
                '{constitution}',
                '50'::jsonb
            ),
            '{intelligence}',
            '50'::jsonb
        ),
        '{wisdom}',
        '50'::jsonb
    ),
    '{charisma}',
    '50'::jsonb
)
WHERE stats IS NOT NULL;

-- Ensure all new players get correct defaults (if migration 006 sets defaults, update it)
-- This is handled in the Player model default, but verify migration 006 is correct
```

### Default Stats Structure

The default stats JSONB structure should be:

```json
{
  "strength": 50,
  "dexterity": 50,
  "constitution": 50,
  "intelligence": 50,
  "wisdom": 50,
  "charisma": 50,
  "lucidity": 100,
  "occult_knowledge": 0,
  "fear": 0,
  "corruption": 0,
  "cult_affiliation": 0,
  "current_health": 100,
  "position": "standing"
}
```

## Rationale

**Data Reset Strategy:** All existing player stats are reset to 50 (the new midpoint) rather than scaling, as per user requirements. This ensures a clean slate for the new stat system.

**Preservation of Other Stats:** Lucidity, occult_knowledge, fear, corruption, cult_affiliation, current_health, and position are preserved as-is since they are not part of the core attribute migration.

**JSONB Update:** Using `jsonb_set()` ensures we only update the specific stat fields without affecting other JSONB data in the stats column.

**Migration Safety:** The WHERE clause ensures we only update rows with existing stats data, preventing errors on NULL values.

## Verification

After migration, verify:

1. All players have core attributes set to 50
2. Other stats (lucidity, current_health, etc.) are preserved
3. New player creation uses correct defaults (50 for core attributes)
4. No data loss or corruption occurred
