---
name: Structlog Anti-Pattern Remediation
overview: Fix all identified structlog anti-patterns and violations found in the codebase, including direct logging module usage, f-string logging, deprecated context parameters, and ensure compliance with structlog.mdc best practices.
todos:
  - id: fix-test-fixture-logging
    content: "Fix server/tests/fixtures/integration/__init__.py: Replace import logging and f-string logging with enhanced structured logging"
    status: completed
  - id: verify-no-other-violations
    content: Run comprehensive search to verify no other violations exist (excluding infrastructure and docs)
    status: completed
  - id: fix-error-logging-api-signatures
    content: Update error_logging.py function signatures - remove context parameter, add **kwargs
    status: pending
  - id: find-all-error-logging-usages
    content: Find all usages of error_logging.py functions across server and client codebases
    status: pending
  - id: update-error-logging-callers-server
    content: Update all server callers to use new error_logging.py API (remove context=, use **kwargs)
    status: pending
  - id: update-error-logging-callers-client
    content: Update client codebase error logging patterns (if any exist)
    status: pending
  - id: update-error-logging-tests
    content: Update test files that test or mock error_logging.py functions
    status: pending
  - id: consolidate-error-logging-modules
    content: Consolidate error_logging.py and enhanced_error_logging.py (optional but recommended)
    status: pending
  - id: update-pre-commit-validation
    content: Ensure pre-commit validation scripts catch all anti-patterns
    status: completed
  - id: update-api-character-creation
    content: Update server/api/character_creation.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-players
    content: Update server/api/players.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-professions
    content: Update server/api/professions.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-real-time
    content: Update server/api/real_time.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-admin-npc
    content: Update server/api/admin/npc.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-maps
    content: Update server/api/maps.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-rooms
    content: Update server/api/rooms.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-player-effects
    content: Update server/api/player_effects.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-player-respawn
    content: Update server/api/player_respawn.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-metrics
    content: Update server/api/metrics.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-monitoring
    content: Update server/api/monitoring.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-system-monitoring
    content: Update server/api/system_monitoring.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-container-helpers
    content: Update server/api/container_helpers.py - remove context parameter, use **kwargs
    status: pending
  - id: update-api-container-exception-handlers
    content: Update server/api/container_exception_handlers.py - remove context parameter, use **kwargs
    status: pending
  - id: update-auth-endpoints
    content: Update server/auth/endpoints.py - remove context parameter, use **kwargs
    status: pending
  - id: update-auth-invites
    content: Update server/auth/invites.py - remove context parameter, use **kwargs
    status: pending
  - id: update-game-player-service
    content: Update server/game/player_service.py - remove context parameter, use **kwargs
    status: pending
  - id: update-game-player-creation-service
    content: Update server/game/player_creation_service.py - remove context parameter, use **kwargs
    status: pending
  - id: update-game-player-respawn-wrapper
    content: Update server/game/player_respawn_wrapper.py - remove context parameter, use **kwargs
    status: pending
  - id: update-game-player-state-service
    content: Update server/game/player_state_service.py - remove context parameter, use **kwargs
    status: pending
  - id: update-game-mechanics
    content: Update server/game/mechanics.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-player-effect-repository
    content: Update server/persistence/repositories/player_effect_repository.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-health-repository
    content: Update server/persistence/repositories/health_repository.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-experience-repository
    content: Update server/persistence/repositories/experience_repository.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-spell-repository
    content: Update server/persistence/repositories/spell_repository.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-profession-repository
    content: Update server/persistence/repositories/profession_repository.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-player-spell-repository
    content: Update server/persistence/repositories/player_spell_repository.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-async-persistence
    content: Update server/async_persistence.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-container-persistence-async
    content: Update server/persistence/container_persistence_async.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-item-instance-persistence-async
    content: Update server/persistence/item_instance_persistence_async.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-container-query-helpers-async
    content: Update server/persistence/container_query_helpers_async.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-container-query-helpers
    content: Update server/persistence/container_query_helpers.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-item-instance-persistence
    content: Update server/persistence/item_instance_persistence.py - remove context parameter, use **kwargs
    status: pending
  - id: update-persistence-container-helpers
    content: Update server/persistence/container_helpers.py - remove context parameter, use **kwargs
    status: pending
  - id: update-services-container-service
    content: Update server/services/container_service.py - remove context parameter, use **kwargs
    status: pending
  - id: update-utils-command-parser
    content: Update server/utils/command_parser.py - remove context parameter, use **kwargs (note: uses log_and_raise_enhanced)
    status: pending
  - id: update-utils-command-factories-exploration
    content: Update server/utils/command_factories_exploration.py - remove context parameter, use **kwargs (note: uses log_and_raise_enhanced)
    status: pending
  - id: update-utils-command-factories-utility
    content: Update server/utils/command_factories_utility.py - remove context parameter, use **kwargs
    status: pending
  - id: update-utils-command-factories-inventory
    content: Update server/utils/command_factories_inventory.py - remove context parameter, use **kwargs
    status: pending
  - id: update-utils-command-factories-communication
    content: Update server/utils/command_factories_communication.py - remove context parameter, use **kwargs
    status: pending
  - id: update-utils-command-factories-player-state
    content: Update server/utils/command_factories_player_state.py - remove context parameter, use **kwargs
    status: pending
  - id: update-utils-command-factories-moderation
    content: Update server/utils/command_factories_moderation.py - remove context parameter, use **kwargs
    status: pending
  - id: update-utils-command-processor
    content: Update server/utils/command_processor.py - remove context parameter, use **kwargs
    status: pending
  - id: update-utils-command-helpers
    content: Update server/utils/command_helpers.py - remove context parameter, use **kwargs
    status: pending
  - id: update-utils-motd-loader
    content: Update server/utils/motd_loader.py - remove context parameter, use **kwargs
    status: pending
  - id: update-database-helpers
    content: Update server/database_helpers.py - remove context parameter, use **kwargs
    status: pending
  - id: update-database
    content: Update server/database.py - remove context parameter, use **kwargs
    status: pending
  - id: update-database-config-helpers
    content: Update server/database_config_helpers.py - remove context parameter, use **kwargs
    status: pending
  - id: update-auth-utils
    content: Update server/auth_utils.py - remove context parameter, use **kwargs
    status: pending
  - id: update-auth-argon2-utils
    content: Update server/auth/argon2_utils.py - remove context parameter, use **kwargs
    status: pending
  - id: update-npc-database
    content: Update server/npc_database.py - remove context parameter, use **kwargs
    status: pending
  - id: update-world-loader
    content: Update server/world_loader.py - remove context parameter, use **kwargs
    status: pending
  - id: update-monitoring-exception-tracker
    content: Update server/monitoring/exception_tracker.py - remove context parameter, use **kwargs
    status: pending
  - id: update-exceptions
    content: Update server/exceptions.py - remove context parameter, use **kwargs (if used internally)
    status: pending
  - id: update-error-handlers-pydantic-error-handler
    content: Update server/error_handlers/pydantic_error_handler.py - remove context parameter, use **kwargs
    status: pending
  - id: update-test-error-logging
    content: Update server/tests/unit/utils/test_error_logging.py - update test mocks and assertions for new API
    status: pending
  - id: update-test-enhanced-error-logging
    content: Update server/tests/unit/utils/test_enhanced_error_logging.py - verify tests work with new API
    status: pending
  - id: update-test-legacy-error-handlers
    content: Update server/tests/unit/test_legacy_error_handlers.py - update test mocks and assertions
    status: pending
  - id: update-test-exceptions-comprehensive
    content: Update server/tests/unit/test_exceptions_comprehensive.py - update test mocks and assertions
    status: pending
  - id: update-test-exceptions
    content: Update server/tests/unit/test_exceptions.py - update test mocks and assertions
    status: pending
  - id: update-test-containers
    content: Update server/tests/unit/api/test_containers.py - update test mocks and assertions
    status: pending
  - id: update-test-container-helpers
    content: Update server/tests/unit/api/test_container_helpers.py - update test mocks and assertions
    status: pending
