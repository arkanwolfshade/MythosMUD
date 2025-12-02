# Spec Tasks

## Tasks

- [x] 1. Update Core Stats Model
  - [x] 1.1 Update Stats model Field constraints from `ge=1, le=20` to `ge=1, le=100` for all six core attributes in `server/models/game.py`
  - [x] 1.2 Update `get_attribute_modifier()` method formula from `(attr_value - 10) // 2` to `(attr_value - 50) // 2` and update default fallback from 10 to 50
  - [x] 1.3 Update `max_health` computed field from `(self.constitution or 10) * 10` to `(self.constitution or 50)`
  - [x] 1.4 Update `max_lucidity` computed field from `(self.wisdom or 10) * 5` to `(self.wisdom or 50)`
  - [x] 1.5 Update tests in `server/tests/unit/models/test_models.py`: update range assertions, max_health test, max_lucidity test, and attribute modifier test
  - [x] 1.6 Verify all model tests pass (Note: 2 tests will pass after Task 2 updates stats generator)

- [x] 2. Update Stats Generator System
  - [x] 2.1 Update `MIN_STAT` and `MAX_STAT` constants from 3/18 to 15/90 in `server/game/stats_generator.py`
  - [x] 2.2 Update `generate_random_stats()` to use `randint(15, 90)` instead of `randint(3, 18)`
  - [x] 2.3 Update `_roll_3d6()` to use `randint(15, 90)` for all attributes
  - [x] 2.4 Update `_roll_4d6_drop_lowest()` to produce 15-90 range (scale by 5)
  - [x] 2.5 Update `_roll_point_buy()`: change base stats from 8 to 40, update point costs for 1-100 range, adjust max stat cap from 18 to 90
  - [x] 2.6 Update `CLASS_PREREQUISITES` by scaling all values by 5 (10→50, 12→60, 14→70)
  - [x] 2.7 Update tests in `server/tests/unit/player/test_stats_generator.py`: update MIN_STAT/MAX_STAT assertions, range checks, class prerequisite tests, and point buy tests
  - [x] 2.8 Verify all stats generator tests pass

- [x] 3. Update Configuration System
  - [x] 3.1 Update `PlayerStatsConfig` default values from 10 to 50 for all core attributes in `server/config/models.py`
  - [x] 3.2 Update `validate_stat_range()` to validate 1-100 range instead of 1-20
  - [x] 3.3 Update error message from "Stats must be between 1 and 20" to "Stats must be between 1 and 100"
  - [x] 3.4 Update tests in `server/tests/unit/infrastructure/test_config.py`: update validation error message assertions, test ranges, and default value assertions
  - [x] 3.5 Verify all config tests pass

- [x] 4. Update Database Model Defaults
  - [x] 4.1 Update default stats in `Player` model Column default from 10 to 50 for all core attributes in `server/models/player.py`
  - [x] 4.2 Update `get_stats()` fallback defaults from 10 to 50 for all core attributes
  - [x] 4.3 Verify database model changes work correctly

- [x] 5. Update Combat System Calculations
  - [x] 5.1 Update `calculate_damage()` in `server/npc/combat_integration.py`: change strength bonus from `(strength_mod - 10) // 2` to `(strength_mod - 50) // 2`
  - [x] 5.2 Update damage reduction calculation from `(target_con - 10) // 4` to `(target_con - 50) // 4`
  - [x] 5.3 Update default fallback values from 10 to 50
  - [x] 5.4 Verify combat calculations work correctly with new formulas

- [x] 6. Create Database Migration Script
  - [x] 6.1 Create new SQL migration file in `db/migrations/` to reset all existing player stats to new defaults (50 for core attributes)
  - [x] 6.2 Ensure migration preserves other stats (lucidity, occult_knowledge, fear, corruption, cult_affiliation, current_health, position)
  - [x] 6.3 Verify migration script syntax and logic
  - [x] 6.4 Update migration 006 if it sets default stats

- [x] 7. Update Integration and API Tests
  - [x] 7.1 Update stat range assertions in `server/tests/integration/npc/test_combat_database_schema.py` from `1 <= stat <= 20` to `1 <= stat <= 100`
  - [x] 7.2 Update mock generator `MIN_STAT`/`MAX_STAT` in `server/tests/unit/api/test_players.py` from 3/18 to 15/90
  - [x] 7.3 Verify all integration and API tests pass

- [x] 8. Verify Client-Side Display
  - [x] 8.1 Verify `client/src/components/ui/StatusPanel.tsx` handles 1-100 range correctly (no hardcoded ranges, displays as numbers)
  - [x] 8.2 Verify `client/src/components/GameTerminalPresentation.tsx` handles 1-100 range correctly (no hardcoded ranges, displays as numbers)
  - [x] 8.3 Update test fixtures in `client/tests/e2e/runtime/fixtures/test-data.ts` if they have hardcoded stat values (updated from 10 to 50)
  - [x] 8.4 Verify no TypeScript errors or type mismatches (no type constraints on stat values)
  - [x] 8.5 Test client display with actual stat values in 1-100 range (client displays stats as numbers without range validation)

- [x] 9. Final Verification and Testing
  - [x] 9.1 Run full test suite and verify all tests pass
  - [x] 9.2 Verify stat generation produces values in correct ranges (15-90 for random, 1-100 for validation)
  - [x] 9.3 Verify attribute modifiers calculate correctly with new formula
  - [x] 9.4 Verify max health and max lucidity calculations work correctly
  - [x] 9.5 Verify combat damage calculations work correctly
  - [x] 9.6 Verify class prerequisites validation works with scaled values
  - [x] 9.7 Verify database migration resets stats correctly (if applicable in test environment)
