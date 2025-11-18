# Spec Tasks

## Tasks

- [ ] 1. Update Core Stats Model
  - [ ] 1.1 Update Stats model Field constraints from `ge=1, le=20` to `ge=1, le=100` for all six core attributes in `server/models/game.py`
  - [ ] 1.2 Update `get_attribute_modifier()` method formula from `(attr_value - 10) // 2` to `(attr_value - 50) // 2` and update default fallback from 10 to 50
  - [ ] 1.3 Update `max_health` computed field from `(self.constitution or 10) * 10` to `(self.constitution or 50)`
  - [ ] 1.4 Update `max_sanity` computed field from `(self.wisdom or 10) * 5` to `(self.wisdom or 50)`
  - [ ] 1.5 Update tests in `server/tests/unit/models/test_models.py`: update range assertions, max_health test, max_sanity test, and attribute modifier test
  - [ ] 1.6 Verify all model tests pass

- [ ] 2. Update Stats Generator System
  - [ ] 2.1 Update `MIN_STAT` and `MAX_STAT` constants from 3/18 to 15/90 in `server/game/stats_generator.py`
  - [ ] 2.2 Update `generate_random_stats()` to use `randint(15, 90)` instead of `randint(3, 18)`
  - [ ] 2.3 Update `_roll_3d6()` to use `randint(15, 90)` for all attributes
  - [ ] 2.4 Update `_roll_4d6_drop_lowest()` to produce 15-90 range (scale by 5)
  - [ ] 2.5 Update `_roll_point_buy()`: change base stats from 8 to 40, update point costs for 1-100 range, adjust max stat cap from 18 to 90
  - [ ] 2.6 Update `CLASS_PREREQUISITES` by scaling all values by 5 (10→50, 12→60, 14→70)
  - [ ] 2.7 Update tests in `server/tests/unit/player/test_stats_generator.py`: update MIN_STAT/MAX_STAT assertions, range checks, class prerequisite tests, and point buy tests
  - [ ] 2.8 Verify all stats generator tests pass

- [ ] 3. Update Configuration System
  - [ ] 3.1 Update `PlayerStatsConfig` default values from 10 to 50 for all core attributes in `server/config/models.py`
  - [ ] 3.2 Update `validate_stat_range()` to validate 1-100 range instead of 1-20
  - [ ] 3.3 Update error message from "Stats must be between 1 and 20" to "Stats must be between 1 and 100"
  - [ ] 3.4 Update tests in `server/tests/unit/infrastructure/test_config.py`: update validation error message assertions, test ranges, and default value assertions
  - [ ] 3.5 Verify all config tests pass

- [ ] 4. Update Database Model Defaults
  - [ ] 4.1 Update default stats in `Player` model Column default from 10 to 50 for all core attributes in `server/models/player.py`
  - [ ] 4.2 Update `get_stats()` fallback defaults from 10 to 50 for all core attributes
  - [ ] 4.3 Verify database model changes work correctly

- [ ] 5. Update Combat System Calculations
  - [ ] 5.1 Update `calculate_damage()` in `server/npc/combat_integration.py`: change strength bonus from `(strength_mod - 10) // 2` to `(strength_mod - 50) // 2`
  - [ ] 5.2 Update damage reduction calculation from `(target_con - 10) // 4` to `(target_con - 50) // 4`
  - [ ] 5.3 Update default fallback values from 10 to 50
  - [ ] 5.4 Verify combat calculations work correctly with new formulas

- [ ] 6. Create Database Migration Script
  - [ ] 6.1 Create new SQL migration file in `server/sql/migrations/` to reset all existing player stats to new defaults (50 for core attributes)
  - [ ] 6.2 Ensure migration preserves other stats (sanity, occult_knowledge, fear, corruption, cult_affiliation, current_health, position)
  - [ ] 6.3 Verify migration script syntax and logic
  - [ ] 6.4 Update migration 006 if it sets default stats

- [ ] 7. Update Integration and API Tests
  - [ ] 7.1 Update stat range assertions in `server/tests/integration/npc/test_combat_database_schema.py` from `1 <= stat <= 20` to `1 <= stat <= 100`
  - [ ] 7.2 Update mock generator `MIN_STAT`/`MAX_STAT` in `server/tests/unit/api/test_players.py` from 3/18 to 15/90
  - [ ] 7.3 Verify all integration and API tests pass

- [ ] 8. Verify Client-Side Display
  - [ ] 8.1 Verify `client/src/components/ui/StatusPanel.tsx` handles 1-100 range correctly
  - [ ] 8.2 Verify `client/src/components/GameTerminalPresentation.tsx` handles 1-100 range correctly
  - [ ] 8.3 Update test fixtures in `client/tests/e2e/runtime/fixtures/test-data.ts` if they have hardcoded stat values
  - [ ] 8.4 Verify no TypeScript errors or type mismatches
  - [ ] 8.5 Test client display with actual stat values in 1-100 range

- [ ] 9. Final Verification and Testing
  - [ ] 9.1 Run full test suite and verify all tests pass
  - [ ] 9.2 Verify stat generation produces values in correct ranges (15-90 for random, 1-100 for validation)
  - [ ] 9.3 Verify attribute modifiers calculate correctly with new formula
  - [ ] 9.4 Verify max health and max sanity calculations work correctly
  - [ ] 9.5 Verify combat damage calculations work correctly
  - [ ] 9.6 Verify class prerequisites validation works with scaled values
  - [ ] 9.7 Verify database migration resets stats correctly (if applicable in test environment)