isProject: false
---

# Structlog Anti-Pattern Remediation Plan

## Analysis Summary

After analyzing the codebase against `.cursor/rules/structlog.mdc` and the project's internal `LOGGING_BEST_PRACTICES.md`, the following violations were identified:

### Critical Violations Found

1. **Direct `logging` Module Usage** (1 file)

  - `server/tests/fixtures/integration/__init__.py`: Uses `import logging` and `logging.getLogger(__name__).debug(f"...")` - violates the requirement to use enhanced logging

2. **F-String Logging** (1 file)

  - `server/tests/fixtures/integration/__init__.py`: Uses f-string in log message: `logging.getLogger(__name__).debug(f"Database cleanup warning: {e}")`

3. **Deprecated `context` Parameter API** (1 file)

  - `server/utils/error_logging.py`: Public API functions accept `context: ErrorContext | None = None` parameter, which is explicitly deprecated per `LOGGING_BEST_PRACTICES.md`. While the internal implementation correctly converts to `**kwargs`, the public API still exposes the deprecated pattern.

### Acceptable Usage (Not Violations)

- `server/structured_logging/enhanced_logging_config.py`: Uses `import logging` and `structlog.get_logger()` directly - **ACCEPTABLE** per module docstring (lines 65-68) as it's logging infrastructure code that must avoid circular imports during initialization
- `server/structured_logging/logging_file_setup.py`: Uses `logging.getLogger()` - **ACCEPTABLE** as it's part of the logging infrastructure integrating with standard library logging
- Documentation files showing f-string examples: These are **INTENTIONAL** examples of anti-patterns to avoid, not actual violations

## Remediation Tasks

### Task 1: Fix Test Fixture Logging Violations

**File**: `server/tests/fixtures/integration/__init__.py`

**Current Violation** (lines 153-155):

```python
import logging
logging.getLogger(__name__).debug(f"Database cleanup warning: {e}")
```

**Fix Required**:

