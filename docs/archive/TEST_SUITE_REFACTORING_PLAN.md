# Test Suite Refactoring Plan

> *"The old ways of organizing our research have proven... inadequate. We must bring structure to chaos, lest we lose ourselves in the labyrinth of our own making."* - From the Notes of Dr. Armitage on Academic Organization, 1929

## Executive Summary

The current test suite contains **204 test files** with **519+ test functions/classes** in a relatively flat structure. While functional, the organization makes it difficult to:
- Locate related tests quickly
- Understand test coverage scope
- Maintain consistency across test types
- Onboard new developers to the testing patterns

This plan proposes a hierarchical, feature-based reorganization following pytest/unittest best practices and the existing codebase patterns.

## Current State Analysis

### Test Distribution by Category

Based on analysis of test file patterns:

- **API/Endpoints**: ~15 files (api_*, health_*, monitoring_*)
- **Commands**: ~20 files (command_*, admin_*, utility_*)
- **Chat/Communication**: ~25 files (chat_*, whisper_*, local_channel_*, global_channel_*, emote_*)
- **Player Management**: ~15 files (player_*, character_*, auth_*)
- **NPC System**: ~18 files (npc_*)
- **Room/World**: ~10 files (room_*, world_*, movement_*)
- **Events/Real-time**: ~15 files (event_*, websocket_*, sse_*, nats_*)
- **Infrastructure**: ~20 files (config_*, database_*, persistence_*, security_*)
- **Integration/E2E**: ~15 files (*_integration, *_e2e, multiplayer_*)
- **Coverage/Performance**: ~10 files (*_coverage, *_performance, *_benchmarks)
- **Bug Fixes/Debugging**: ~8 files (*_fix, *_bug, *_debug)
- **Utilities/Helpers**: ~10 files (utils_*, mock_*, conftest, etc.)
- **Other**: ~23 files (aliases, stats, models, etc.)

### Test Type Distribution

- **Unit Tests**: ~40% (isolated component tests)
- **Integration Tests**: ~30% (component interaction tests)
- **Coverage Tests**: ~10% (focused coverage improvement)
- **Security Tests**: ~5% (security validation)
- **Performance Tests**: ~3% (benchmark and performance)
- **E2E Tests**: ~5% (full workflow tests)
- **Bug Fix Tests**: ~4% (regression prevention)
- **Other**: ~3% (verification, demo, etc.)

### Current Issues

1. **Naming Inconsistency**
   - Multiple files for same feature (e.g., `test_admin_teleport_commands.py`, `test_admin_teleport_integration.py`, `test_admin_teleport_security.py`)
   - Unclear suffixes (*_fix, *_bug, *_simple, *_comprehensive, *_demo)
   - Mixed naming patterns

2. **Flat Structure**
   - All 204 files in single directory
   - No logical grouping
   - Difficult navigation

3. **Test Type Ambiguity**
   - Coverage tests mixed with unit tests
   - Integration tests not clearly separated
   - Bug fix tests scattered

4. **Duplication Risk**
   - Similar tests across multiple files
   - Unclear which test file to update
   - Potential for inconsistent assertions

## Proposed Structure

### Directory Hierarchy

