# Merge Reconciliation Plan: Local Test Changes → Refactored Structure

## Overview

The upstream merge brought in the TEST_SUITE_REFACTORING, but local commits contain changes to test files in the old flat structure. These changes must be applied to the new hierarchical structure.

## Local Test File Changes Requiring Migration

### Modified Test Files (with new locations)

| Old Location (Local Changes)               | New Location (After Refactor)                          | Local Changes     |
| ------------------------------------------ | ------------------------------------------------------ | ----------------- |
| `test_api_players.py`                      | `unit/api/test_players.py`                             | 358 lines changed |
| `test_chat_service.py`                     | `unit/chat/test_chat_service.py`                       | 93 lines changed  |
| `test_emote_mute_filtering.py`             | DELETED (moved to `unit/chat/test_emote_filtering.py`) | 2 lines changed   |
| `test_emote_types_mute_filtering.py`       | `unit/chat/test_emote_filtering.py`                    | 10 lines changed  |
| `test_error_logging_integration.py`        | DELETED (consolidated)                                 | 96 lines changed  |
| `test_event_broadcasting_bugs.py`          | `integration/events/test_event_broadcasting.py`        | 3 lines changed   |
| `test_global_channel_commands.py`          | `unit/chat/test_global_channel.py`                     | 96 lines changed  |
| `test_local_channel.py`                    | `unit/chat/test_local_channel.py`                      | 4 lines changed   |
| `test_local_channel_commands.py`           | DELETED (consolidated)                                 | 96 lines changed  |
| `test_main.py`                             | `unit/infrastructure/test_main.py`                     | 90 lines changed  |
| `test_mute_filtering_monitoring.py`        | `monitoring/test_mute_filtering_monitoring.py`         | 40 lines changed  |
| `test_mute_filtering_performance.py`       | `performance/test_mute_filtering_performance.py`       | 40 lines changed  |
| `test_npc_models.py`                       | `unit/npc/test_npc_models.py`                          | 55 lines changed  |
| `test_player_service.py`                   | DELETED → `unit/player/test_player_service.py`         | 69 lines changed  |
| `test_room_service.py`                     | DELETED → `unit/world/test_room_service.py`            | 59 lines changed  |
| `test_sse_handler.py`                      | `unit/realtime/test_sse_handler.py`                    | 14 lines changed  |
| `test_system_channel.py`                   | `unit/chat/test_system_channel.py`                     | 2 lines changed   |
| `test_system_channel_integration.py`       | `integration/chat/test_system_channel_integration.py`  | Changed           |
| `test_task_registry.py`                    | `unit/infrastructure/test_task_registry.py`            | 8 lines changed   |
| `test_temporary_permanent_mutes.py`        | `monitoring/test_temporary_permanent_mutes.py`         | 64 lines changed  |
| `test_whisper_channel.py`                  | `unit/chat/test_whisper_channel.py`                    | 2 lines changed   |
| `test_async_pattern_standardization.py`    | `verification/test_async_pattern_standardization.py`   | 2 lines changed   |
| `test_debug_infinite_loop.py`              | `regression/test_infinite_loop_debug.py`               | 2 lines changed   |
| `test_mute_unmute_workflow_integration.py` | `integration/chat/test_mute_workflow_integration.py`   | Changed           |

### New Test Files Created Locally (need proper placement)

| File Created Locally                          | Recommended New Location                                      |
| --------------------------------------------- | ------------------------------------------------------------- |
| `test_api_players_integration.py`             | `integration/api/test_api_players_integration.py`             |
| `test_async_operations_verification.py`       | `verification/test_async_operations_verification.py`          |
| `test_async_route_handlers.py`                | `verification/test_async_route_handlers.py`                   |
| `test_character_creation_service_layer.py`    | `unit/player/test_character_creation.py`                      |
| `test_comprehensive_integration.py`           | `integration/comprehensive/test_comprehensive_integration.py` |
| `test_comprehensive_logging_middleware.py`    | `unit/middleware/test_logging_middleware.py`                  |
| `test_cors_configuration_verification.py`     | `unit/middleware/test_cors_configuration.py`                  |
| `test_dependency_functions.py`                | `unit/infrastructure/test_dependency_injection.py`            |
| `test_dependency_injection.py`                | `unit/services/test_dependency_injection.py`                  |
| `test_dependency_injection_functions.py`      | CONSOLIDATE with above                                        |
| `test_player_service_layer.py`                | `unit/player/test_player_service.py`                          |
| `test_room_service_layer.py`                  | `unit/world/test_room_service.py`                             |
| `test_security_headers_verification.py`       | `security/test_security_headers_verification.py`              |
| `test_security_middleware.py`                 | `unit/middleware/test_security_middleware.py`                 |
| `test_service_dependency_injection.py`        | CONSOLIDATE                                                   |
| `test_service_dependency_injection_simple.py` | CONSOLIDATE                                                   |

## Migration Strategy

### Phase 1: Extract Local Changes

For each modified file, extract the diff between origin/main and local changes:

```powershell
# Example for test_api_players.py
git diff origin/main...HEAD~1 -- server/tests/test_api_players.py > local_changes_api_players.patch
```

### Phase 2: Apply to New Locations

1. Identify the new location from the mapping above
2. Apply the local changes to that new location
3. Resolve any conflicts due to structural changes

### Phase 3: Handle New Files

1. Move new test files to appropriate new locations
2. Consolidate duplicate functionality
3. Update imports and references

### Phase 4: Validation

1. Run test suite: `make test-server`
2. Verify coverage maintained
3. Check for import errors
4. Validate all tests pass

## Recommended Approach

**Option 1: Manual Migration (Recommended)**
- Safer, more controlled
- Review each change before applying
- Better understanding of what changed

**Option 2: Automated Git Rerere**
- Faster but riskier
- May miss subtle conflicts
- Good for simple renames

**Option 3: Three-way Comparison**
- Compare: old local, old upstream, new upstream
- Most thorough but most complex
- Best for understanding full context

## Next Steps

1. **Decide on approach** - Which method would you prefer?
2. **Create working branch** - Should we create a branch for this reconciliation?
3. **Start migration** - Begin with highest-impact files
4. **Test frequently** - Run tests after each batch of changes

## Priority Order (Highest Impact First)

1. ✅ Infrastructure tests (conftest.py, test_main.py)
2. ✅ API tests (test_api_players.py)
3. ✅ Service layer tests (new files created locally)
4. ✅ Chat/Communication tests
5. ✅ NPC tests
6. ✅ Integration tests
7. ✅ Performance/Security tests

---

*"Like reconciling contradictory translations of the Pnakotic Manuscripts, we must carefully merge these parallel histories of our test suite..."*