1. Replace `import logging` with `from server.structured_logging.enhanced_logging_config import get_logger`
2. Replace f-string logging with structured logging
3. Use appropriate log level (warning, not debug, for cleanup exceptions)

**Expected Result**:

```python
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# In exception handler:
logger.warning("Database cleanup warning", error=str(e), error_type=type(e).__name__)
```

### Task 2: Fix Error Logging API - Remove Deprecated Context Parameter

**File**: `server/utils/error_logging.py`

**Issue**: Public API functions (`log_and_raise`, `log_and_raise_http`, `log_error_with_context`, etc.) accept `context: ErrorContext | None = None` parameter, which is deprecated per project standards. The internal implementation correctly converts to `**kwargs`, but the public API still exposes the deprecated pattern.

**Approach**: Direct fix - no backward compatibility. Update `error_logging.py` to match the correct pattern from `enhanced_error_logging.py` and update all callers across server and client codebases.

**Steps**:

1. **Update `error_logging.py` function signatures**:

  - Remove `context: ErrorContext | None = None` parameter from public API
  - Add `**kwargs: Any` parameter for structured logging data
  - Internally, create `ErrorContext` from `**kwargs` if needed for exception objects
  - Use `log_with_context` from `enhanced_logging_config` for structured logging (like `enhanced_error_logging.py` does)

2. **Find all usages** across server and client codebases:

  - Search for `log_and_raise(`, `log_and_raise_http(`, `log_error_with_context(`, `create_logged_http_exception(`, `wrap_third_party_exception(`
  - Identify all files that pass `context=context` parameter

3. **Update all callers**:

  - Remove `context=context` parameter from function calls
  - Convert `context.metadata` and other context data to `**kwargs` format
  - Example transformation:
    ```python
    # OLD:
    context = create_error_context()
    context.metadata["operation"] = "move_player"
    log_and_raise(ValidationError, "Error", context=context)

    # NEW:
    log_and_raise(ValidationError, "Error", operation="move_player")
    ```

4. **Consolidate modules** (optional but recommended):

  - Consider merging `error_logging.py` and `enhanced_error_logging.py` if they're duplicates
  - Or update `error_logging.py` to match `enhanced_error_logging.py` pattern exactly
  - Update all imports to use the consolidated module

5. **Update exception creation**:

  - Ensure `ErrorContext` objects are still created internally for exception objects (exceptions need ErrorContext)
  - But logging should use `**kwargs` directly via `log_with_context`

**Files to Update** (based on grep results):

- Server files: ~40+ files using `log_and_raise`, `log_and_raise_http`, etc.
- Client files: Check for any TypeScript/JavaScript error logging patterns
- Test files: Update test mocks and assertions

**Note**: `enhanced_error_logging.py` already implements the correct pattern. We can either:

- Option A: Update `error_logging.py` to match `enhanced_error_logging.py` exactly, then migrate all imports
- Option B: Keep both but make `error_logging.py` match the enhanced pattern

**Recommended**: Option A - Update `error_logging.py` to match enhanced pattern, then update all imports.

### Task 3: Verify No Other Violations

**Action**: Run comprehensive search to ensure no other violations exist:

1. Search for remaining `import logging` statements (excluding logging infrastructure files)
2. Search for remaining `logging.getLogger` calls (excluding logging infrastructure files)
3. Search for f-string logging patterns: `logger.(info|debug|warning|error|critical)\(f"`
4. Verify no `context={"key": "value"}` patterns in logger calls

**Files to Exclude from Violation Checks**:

- `server/structured_logging/*` (logging infrastructure)
- Documentation files (`docs/**`, `*.md`)
- Example files (`docs/examples/**`)

### Task 4: Update Pre-Commit Validation

**File**: `scripts/verify_enhanced_logging_compliance.py` (if exists)

**Action**: Ensure the validation script catches all identified anti-patterns:

- Direct `logging` module imports
- F-string logging patterns
- Deprecated `context` parameter usage

## Implementation Order

1. **Task 1** (Fix test fixture) - Quick fix, low risk
2. **Task 3** (Verify no other violations) - Comprehensive check before major changes
3. **Task 2** (Migrate error logging API) - Requires codebase-wide changes, do after verification
4. **Task 4** (Update validation) - Ensure future violations are caught

## Testing Requirements

After each task:

1. Run test suite to ensure no regressions
2. Verify logging output is structured correctly
3. Check that enhanced logging features (MDC, correlation IDs, sanitization) still work

## Success Criteria

- All direct `logging` module usage removed (except infrastructure files)
- All f-string logging converted to structured logging
- Deprecated `context` parameter removed from public APIs - replaced with `**kwargs` pattern
- All tests pass
- Logging output verified to be structured and machine-readable
- Pre-commit validation updated to catch violations

## Notes

- The logging infrastructure files (`server/structured_logging/*`) correctly use `logging` module for integration with Python's standard library logging system - these are NOT violations
- Documentation files showing anti-patterns are intentional examples and should NOT be changed
- The `enhanced_error_logging.py` module already implements the correct pattern with `**kwargs` support
- Task 2 will update `error_logging.py` to match this pattern and update all callers across server and client codebases