```
server/tests/
├── README.md                          # Updated test suite documentation
├── conftest.py                        # Global fixtures and configuration
├── pytest.ini                         # Pytest configuration (if needed)
│
├── fixtures/                          # Shared test fixtures and utilities
│   ├── __init__.py
│   ├── player_fixtures.py            # Player-related fixtures
│   ├── room_fixtures.py              # Room/world fixtures
│   ├── npc_fixtures.py               # NPC fixtures
│   ├── connection_fixtures.py        # Connection/network fixtures
│   ├── mock_data.py                  # Mock data generators (existing)
│   └── test_environment.py           # Test environment utilities (from utils/)
│
├── unit/                              # Unit tests (isolated component tests)
│   ├── __init__.py
│   ├── api/                          # API layer tests
│   │   ├── __init__.py
│   │   ├── test_base.py
│   │   ├── test_players.py
│   │   ├── test_professions.py
│   │   ├── test_health_endpoints.py
│   │   ├── test_monitoring_endpoints.py
│   │   └── test_real_time.py
│   │
│   ├── commands/                     # Command handler tests
│   │   ├── __init__.py
│   │   ├── test_command_handler.py
│   │   ├── test_command_validation.py
│   │   ├── test_admin_commands.py
│   │   ├── test_utility_commands.py
│   │   ├── test_movement_commands.py
│   │   └── test_command_rate_limiter.py
│   │
│   ├── chat/                         # Chat/communication tests
│   │   ├── __init__.py
│   │   ├── test_chat_service.py
│   │   ├── test_chat_logger.py
│   │   ├── test_emote_service.py
│   │   ├── test_whisper_channel.py
│   │   ├── test_local_channel.py
│   │   ├── test_global_channel.py
│   │   └── test_system_channel.py
│   │
│   ├── player/                       # Player management tests
│   │   ├── __init__.py
│   │   ├── test_player_service.py
│   │   ├── test_player_models.py
│   │   ├── test_player_stats.py
│   │   ├── test_character_creation.py
│   │   ├── test_character_recovery.py
│   │   ├── test_player_preferences.py
│   │   └── test_player_guid_formatter.py
│   │
│   ├── npc/                          # NPC system tests
│   │   ├── __init__.py
│   │   ├── test_npc_models.py
│   │   ├── test_npc_behaviors.py
│   │   ├── test_npc_spawning_service.py
│   │   ├── test_npc_lifecycle_manager.py
│   │   ├── test_npc_population_control.py
│   │   ├── test_npc_name_formatting.py
│   │   └── test_npc_admin_api.py
│   │
│   ├── world/                        # Room/world tests
│   │   ├── __init__.py
│   │   ├── test_room_models.py
│   │   ├── test_room_service.py
│   │   ├── test_room_utils.py
│   │   ├── test_world_loader.py
│   │   ├── test_world_hierarchy.py
│   │   └── test_movement_service.py
│   │
│   ├── events/                       # Event system tests
│   │   ├── __init__.py
│   │   ├── test_event_bus.py
│   │   ├── test_event_publisher.py
│   │   ├── test_event_handler.py
│   │   └── test_message_handler_factory.py
│   │
│   ├── auth/                         # Authentication/authorization tests
│   │   ├── __init__.py
│   │   ├── test_auth.py
│   │   ├── test_auth_utils.py
│   │   ├── test_jwt_authentication.py
│   │   ├── test_argon2_utils.py
│   │   └── test_email_utils.py
│   │
│   ├── infrastructure/               # Core infrastructure tests
│   │   ├── __init__.py
│   │   ├── test_config.py
│   │   ├── test_database.py
│   │   ├── test_persistence.py
│   │   ├── test_app_factory.py
│   │   ├── test_lifespan.py
│   │   └── test_main.py
│   │
│   ├── middleware/                   # Middleware tests
│   │   ├── __init__.py
│   │   ├── test_error_handling_middleware.py
│   │   ├── test_logging_middleware.py
│   │   ├── test_security_middleware.py
│   │   └── test_cors_configuration.py
│   │
│   ├── models/                       # Model tests
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   ├── test_model_relationships.py
│   │   ├── test_model_configuration.py
│   │   ├── test_profession_models.py
│   │   ├── test_health_models.py
│   │   └── test_alias_models.py
│   │
│   ├── services/                     # Service layer tests
│   │   ├── __init__.py
│   │   ├── test_health_service.py
│   │   ├── test_game_tick_service.py
│   │   ├── test_memory_cleanup_service.py
│   │   ├── test_metrics_collector.py
│   │   └── test_dependency_injection.py
│   │
│   ├── realtime/                     # Real-time communication tests
│   │   ├── __init__.py
│   │   ├── test_websocket_handler.py
│   │   ├── test_websocket_message_handler.py
│   │   ├── test_sse_handler.py
│   │   ├── test_sse_auth.py
│   │   ├── test_nats_service.py
│   │   ├── test_nats_message_handler.py
│   │   └── test_nats_retry_handler.py
│   │
│   ├── logging/                      # Logging tests
│   │   ├── __init__.py
│   │   ├── test_audit_logger.py
│   │   ├── test_chat_logger.py
│   │   ├── test_admin_actions_logger.py
│   │   └── test_log_analysis_tools.py
│   │
│   └── utilities/                    # Utility tests
│       ├── __init__.py
│       ├── test_security_utils.py
│       ├── test_security_validator.py
│       ├── test_rate_limiter.py
│       ├── test_circuit_breaker.py
│       ├── test_alias_graph.py
│       ├── test_alias_storage.py
│       ├── test_stats_generator.py
│       ├── test_validation_functions.py
│       └── test_error_handlers.py
│
├── integration/                       # Integration tests
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── test_api_players_integration.py
│   │   ├── test_dual_connection_integration.py
│   │   └── test_monitoring_integration.py
│   │
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── test_admin_teleport_integration.py
│   │   ├── test_command_handler_integration.py
│   │   └── test_whisper_command_integration.py
│   │
│   ├── chat/
│   │   ├── __init__.py
│   │   ├── test_local_channel_integration.py
│   │   ├── test_global_channel_integration.py
│   │   ├── test_whisper_integration.py
│   │   └── test_mute_workflow_integration.py
│   │
│   ├── events/
│   │   ├── __init__.py
│   │   ├── test_event_flow_integration.py
│   │   ├── test_event_broadcasting.py
│   │   ├── test_realtime_event_handler_integration.py
│   │   └── test_websocket_connection_events.py
│   │
│   ├── npc/
│   │   ├── __init__.py
│   │   ├── test_npc_integration.py
│   │   ├── test_npc_room_integration.py
│   │   └── test_npc_admin_commands_integration.py
│   │
│   ├── movement/
│   │   ├── __init__.py
│   │   ├── test_movement_integration.py
│   │   └── test_room_synchronization.py
│   │
│   ├── nats/
│   │   ├── __init__.py
│   │   ├── test_nats_integration_e2e.py
│   │   ├── test_connection_manager_nats.py
│   │   └── test_local_channel_nats.py
│   │
│   └── comprehensive/
│       ├── __init__.py
│       ├── test_comprehensive_integration.py
│       ├── test_simple_integration.py
│       └── test_connection_manager_comprehensive.py
│
├── e2e/                               # End-to-end tests
│   ├── __init__.py
│   ├── test_multiplayer_integration.py
│   ├── test_multiplayer_connection_messaging.py
│   ├── test_logout_integration.py
│   └── test_dual_connection_testing_strategy.py
│
├── performance/                       # Performance and benchmark tests
│   ├── __init__.py
│   ├── test_dual_connection_performance.py
│   ├── test_error_logging_performance.py
│   ├── test_mute_filtering_performance.py
│   └── test_model_performance_benchmarks.py
│
├── security/                          # Security-focused tests
│   ├── __init__.py
│   ├── test_admin_teleport_security.py
│   ├── test_security_penetration.py
│   ├── test_security_headers_verification.py
│   ├── test_centralized_security_validation.py
│   ├── test_global_channel_access_control.py
│   └── test_file_containment.py
│
├── coverage/                          # Coverage improvement tests
│   ├── __init__.py
│   ├── test_command_handler_coverage.py
│   ├── test_command_rate_limiter_coverage.py
│   ├── test_comprehensive_logging_coverage.py
│   ├── test_system_commands_coverage.py
│   ├── test_help_content_coverage.py
│   └── test_simple_coverage_gaps.py
│
├── regression/                        # Bug fix and regression tests
│   ├── __init__.py
│   ├── test_unknown_room_fix.py
│   ├── test_movement_fix.py
│   ├── test_self_message_bug.py
│   ├── test_self_message_exclusion.py
│   ├── test_npc_spawn_fix.py
│   ├── test_event_broadcasting_bugs.py
│   └── test_unresolved_bugs.py
│
├── monitoring/                        # Monitoring and observability tests
│   ├── __init__.py
│   ├── test_mute_filtering_monitoring.py
│   ├── test_movement_monitor.py
│   ├── test_monitoring_api.py
│   ├── test_monitoring_dual_connections.py
│   └── test_occupant_count_integration.py
│
├── verification/                      # Verification and validation tests
│   ├── __init__.py
│   ├── test_async_operations_verification.py
│   ├── test_async_pattern_standardization.py
│   ├── test_pure_async_eventbus_verification.py
│   ├── test_help_topic_validation.py
│   ├── test_validation_error_imports.py
│   └── test_mute_data_consistency.py
│
└── scripts/                           # Test database and setup scripts
    ├── __init__.py
    ├── init_databases.py             # Existing
    ├── init_databases.ps1            # Existing
    ├── verify_databases.ps1          # Existing
    ├── init_test_db.py               # Move from root
    ├── init_npc_test_db.py           # Move from root
    └── verify_test_db.py             # Move from root
```

