# Legacy Test Files - Consolidation Guide

> *Created during test suite refactoring - October 14, 2025*

## Overview

During the migration to the new hierarchical test structure, 28 test files were marked with `*_legacy.py` suffix. These files contain **330+ valid tests** representing alternative implementations, additional coverage, and different testing approaches.

**Status:** Files are properly organized in correct categories and can run alongside their primary counterparts.

**Recommendation:** Consolidate gradually over time during feature work, not as a big-bang effort.

---

## Legacy Files Inventory

### Total: 28 files with 330+ tests

| Primary Test File                                        | Legacy File(s)                                    | Test Count | Priority | Notes                   |
| -------------------------------------------------------- | ------------------------------------------------- | ---------- | -------- | ----------------------- |
| **Unit/Utilities** (3 files, 93 tests)                   |                                                   |            |
| `unit/utilities/test_error_handlers.py`                  | `test_legacy_error_handlers_legacy.py`            | 57         | High     | Large test suite        |
| `unit/utilities/test_error_handlers.py`                  | `test_standardized_error_handling_legacy.py`      | 17         | Medium   | Error handling patterns |
| `unit/utilities/test_rate_limiter.py`                    | `test_utils_rate_limiter_legacy.py`               | 19         | Medium   | Rate limiting tests     |
| **Unit/NPC** (2 files, 71 tests)                         |                                                   |            |          |
| `unit/npc/test_npc_admin_api.py`                         | `test_npc_admin_api_full_legacy.py`               | 50         | High     | Comprehensive API tests |
| `unit/npc/test_npc_population_control.py`                | `test_npc_population_management_legacy.py`        | 21         | Medium   | Population mgmt         |
| **Unit/Infrastructure** (3 files, 36 tests)              |                                                   |            |          |
| `unit/infrastructure/test_dependency_injection.py`       | `test_dependency_injection_functions_legacy.py`   | 19         | Medium   | DI functions            |
| `unit/infrastructure/test_dependency_injection.py`       | `test_dependency_functions_legacy.py`             | 14         | Medium   | More DI tests           |
| `unit/infrastructure/test_lifespan.py`                   | `test_lifespan_legacy.py`                         | 3          | Low      | App lifespan            |
| **Coverage** (2 files, 32 tests)                         |                                                   |            |          |
| `coverage/test_error_logging_coverage.py`                | `test_error_logging_integration_legacy.py`        | 28         | Medium   | Logging coverage        |
| `coverage/test_command_handler_coverage.py`              | `test_command_handler_unified_coverage_legacy.py` | 4          | Low      | Command coverage        |
| **Unit/Services** (1 file, 14 tests)                     |                                                   |            |          |
| `unit/services/test_dependency_injection.py`             | `test_dependency_injection_simple_legacy.py`      | 14         | Medium   | Service DI              |
| **Unit/Player** (2 files, 15 tests)                      |                                                   |            |          |
| `unit/player/test_stats_generator.py`                    | `test_stats_random_generation_legacy.py`          | 13         | Medium   | Random stats            |
| `unit/player/test_player_service.py`                     | `test_player_service_layer_legacy.py`             | 2          | Low      | Player service          |
| **Unit/API** (1 file, 12 tests)                          |                                                   |            |          |
| `unit/api/test_monitoring_endpoints.py`                  | `test_monitoring_api_legacy.py`                   | 12         | Medium   | Monitoring API          |
| **Unit/World** (2 files, 18 tests)                       |                                                   |            |          |
| `unit/world/test_movement_service.py`                    | `test_movement_comprehensive_legacy.py`           | 10         | Medium   | Movement tests          |
| `unit/world/test_room_service.py`                        | `test_room_service_layer_legacy.py`               | 8          | Low      | Room service            |
| **Unit/Chat** (3 files, 13 tests)                        |                                                   |            |          |
| `unit/chat/test_broadcasting_strategies.py`              | `test_broadcasting_strategies_impl_legacy.py`     | 9          | Medium   | Broadcasting impl       |
| `unit/chat/test_local_channel.py`                        | `test_local_channel_commands_legacy.py`           | 3          | Low      | Channel commands        |
| `unit/chat/test_emote_filtering.py`                      | `test_emote_types_filtering_legacy.py`            | 1          | Low      | Emote filtering         |
| **Unit/Realtime** (1 file, 8 tests)                      |                                                   |            |          |
| `unit/realtime/test_nats_message_handler.py`             | `test_nats_message_handler_subzone_legacy.py`     | 8          | Medium   | NATS subzone            |
| **Unit/Commands** (2 files, 8 tests)                     |                                                   |            |          |
| `unit/commands/test_command_handler.py`                  | `test_command_handler_v2_legacy.py`               | 7          | Medium   | Handler v2              |
| `unit/commands/test_command_handler.py`                  | `test_unified_command_handler_legacy.py`          | 1          | Low      | Unified handler         |
| **Unit/Events** (1 file, 2 tests)                        |                                                   |            |          |
| `unit/events/test_event_handler.py`                      | `test_event_handler_broadcasting_legacy.py`       | 2          | Low      | Event broadcasting      |
| **Integration** (3 files, 11 tests)                      |                                                   |            |          |
| `integration/events/test_event_flow_integration.py`      | `test_real_event_flow_legacy.py`                  | 1          | Low      | Event flow              |
| `integration/comprehensive/test_simple_integration.py`   | `test_simple_connection_events_legacy.py`         | 5          | Low      | Connection events       |
| `integration/npc/test_npc_admin_commands_integration.py` | `test_npc_admin_commands_fixed_legacy.py`         | 5          | Medium   | NPC commands            |
| **Monitoring** (1 file, 2 tests)                         |                                                   |            |          |
| `monitoring/test_occupant_count_integration.py`          | `test_occupant_count_simple_legacy.py`            | 2          | Low      | Occupant count          |
| **Regression** (1 file, 1 test)                          |                                                   |            |          |
| `regression/test_self_message_bug.py`                    | `test_self_message_exclusion_legacy.py`           | 1          | Low      | Self-message fix        |

