# Spec Requirements Document

> Spec: Player Stats Migration (1-20 to 1-100 Range)
> Created: 2025-11-17

## Overview

Migrate all player statistics from the 1-20 range to a 1-100 range to provide greater granularity and flexibility in character progression. This migration will update model constraints, stat generation algorithms, derived stat formulas, combat calculations, and all related tests while resetting existing player data to new defaults.

## User Stories

### As a Game Developer

As a game developer, I want player stats to use a 1-100 range instead of 1-20, so that I can provide more nuanced character progression and finer-grained stat differences between players.

**Workflow:**

1. All existing player stats are reset to new defaults (50 for all core attributes)
2. New character creation generates stats in the 15-90 range (scaled from previous 3-18)
3. All formulas and calculations are updated to work with the new range
4. Class prerequisites are scaled proportionally (e.g., 12 → 60, 14 → 70)
5. Combat damage calculations use the new midpoint (50 instead of 10)
6. Derived stats (max health, max lucidity) use direct stat values instead of multipliers

### As a Player

As a player, I want my character stats to be displayed and calculated using the new 1-100 range, so that I can see more detailed stat information and experience more granular character progression.

**Workflow:**

1. Player views character stats in the UI and sees values in 1-100 range
2. Player creates a new character and receives stats rolled in 15-90 range
3. Player's max health and lucidity are calculated directly from constitution and wisdom stats
4. Combat damage calculations properly reflect the new stat ranges

## Spec Scope

1. **Model Constraints Update** - Update Pydantic Field constraints in Stats model from `ge=1, le=20` to `ge=1, le=100` for all six core attributes (strength, dexterity, constitution, intelligence, wisdom, charisma)

2. **Stat Generation System** - Update StatsGenerator to use 15-90 range for random stat generation (scaled from 3-18), update all rolling methods (3d6, 4d6_drop_lowest, point_buy), and scale class prerequisites by 5x

3. **Formula Updates** - Update attribute modifier formula from `(attr_value - 10) // 2` to `(attr_value - 50) // 2`, change max_health from `constitution * 10` to `constitution`, and change max_lucidity from `wisdom * 5` to `wisdom`

4. **Combat System Updates** - Update combat damage calculations to use 50 as the midpoint instead of 10 for strength bonuses and constitution-based damage reduction

5. **Configuration Updates** - Update PlayerStatsConfig defaults from 10 to 50 and validation from 1-20 to 1-100 range

6. **Database Migration** - Create SQL migration script to reset all existing player stats to new defaults (50 for all core attributes)

7. **Test Suite Updates** - Update all unit tests, integration tests, and API tests to reflect new stat ranges, formulas, and expected values

8. **Client Display Verification** - Verify client-side components correctly display and handle the 1-100 stat range

## Out of Scope

Migration of existing player stats by scaling (all stats will be reset to defaults)

- Changes to lucidity, occult_knowledge, fear, corruption, or cult_affiliation ranges (these remain 0-100)
- Changes to current_health calculation or health regeneration formulas
- UI redesign for stat display (existing UI should handle the range correctly)
- Changes to NPC stat ranges (NPCs may be updated separately in future work)

## Expected Deliverable

1. All player stats successfully migrated to 1-100 range with all existing player data reset to new defaults (50 for core attributes)

2. All stat generation, validation, and calculation formulas updated and tested to work correctly with the new range

3. All tests passing with updated assertions and expected values reflecting the new stat system

4. Client UI correctly displays and handles stats in the 1-100 range without errors or display issues