## Migration Strategy

### Phase 1: Preparation (Week 1)

1. **Create New Directory Structure**
   - Create all directories with `__init__.py` files
   - Set up shared fixtures in `fixtures/` directory
   - Update `conftest.py` with new paths

2. **Document Migration**
   - Create migration tracking document
   - Map each existing test to new location
   - Identify tests that need consolidation

3. **Set Up CI/CD Compatibility**
   - Ensure pytest can discover tests in new structure
   - Update test running scripts
   - Verify coverage reporting works

### Phase 2: Core Infrastructure (Week 2)

**Move tests in order of dependency (least to most dependent):**

1. **Fixtures and Utilities**
   ```
   server/tests/mock_data.py           → fixtures/mock_data.py
   server/tests/utils/*                → fixtures/
   ```

2. **Unit Tests - Infrastructure**
   ```
   test_config.py                      → unit/infrastructure/
   test_database.py                    → unit/infrastructure/
   test_models*.py                     → unit/models/
   test_exceptions.py                  → unit/infrastructure/
   ```

3. **Unit Tests - Models and Basic Services**
   ```
   test_*_models.py                    → unit/models/
   test_*_service.py                   → unit/services/ or domain-specific
   ```

### Phase 3: Feature Domains (Week 3)

**Group related tests by domain:**