**Total: 28 legacy files containing 330+ tests**

---

## Consolidation Strategy

### Immediate (Done)
- ✅ Empty legacy files removed (1 file)
- ✅ Legacy files organized in correct categories
- ✅ All legacy tests are discoverable and runnable

### Short-term (As-Needed)
**Approach:** Consolidate during feature work, not as bulk task

When working on a feature, if you touch a test file with a legacy counterpart:
1. Review the legacy file for unique tests
2. Merge unique tests into primary file
3. Remove duplicates
4. Delete legacy file
5. Run tests to validate

### Priority Order

**High Priority (Large test suites):**
1. `unit/utilities/test_legacy_error_handlers_legacy.py` (57 tests)
2. `unit/npc/test_npc_admin_api_full_legacy.py` (50 tests)
3. `coverage/test_error_logging_integration_legacy.py` (28 tests)
4. `unit/npc/test_npc_population_management_legacy.py` (21 tests)

**Medium Priority (10-19 tests):**
5. `unit/utilities/test_utils_rate_limiter_legacy.py` (19 tests)
6. `unit/infrastructure/test_dependency_injection_functions_legacy.py` (19 tests)
7. `unit/utilities/test_standardized_error_handling_legacy.py` (17 tests)
8. `unit/infrastructure/test_dependency_functions_legacy.py` (14 tests)
9. `unit/services/test_dependency_injection_simple_legacy.py` (14 tests)
10. `unit/player/test_stats_random_generation_legacy.py` (13 tests)
11. `unit/api/test_monitoring_api_legacy.py` (12 tests)
12. `unit/world/test_movement_comprehensive_legacy.py` (10 tests)

**Low Priority (<10 tests):**
- All others (16 files, 75 tests total)

---

## Consolidation Process

### For Each Legacy File:

1. **Review Primary File**
   ```bash
   # Open primary file
   code server/tests/unit/player/test_player_service.py
   ```

2. **Review Legacy File**
   ```bash
   # Open legacy file
   code server/tests/unit/player/test_player_service_layer_legacy.py
   ```

3. **Identify Unique Tests**
   - Compare test names
   - Look for different test approaches
   - Check for additional edge cases
   - Note any setup/fixture differences

4. **Merge Unique Content**
   - Copy unique tests to primary file
   - Update imports if needed
   - Preserve docstrings and comments
   - Maintain test organization

5. **Validate**
   ```bash
   # Run tests for the specific file
   pytest server/tests/unit/player/test_player_service.py -v
   ```

6. **Remove Legacy File**
   ```bash
   # Once validated
   rm server/tests/unit/player/test_player_service_layer_legacy.py
   ```

---

## Why Keep Legacy Files for Now?

### Benefits of Gradual Consolidation

1. **Risk Mitigation**
   - No loss of test coverage
   - Tests remain runnable
   - Can review incrementally

