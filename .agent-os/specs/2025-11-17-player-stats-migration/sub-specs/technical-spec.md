# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-17-player-stats-migration/spec.md

## Technical Requirements

### Core Model Changes

**File:** `server/models/game.py`

- Update `Stats` model Field constraints:
  - Change `ge=1, le=20` to `ge=1, le=100` for: strength, dexterity, constitution, intelligence, wisdom, charisma
  - Keep existing constraints for lucidity, occult_knowledge, fear, corruption, cult_affiliation (0-100)

- Update `get_attribute_modifier()` method:
  - Current: `(attr_value - 10) // 2`
  - New: `(attr_value - 50) // 2`
  - Update default fallback from 10 to 50

- Update `max_health` computed field:
  - Current: `(self.constitution or 10) * 10`
  - New: `(self.constitution or 50)`
  - Remove multiplication, use direct value

- Update `max_lucidity` computed field:
  - Current: `(self.wisdom or 10) * 5`
  - New: `(self.wisdom or 50)`
  - Remove multiplication, use direct value

### Stats Generator Updates

**File:** `server/game/stats_generator.py`

- Update class constants:
  - `MIN_STAT`: 3 → 15
  - `MAX_STAT`: 18 → 90

- Update `generate_random_stats()`:

  Change `randint(3, 18)` → `randint(15, 90)` for all six attributes

- Update `_roll_3d6()`:

  Change `randint(3, 18)` → `randint(15, 90)` for all attributes

- Update `_roll_4d6_drop_lowest()`:
  - Modify roll calculation to produce 15-90 range
  - Current: 4d6 drop lowest (range 3-18)
  - New: Scale to 15-90 range (multiply by 5)

- Update `_roll_point_buy()`:
  - Update base stats from 8 to 40 (scaled by 5)
  - Update point costs for 1-100 range
  - Adjust maximum stat cap from 18 to 90

- Update `CLASS_PREREQUISITES`:

  - Scale all values by 5:
    - 10 → 50
    - 12 → 60
    - 14 → 70
  - Update all class prerequisite entries

### Configuration Updates

**File:** `server/config/models.py`

- Update `PlayerStatsConfig`:

  - Change default values: 10 → 50 for strength, dexterity, constitution, intelligence, wisdom, charisma
  - Update `validate_stat_range()`:
    - Change validation from `1 <= v <= 20` to `1 <= v <= 100`
    - Update error message: "Stats must be between 1 and 20" → "Stats must be between 1 and 100"

### Database Model Updates

**File:** `server/models/player.py`

- Update default stats in `Player` model Column default:
  - Change all core attributes from 10 to 50
  - Update JSONB default lambda function

- Update `get_stats()` fallback defaults:

  Change all core attributes from 10 to 50 in fallback dictionary

### Combat System Updates

**File:** `server/npc/combat_integration.py`

- Update `calculate_damage()` method:

  - Strength bonus calculation:
    - Current: `(strength_mod - 10) // 2`
    - New: `(strength_mod - 50) // 2`
  - Damage reduction calculation:
    - Current: `(target_con - 10) // 4`
    - New: `(target_con - 50) // 4`
  - Update default fallback values: 10 → 50

### Database Migration

**File:** `server/sql/migrations/` (create new migration file)

- Create SQL migration script to:
  - Reset all existing player stats to new defaults
  - Update all core attributes (strength, dexterity, constitution, intelligence, wisdom, charisma) to 50
  - Preserve other stats (lucidity, occult_knowledge, fear, corruption, cult_affiliation, current_health)
  - Update default stats in migration 006 if it sets defaults

### Test Updates

**File:** `server/tests/unit/models/test_models.py`

- Update stat range assertions:
  - `3 <= stat <= 18` → `15 <= stat <= 90` (for random generation)
  - `1 <= stat <= 20` → `1 <= stat <= 100` (for validation)

- Update `test_stats_max_health_property`:

  Change test values and expected results for new formula

- Update `test_stats_max_lucidity_property`:

  Change test values and expected results for new formula

- Update `test_stats_get_attribute_modifier`:

  Update test values and expected modifier calculations

**File:** `server/tests/unit/player/test_stats_generator.py`

- Update `MIN_STAT`/`MAX_STAT` assertions: 3/18 → 15/90
- Update all range assertions: `3 <= stat <= 18` → `15 <= stat <= 90`
- Update class prerequisite tests with scaled values (12→60, 14→70, etc.)
- Update point buy test ranges and expected values

**File:** `server/tests/unit/infrastructure/test_config.py`

- Update `TestPlayerStatsConfig`:
  - Change validation error message assertions
  - Update test ranges from 1-20 to 1-100
  - Update default value assertions from 10 to 50

**File:** `server/tests/integration/npc/test_combat_database_schema.py`

- Update stat range assertions: `1 <= stat <= 20` → `1 <= stat <= 100`

**File:** `server/tests/unit/api/test_players.py`

- Update mock generator `MIN_STAT`/`MAX_STAT`: 3/18 → 15/90

### Client-Side Verification

**Files to verify (no changes expected, but verify):**

- `client/src/components/ui/StatusPanel.tsx`
- `client/src/components/GameTerminalPresentation.tsx`
- `client/tests/e2e/runtime/fixtures/test-data.ts`

- Verify stat display handles 1-100 range correctly
- Verify no TypeScript errors or type mismatches
- Update test fixtures if they have hardcoded stat values

## External Dependencies

No new external dependencies required. This migration uses existing Pydantic, SQLAlchemy, and testing frameworks.