1. **Player Domain**
   ```
   test_player*.py                     → unit/player/
   test_character*.py                  → unit/player/
   test_auth*.py                       → unit/auth/
   ```

2. **NPC Domain**
   ```
   test_npc*.py                        → unit/npc/ or integration/npc/
   ```

3. **World/Room Domain**
   ```
   test_room*.py                       → unit/world/
   test_world*.py                      → unit/world/
   test_movement*.py                   → unit/world/ or integration/movement/
   ```

4. **Communication Domain**
   ```
   test_chat*.py                       → unit/chat/
   test_whisper*.py                    → unit/chat/
   test_*_channel*.py                  → unit/chat/
   test_emote*.py                      → unit/chat/
   ```

### Phase 4: Integration and Specialized Tests (Week 4)

1. **Integration Tests**
   ```
   test_*_integration.py               → integration/<domain>/
   ```

2. **E2E Tests**
   ```
   test_*_e2e*.py                      → e2e/
   test_multiplayer*.py                → e2e/
   ```

3. **Security Tests**
   ```
   test_*_security.py                  → security/
   test_*_penetration.py               → security/
   ```

4. **Performance Tests**
   ```
   test_*_performance.py               → performance/
   test_*_benchmarks.py                → performance/
   ```

### Phase 5: Coverage and Bug Fixes (Week 5)