2. **Quality**
   - Careful review of each test
   - Preserve unique test approaches
   - Avoid hasty merges

3. **Efficiency**
   - Consolidate during related work
   - Context already loaded
   - Natural workflow integration

4. **Validation**
   - Can compare behavior before/after
   - Easy rollback if needed
   - Incremental validation

### Current State is Acceptable

- ✅ All 28 legacy files are in correct categories
- ✅ All tests are discoverable by pytest
- ✅ All tests can run successfully
- ✅ Clear naming (`*_legacy.py`) indicates status
- ✅ No confusion about which file to use (primary file is obvious)

---

## Quick Wins (Easy Consolidations)

### Very Low Test Count (1-3 tests)

These can be reviewed and consolidated quickly:

1. `regression/test_self_message_exclusion_legacy.py` (1 test)
   - Target: `regression/test_self_message_bug.py`
   - Effort: 5 minutes

2. `integration/events/test_real_event_flow_legacy.py` (1 test)
   - Target: `integration/events/test_event_flow_integration.py`
   - Effort: 5 minutes

3. `unit/chat/test_emote_types_filtering_legacy.py` (1 test)
   - Target: `unit/chat/test_emote_filtering.py`
   - Effort: 5 minutes

4. `unit/commands/test_unified_command_handler_legacy.py` (1 test)
   - Target: `unit/commands/test_command_handler.py`
   - Effort: 5 minutes

5. `unit/player/test_player_service_layer_legacy.py` (2 tests)
   - Target: `unit/player/test_player_service.py`
   - Effort: 10 minutes

6. `monitoring/test_occupant_count_simple_legacy.py` (2 tests)
   - Target: `monitoring/test_occupant_count_integration.py`
   - Effort: 10 minutes

7. `unit/events/test_event_handler_broadcasting_legacy.py` (2 tests)
   - Target: `unit/events/test_event_handler.py`
   - Effort: 10 minutes

8. `unit/infrastructure/test_lifespan_legacy.py` (3 tests)
   - Target: `unit/infrastructure/test_lifespan.py`
   - Effort: 10 minutes

9. `unit/chat/test_local_channel_commands_legacy.py` (3 tests)
   - Target: `unit/chat/test_local_channel.py`
   - Effort: 10 minutes

**Total Quick Wins: 9 files, 16 tests, ~1 hour total effort**

---

## Future Consolidation Tracking

### When to Consolidate

**Trigger Events:**
- Working on related feature
- Updating tests for bug fix
- Refactoring component
- Reviewing test coverage

**Process:**
1. Notice legacy file exists
2. Review for unique content
3. Merge what's unique
4. Remove legacy file
5. Update this guide (remove from list)

### Progress Tracking

As legacy files are consolidated, update this section:

**Consolidated (0/28):**
- (none yet)

**Remaining (28/28):**
- All 28 legacy files remain

**Target:** Consolidate opportunistically over next 3-6 months

---

## Commands Reference

```bash
# List all legacy files
python server/tests/scripts/consolidate_legacy.py --list

# Analyze legacy files
python server/tests/scripts/consolidate_legacy.py --analyze

# Track overall migration
python server/tests/scripts/track_migration.py
```

---

## Decision Rationale

**Why not consolidate all now?**

1. **Volume:** 330+ tests across 28 files require careful review
2. **Risk:** Hasty consolidation could lose unique test cases
3. **Effort:** 3-5 hours of focused work needed
4. **Value:** Current state is functional and well-organized
5. **Pragmatism:** Incremental consolidation during feature work is more efficient

**Why marked as legacy?**

1. **Clear Intent:** `*_legacy.py` suffix indicates temporary status
2. **Primary Files:** Clear which file to update for new tests
3. **Discoverability:** pytest finds both, no tests lost
4. **Safety:** Easy to find and consolidate later

---

## Conclusion

The legacy files represent a **temporary state** that is acceptable and functional. They:
- ✅ Are properly organized in correct categories
- ✅ Contain valid, runnable tests
- ✅ Are clearly marked for future consolidation
- ✅ Don't interfere with new test development
- ✅ Can be consolidated incrementally

**No immediate action required.** Consolidate opportunistically during feature work.

---

*"Wisdom teaches us that perfection is the enemy of progress. The archives are organized, the knowledge preserved. The final cataloguing refinements can proceed at a measured pace."*

— Legacy Files Guide
— Assistant Professor of Occult Studies