1. **Coverage Tests**
   ```
   test_*_coverage.py                  → coverage/
   ```

2. **Regression Tests**
   ```
   test_*_fix.py                       → regression/
   test_*_bug.py                       → regression/
   ```

3. **Consolidation**
   - Merge duplicate tests
   - Remove obsolete tests
   - Update test names for clarity

### Phase 6: Validation and Cleanup (Week 6)

1. **Validation**
   - Run full test suite
   - Verify coverage metrics maintained/improved
   - Check CI/CD pipeline
   - Performance benchmark comparison

2. **Documentation**
   - Update README.md with new structure
   - Document test organization principles
   - Create contributor guide for test writing
   - Update development documentation

3. **Cleanup**
   - Remove old test files
   - Archive obsolete tests
   - Clean up conftest.py

## Test Organization Principles

### Naming Conventions

**File Names:**
- Unit tests: `test_<component>.py`
- Integration tests: `test_<feature>_integration.py`
- E2E tests: `test_<workflow>_e2e.py`
- Security tests: `test_<feature>_security.py`
- Performance tests: `test_<feature>_performance.py`
- Coverage tests: `test_<feature>_coverage.py`
- Regression tests: `test_<issue_or_bug>_fix.py`

**Class Names:**
- `TestClassName` (PascalCase)
- Descriptive of what's being tested
- Example: `TestAdminTeleportCommands`, `TestPlayerAuthentication`

**Test Method Names:**
- `test_<what>_<condition>_<expected_result>`
- Examples:
  - `test_login_with_valid_credentials_succeeds`
  - `test_teleport_without_admin_permission_fails`
  - `test_npc_spawn_in_invalid_room_raises_error`

### Test Structure

**Follow AAA Pattern:**
```python
def test_example():
    # Arrange - Set up test data and conditions
    player = create_test_player(admin=True)
    target_room = "arkham_001"

    # Act - Execute the code being tested
    result = teleport_player(player, target_room)

    # Assert - Verify the expected outcome
    assert result.success
    assert player.current_room_id == target_room
```

**Use Fixtures for Common Setup:**
```python
@pytest.fixture
def admin_player():
    """Fixture providing an admin player for testing."""
    return create_test_player(admin=True, room="test_room_001")

def test_admin_command(admin_player):
    # Test uses the fixture
    result = execute_admin_command(admin_player, "teleport")
    assert result.allowed
```

### When to Create New Test Files

**Create new file when:**
- Testing a distinct component or module
- Test file exceeds 500 lines
- Tests serve different purposes (unit vs integration)
- Tests belong to different domains

**Combine in same file when:**
- Testing closely related functionality
- Tests share significant setup/fixtures
- Natural grouping by feature
- File stays under 500 lines

### Coverage Strategy

**Coverage Goals:**
- Critical paths: 95%+ coverage
- Core business logic: 90%+ coverage
- API endpoints: 85%+ coverage
- Utilities: 80%+ coverage
- Overall project: 85%+ coverage

**Focus Areas:**
1. Happy paths (normal operation)
2. Error conditions (expected failures)
3. Edge cases (boundary conditions)
4. Security validation
5. Performance critical paths

## Migration File Mapping

### Detailed Mapping (Sample)

```
# Infrastructure
test_config.py                          → unit/infrastructure/test_config.py
test_database.py                        → unit/infrastructure/test_database.py
test_app_factory.py                     → unit/infrastructure/test_app_factory.py
test_app_lifespan.py                    → unit/infrastructure/test_lifespan.py
test_main.py                            → unit/infrastructure/test_main.py

# API Layer
test_api_base.py                        → unit/api/test_base.py
test_api_players.py                     → unit/api/test_players.py
test_api_players_integration.py         → integration/api/test_api_players_integration.py
test_api_professions.py                 → unit/api/test_professions.py
test_health_endpoint.py                 → unit/api/test_health_endpoints.py
test_health_models.py                   → unit/models/test_health_models.py
test_health_service.py                  → unit/services/test_health_service.py

# Commands
test_command_handler.py                 → unit/commands/test_command_handler.py
test_command_handler_v2.py              → unit/commands/test_command_handler.py (merge)
test_command_handler_unified.py         → unit/commands/test_command_handler.py (merge)
test_command_handler_coverage.py        → coverage/test_command_handler_coverage.py
test_command_validation.py              → unit/commands/test_command_validation.py
test_admin_teleport_commands.py         → unit/commands/test_admin_commands.py
test_admin_teleport_integration.py      → integration/commands/test_admin_teleport_integration.py
test_admin_teleport_security.py         → security/test_admin_teleport_security.py

# Chat/Communication
test_chat_service.py                    → unit/chat/test_chat_service.py
test_chat_logger.py                     → unit/logging/test_chat_logger.py
test_whisper_channel.py                 → unit/chat/test_whisper_channel.py
test_whisper_command_integration.py     → integration/chat/test_whisper_integration.py
test_local_channel.py                   → unit/chat/test_local_channel.py
test_local_channel_commands.py          → unit/chat/test_local_channel.py (merge)
test_local_channel_logging.py           → unit/logging/test_local_channel_logging.py
test_local_channel_nats_integration.py  → integration/nats/test_local_channel_nats.py

# ... (continue for all 204 files)
```

## Testing Standards and Best Practices

### 1. Test Independence

- Each test must be runnable in isolation
- No dependencies between test execution order
- Clean up resources in teardown/fixtures
- Use fixtures for shared setup

### 2. Mock Usage

- Mock external dependencies (databases, APIs, file system)
- Use real objects for the system under test
- Prefer dependency injection over patching
- Mock at boundaries, not internals

### 3. Assertion Quality

- One logical assertion per test (can be multiple assert statements for same condition)
- Use specific assertions (assertEqual vs assertTrue)
- Provide meaningful failure messages
- Test both success and failure cases

### 4. Test Data Management

- Use factories/fixtures for test data
- Keep test data minimal and relevant
- Don't use production data
- Use randomization judiciously (ensure reproducibility)

### 5. Performance

- Unit tests should run in milliseconds
- Integration tests in seconds
- E2E tests in minutes
- Use markers to categorize slow tests
- Parallelize test execution when possible

## Tooling Updates

### pytest Configuration

Update `pytest.ini` or `pyproject.toml`:

```ini
[tool.pytest.ini_options]
testpaths = ["server/tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"

# Test discovery patterns
norecursedirs = [".git", ".tox", "dist", "build", "*.egg"]

# Markers for test categories
markers = [
    "unit: Unit tests",
    "integration: Integration tests",
    "e2e: End-to-end tests",
    "security: Security tests",
    "performance: Performance tests",
    "slow: Slow running tests",
    "regression: Bug fix regression tests"
]

# Coverage settings
addopts = [
    "-ra",
    "--strict-markers",
    "--cov=server",
    "--cov-branch",
    "--cov-report=term-missing:skip-covered",
    "--cov-report=html",
    "--cov-report=xml",
]

# Async support
asyncio_mode = "auto"
```

### Makefile Updates

```makefile
# Run different test categories
.PHONY: test-unit test-integration test-e2e test-security test-performance test-all

test-unit:
	pytest server/tests/unit -v

test-integration:
	pytest server/tests/integration -v

test-e2e:
	pytest server/tests/e2e -v

test-security:
	pytest server/tests/security -v

test-performance:
	pytest server/tests/performance -v

test-coverage:
	pytest server/tests/coverage -v

test-regression:
	pytest server/tests/regression -v

test-all:
	pytest server/tests -v

# Fast tests (unit only)
test-fast:
	pytest server/tests/unit -v -x

# Slow tests
test-slow:
	pytest server/tests -v -m slow
```

## Success Criteria

### Quantitative Metrics

- [ ] All 204 test files successfully migrated
- [ ] Test coverage maintained or improved (currently ~85%)
- [ ] All tests passing after migration
- [ ] CI/CD pipeline updated and passing
- [ ] Test execution time not significantly increased

### Qualitative Metrics

- [ ] Clear, logical test organization
- [ ] Easy to locate tests for any feature
- [ ] Consistent naming conventions
- [ ] Improved test discoverability
- [ ] Better separation of concerns
- [ ] Reduced duplication
- [ ] Clear documentation

### Documentation Deliverables

- [ ] Updated README.md in tests directory
- [ ] Test organization guide
- [ ] Contributor's testing guide
- [ ] Migration completion report
- [ ] Lessons learned document

## Risk Mitigation

### Risks and Mitigation Strategies

| Risk                        | Impact | Probability | Mitigation                                           |
| --------------------------- | ------ | ----------- | ---------------------------------------------------- |
| Breaking existing tests     | High   | Medium      | Incremental migration with validation at each step   |
| Lost test coverage          | High   | Low         | Coverage tracking before/after each phase            |
| CI/CD pipeline breaks       | High   | Medium      | Update CI in parallel, test in separate branch       |
| Developer confusion         | Medium | Medium      | Clear documentation, team communication              |
| Time overrun                | Medium | Medium      | Phased approach, clear milestones, regular check-ins |
| Duplicate/conflicting tests | Low    | High        | Careful review during consolidation phase            |

### Rollback Plan

1. Maintain git history for all changes
2. Tag before each major phase
3. Keep old structure until validation complete
4. Document rollback procedures
5. Have backup of test results for comparison

## Timeline and Milestones

### 6-Week Timeline

**Week 1: Preparation**
- Day 1-2: Create directory structure
- Day 3-4: Set up fixtures and utilities
- Day 5: Update CI/CD configuration

**Week 2: Core Infrastructure**
- Day 1-2: Migrate infrastructure tests
- Day 3-4: Migrate model tests
- Day 5: Validation and fixes

**Week 3: Feature Domains**
- Day 1: Player domain
- Day 2: NPC domain
- Day 3: World/Room domain
- Day 4: Communication domain
- Day 5: Validation and fixes

**Week 4: Integration and Specialized**
- Day 1-2: Integration tests
- Day 2-3: E2E, security, performance tests
- Day 5: Validation and fixes

**Week 5: Coverage and Regression**
- Day 1-2: Coverage tests
- Day 3: Regression tests
- Day 4-5: Test consolidation and cleanup

**Week 6: Finalization**
- Day 1-2: Final validation
- Day 3-4: Documentation
- Day 5: Cleanup and handoff

## Appendix A: Full File Mapping

*(See separate detailed mapping document for complete 204-file mapping)*

## Appendix B: Test Categories Reference

### Unit Test Categories
- API Layer
- Commands
- Chat/Communication
- Player Management
- NPC System
- World/Rooms
- Events
- Authentication
- Infrastructure
- Middleware
- Models
- Services
- Real-time
- Logging
- Utilities

### Integration Test Categories
- API Integration
- Command Integration
- Chat Integration
- Event Integration
- NPC Integration
- Movement Integration
- NATS Integration
- Comprehensive Integration

### Other Test Categories
- E2E Tests
- Performance Tests
- Security Tests
- Coverage Tests
- Regression Tests
- Monitoring Tests
- Verification Tests

---

*"In organizing the forbidden knowledge of our test suite, we must be methodical, thorough, and patient. Only through careful cataloguing can we hope to maintain our lucidity... and our test coverage."*

— End of Refactoring Plan —
