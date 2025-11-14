# Test Suite Optimization Roadmap

> *"As catalogued in the Pnakotic Manuscripts, the path to test enlightenment requires not random pruning, but systematic optimization guided by empirical measurement and scholarly reasoning."*

**Goal:** Optimize test suite from 4,965 tests / 30 minutes to ~4,255 tests / 25 minutes while maintaining or improving critical coverage.

---

## Optimization Strategy Overview

### Guiding Principles

1. **Value-First Removal:** Remove only tests with demonstrably low value
2. **Coverage Preservation:** Maintain ≥80% overall coverage, ≥95% critical code coverage
3. **Incremental Changes:** Remove in batches, verify after each batch
4. **Risk Mitigation:** Easy rollback for each change
5. **Quality Over Quantity:** Prefer fewer high-quality tests over many low-quality tests

### Success Metrics

- ✅ Reduce test count by 10-15% (~500-710 tests)
- ✅ Reduce execution time by 15-20% (~5-6 minutes)
- ✅ Maintain ≥80% code coverage
- ✅ Maintain 100% of critical code coverage
- ✅ Improve test maintainability
- ✅ Reduce false-positive test failures

---

## Phase 1: Quick Wins (Week 1)

**Effort:** 2-4 hours
**Impact:** -60 tests, -1 minute, LOW RISK

### Task 1.1: Remove Placeholder Tests (30 minutes)

**Action:** Remove all tests with `assert True` / `# Placeholder` assertions

**Command:**
```bash
# Find placeholder tests
grep -r "assert True  # Placeholder" server/tests
grep -r "pass  # Placeholder" server/tests
```

**Files Affected:**
- ~40 tests across 23 files

**Verification:**
```bash
# Before
make test-comprehensive | tee test_before.log

# After removal
make test-comprehensive | tee test_after.log

# Verify same pass count
diff test_before.log test_after.log
```

**Expected Outcome:** -40 tests, -0.3 minutes, 0% coverage loss

---

### Task 1.2: Remove Trivial Type Assertions (1 hour)

**Action:** Remove tests that only verify `isinstance` or `hasattr` with no business logic

**Pattern to Remove:**
```python
def test_service_is_correct_type():
    service = get_service()
    assert isinstance(service, ServiceClass)  # REMOVE: Would fail at runtime
    assert hasattr(service, "method")  # REMOVE: Would fail at runtime
```

**Files to Review:**
- `server/tests/unit/infrastructure/test_dependency_injection_functions.py`
- `server/tests/unit/infrastructure/test_dependency_injection.py`

**Specific Tests to Remove:**
1. `test_dependency_functions_are_callable` (tests Python basics)
2. `test_dependency_function_type_annotations` (mypy's job)
3. `test_service_instances_are_properly_configured` (trivial assertions)
4. `test_service_method_availability` (trivial hasattr checks)

**Expected Outcome:** -15 tests, -0.4 minutes, 0% coverage loss

---

### Task 1.3: Remove Duplicate Tests (30 minutes)

**Action:** Identify and remove duplicate tests that test the same code path

**Investigation:**
```bash
# Find tests with similar names
find server/tests -name "test_*.py" -exec basename {} \; | sort | uniq -d

# Find tests with identical assertions
grep -r "assert.*persistence.*container" server/tests/unit/infrastructure
```

**Likely Duplicates:**
- `test_dependency_injection.py` vs `test_dependency_functions.py` (similar DI tests)
- Multiple "service uses correct persistence" tests

**Expected Outcome:** -5 tests, -0.2 minutes, 0% coverage loss

---

### Task 1.4: Delete Empty Test File (5 minutes)

**Action:** Delete `server/tests/coverage/test_simple_coverage_gaps.py` (empty file)

**Command:**
```bash
rm server/tests/coverage/test_simple_coverage_gaps.py
```

**Expected Outcome:** -0 tests (already empty), cleaner structure

---

**Phase 1 Total:** -60 tests, -0.9 minutes, 2-4 hours effort

---

## Phase 2: Infrastructure Test Reduction (Week 2)

**Effort:** 4-6 hours
**Impact:** -120 tests, -2 minutes, LOW-MEDIUM RISK

### Task 2.1: Reduce Dependency Injection Tests (2 hours)

**Action:** Keep only meaningful DI tests, remove framework behavior tests

**File:** `server/tests/unit/infrastructure/test_dependency_injection_functions.py`

**REMOVE (9 tests):**
- `test_dependency_functions_are_callable`
- `test_dependency_function_type_annotations`
- `test_dependency_functions_performance` (non-failing benchmark)
- `test_dependency_functions_memory_usage` (placeholder assertion)
- `test_dependency_functions_thread_safety` (unstated requirement)
- `test_dependency_functions_request_parameter_validation`
- `test_dependency_functions_service_method_access`
- `test_get_player_service_for_testing_function` (meta-testing)
- `test_dependency_functions_with_testing_function` (meta-testing)

**KEEP (6 tests):**
- `test_get_player_service_function` (container DI integration)
- `test_get_room_service_function` (container DI integration)
- `test_dependency_functions_return_same_instances` (singleton verification)
- `test_dependency_functions_with_container_persistence` (shared state)
- `test_dependency_function_error_handling` (error scenario)
- `test_dependency_functions_consistency` (singleton consistency)

**Expected Outcome:** -9 tests, -0.5 minutes

---

### Task 2.2: Consolidate Dependency Injection Test Files (2 hours)

**Action:** Merge 3 similar test files into 1 comprehensive file

**Files to Merge:**
1. `test_dependency_injection_functions.py` (keep 6 tests)
2. `test_dependency_injection.py` (keep 7 tests)
3. `test_dependency_functions.py` (keep 10 tests)

**Result:** `test_dependency_injection_container.py` (23 tests total)

**Removed:** Duplicates and framework behavior tests

**Expected Outcome:** -35 tests, -0.7 minutes, improved organization

---

### Task 2.3: Reduce App Factory Tests (1 hour)

**Action:** Remove tests verifying FastAPI middleware behavior

**File:** `server/tests/unit/infrastructure/test_app_factory.py`

**REMOVE (Estimate 3-5 tests):**
- Tests that middleware is added (FastAPI behavior)
- Tests that headers exist (library behavior)

**KEEP:**
- Tests for custom CORS configuration logic
- Tests for security header configuration

**Expected Outcome:** -5 tests, -0.2 minutes

---

### Task 2.4: Review Lifespan Tests (1 hour)

**Action:** Remove duplicate or trivial lifespan tests

**File:** `server/tests/unit/infrastructure/test_lifespan.py`

**Review Criteria:**
- Keep tests verifying container initialization
- Keep tests verifying NATS enable/disable
- Remove tests verifying service attribute existence

**Expected Outcome:** -10 tests, -0.3 minutes

---

**Phase 2 Total:** -59 tests, -1.7 minutes, 4-6 hours effort

---

## Phase 3: Coverage Test Optimization (Week 3)

**Effort:** 6-8 hours
**Impact:** -80 tests, -1.5 minutes, MEDIUM RISK

### Task 3.1: Reduce Command Handler Coverage Tests (3 hours)

**Action:** Remove metric-driven tests, keep behavior tests

**File:** `server/tests/coverage/test_command_handler_coverage.py` (1,039 lines, ~50 tests)

**Pattern to Remove:**
```python
# REMOVE: Just executes code with trivial assertion
def test_command_returns_result():
    result = await process_command("say", ["hello"], ...)
    assert "result" in result  # Trivial assertion
```

**Pattern to Keep:**
```python
# KEEP: Verifies meaningful behavior
def test_command_validation_prevents_empty_message():
    result = await process_command("say", [], ...)
    assert "requires a message" in result["result"].lower()
```

**Expected Outcome:** -20 tests, -0.6 minutes

---

### Task 3.2: Reduce Error Logging Coverage Tests (2 hours)

**Action:** Remove tests that just verify logs were written

**File:** `server/tests/coverage/test_error_logging_coverage.py` (691 lines, ~30 tests)

**Pattern to Remove:**
```python
# REMOVE: Just verifies logger.error was called
def test_error_is_logged():
    with patch('logger.error') as mock_logger:
        do_something()
        mock_logger.assert_called()  # Verifies log call, not behavior
```

**Pattern to Keep:**
```python
# KEEP: Verifies error handling behavior
def test_error_returns_correct_response():
    response = do_something_that_errors()
    assert response.status_code == 500
    assert "error" in response.json()
```

**Expected Outcome:** -15 tests, -0.5 minutes

---

### Task 3.3: Merge Coverage Tests into Domain Tests (3 hours)

**Action:** Move valuable coverage tests into relevant domain test files, delete coverage directory

**Steps:**
1. Review each coverage test file
2. Move meaningful tests to domain files (e.g., `test_command_handler_coverage.py` → `test_command_handler.py`)
3. Delete pure metric tests
4. Delete coverage test directory if empty

**Files:**
- `test_command_rate_limiter_coverage.py` → merge into `test_rate_limiter.py`
- `test_help_content_coverage.py` → merge into `test_help_commands.py`
- `test_system_commands_coverage.py` → merge into `test_system_commands.py`

**Expected Outcome:** -45 tests, -0.4 minutes, improved organization

---

**Phase 3 Total:** -80 tests, -1.5 minutes, 6-8 hours effort

---

## Phase 4: Test Consolidation (Week 4)

**Effort:** 8-12 hours
**Impact:** -170 tests (consolidated), +0 minutes (same coverage), HIGH maintainability benefit

### Task 4.1: Parametrize Command Validation Tests (4 hours)

**Action:** Convert repetitive command validation tests into parametrized tests

**Current State:** ~100 separate tests testing command validation with different inputs

**Target Files:**
- `server/tests/unit/commands/test_command_handler.py`
- `server/tests/coverage/test_command_handler_coverage.py`
- `server/tests/unit/commands/test_admin_commands.py`

**Example Consolidation:**
```python
@pytest.mark.parametrize("command,args,expected_error", [
    ("say", [], "requires a message"),
    ("say", [""], "requires a message"),
    ("emote", [], "requires a message"),
    ("whisper", [], "requires a target"),
    ("whisper", ["target"], "requires a message"),
    ("go", [], "requires a direction"),
    ("teleport", [], "requires admin permission"),
    # ... 50+ more cases
])
@pytest.mark.asyncio
async def test_command_validation_errors(command, args, expected_error, mock_request):
    result = await process_command(command, args, mock_user, mock_request, ...)
    assert expected_error in result["result"].lower()
```

**Expected Outcome:** 100 tests → 30 parametrized tests (-70 test count, SAME coverage, better maintainability)

---

### Task 4.2: Parametrize Error Response Tests (3 hours)

**Action:** Convert API error response tests into parametrized tests

**Current State:** ~80 separate tests testing different error responses

**Target Files:**
- `server/tests/unit/api/test_players.py`
- `server/tests/unit/api/test_professions.py`
- `server/tests/integration/api/test_api_players_integration.py`

**Example Consolidation:**
```python
@pytest.mark.parametrize("endpoint,method,data,expected_status,expected_error", [
    ("/api/players/", "POST", {}, 422, "validation error"),
    ("/api/players/", "POST", {"name": ""}, 422, "name required"),
    ("/api/players/999", "GET", None, 404, "not found"),
    ("/api/rooms/invalid", "GET", None, 404, "room not found"),
    # ... 40+ more cases
])
def test_api_error_responses(endpoint, method, data, expected_status, expected_error, client):
    response = make_request(client, method, endpoint, data)
    assert response.status_code == expected_status
    assert expected_error in response.json().get("detail", "").lower()
```

**Expected Outcome:** 80 tests → 25 parametrized tests (-55 test count, SAME coverage)

---

### Task 4.3: Parametrize Permission Tests (2 hours)

**Action:** Convert authorization tests into parametrized tests

**Current State:** ~50 tests testing different permission scenarios

**Target Files:**
- `server/tests/security/test_admin_teleport_security.py`
- `server/tests/unit/commands/test_admin_commands.py`

**Example Consolidation:**
```python
@pytest.mark.parametrize("user_role,command,expected_status", [
    ("user", "teleport player1 room1", 403),
    ("admin", "teleport player1 room1", 200),
    ("user", "shutdown", 403),
    ("admin", "shutdown", 200),
    ("user", "add_admin other_user", 403),
    ("admin", "add_admin other_user", 200),
    # ... 30+ more cases
])
@pytest.mark.asyncio
async def test_admin_command_authorization(user_role, command, expected_status):
    user = create_user_with_role(user_role)
    result = await process_command(command, [], user, ...)
    assert result["status_code"] == expected_status
```

**Expected Outcome:** 50 tests → 15 parametrized tests (-35 test count, BETTER coverage)

---

### Task 4.4: Consolidate Similar Integration Tests (3 hours)

**Action:** Merge similar integration tests that test same workflow

**Target:** NPC integration tests (2 large files with overlapping coverage)

**Files:**
- `test_npc_integration.py` (959 lines)
- `test_npc_admin_commands_integration.py` (958 lines)

**Review for:**
- Duplicate setup/fixtures
- Overlapping test scenarios
- Opportunities to parametrize

**Expected Outcome:** -10 tests, better organization

---

**Phase 4 Total:** -170 test count (but SAME number of test cases via parametrization), improved maintainability

---

## Phase 5: Strategic Additions (Week 5)

**Effort:** 10-15 hours
**Impact:** +70 tests, +2 minutes, closes critical gaps

### Task 5.1: Add MessageBroker Integration Tests (3 hours)

**Priority:** 🔴 HIGH

**New File:** `server/tests/integration/infrastructure/test_message_broker_integration.py`

**Tests to Add:** 15 tests
1. `test_message_broker_protocol_compliance`
2. `test_nats_broker_connection_lifecycle`
3. `test_nats_broker_publish_message`
4. `test_nats_broker_subscribe_to_subject`
5. `test_nats_broker_connection_error_recovery`
6. `test_nats_broker_message_serialization`
7. `test_nats_broker_queue_group_behavior`
8. `test_nats_broker_reconnect_on_failure`
9. `test_nats_broker_graceful_shutdown`
10. `test_nats_broker_concurrent_publishing`
11. `test_nats_broker_subscriber_error_handling`
12. `test_nats_broker_message_ordering`
13. `test_nats_broker_backpressure_handling`
14. `test_nats_broker_connection_timeout`
15. `test_nats_broker_authentication`

**Expected Outcome:** +15 tests, +0.5 minutes, critical gap closed

---

### Task 5.2: Add ApplicationContainer Lifecycle Tests (2 hours)

**Priority:** 🔴 HIGH

**New File:** `server/tests/integration/infrastructure/test_container_lifecycle.py`

**Tests to Add:** 10 tests
1. `test_container_initialization_order`
2. `test_container_service_dependencies_resolved`
3. `test_container_shutdown_cleanup`
4. `test_container_initialization_failure_recovery`
5. `test_container_double_initialization_prevented`
6. `test_container_services_are_singletons`
7. `test_container_persistence_shared_across_services`
8. `test_container_event_bus_wiring`
9. `test_container_graceful_shutdown_on_error`
10. `test_container_resource_cleanup_on_failure`

**Expected Outcome:** +10 tests, +0.4 minutes, critical gap closed

---

### Task 5.3: Add Database Migration Tests (3 hours)

**Priority:** 🔴 HIGH

**New File:** `server/tests/integration/infrastructure/test_database_migrations.py`

**Tests to Add:** 10 tests
1. `test_migration_adds_missing_column`
2. `test_migration_preserves_existing_data`
3. `test_migration_handles_corrupted_schema`
4. `test_migration_rollback_on_failure`
5. `test_migration_idempotent` (can run multiple times safely)
6. `test_init_db_creates_all_tables`
7. `test_init_db_enables_foreign_keys`
8. `test_database_schema_validation`
9. `test_migration_adds_respawn_room_id_column`
10. `test_database_integrity_check`

**Expected Outcome:** +10 tests, +0.4 minutes, data integrity protection

---

### Task 5.4: Add WebSocket Edge Case Tests (4 hours)

**Priority:** 🟡 HIGH

**New File:** `server/tests/integration/realtime/test_websocket_edge_cases.py`

**Tests to Add:** 15 tests
1. `test_websocket_handles_simultaneous_disconnect`
2. `test_websocket_handles_slow_client`
3. `test_websocket_handles_message_queue_overflow`
4. `test_websocket_handles_connection_timeout`
5. `test_websocket_prevents_duplicate_connections`
6. `test_websocket_handles_malformed_messages`
7. `test_websocket_handles_connection_during_shutdown`
8. `test_websocket_recovers_from_send_failure`
9. `test_websocket_handles_client_reconnection`
10. `test_websocket_handles_rapid_reconnections`
11. `test_websocket_cleanup_on_abnormal_close`
12. `test_websocket_handles_ping_pong_timeout`
13. `test_websocket_rate_limits_messages`
14. `test_websocket_handles_authentication_failure`
15. `test_websocket_handles_broadcast_failure`

**Expected Outcome:** +15 tests, +0.5 minutes, reliability improvement

---

### Task 5.5: Add Error Recovery Tests (3 hours)

**Priority:** 🟡 MEDIUM

**New File:** `server/tests/integration/comprehensive/test_error_recovery.py`

**Tests to Add:** 20 tests
1. `test_game_continues_on_database_error`
2. `test_game_continues_on_nats_unavailable`
3. `test_player_moved_to_default_room_on_invalid_room`
4. `test_command_fails_gracefully_on_service_error`
5. `test_chat_message_fails_gracefully_on_broadcast_error`
6. `test_movement_fails_gracefully_on_room_load_error`
7. `test_npc_spawn_fails_gracefully_on_data_error`
8. `test_combat_cancels_gracefully_on_participant_disconnect`
9. `test_persistence_falls_back_on_write_error`
10. `test_event_bus_continues_on_handler_error`
11. `test_connection_manager_handles_websocket_close_error`
12. `test_api_returns_500_on_unexpected_error`
13. `test_authentication_fails_gracefully_on_jwt_error`
14. `test_rate_limiter_fails_open_on_redis_error`
15. `test_room_cache_falls_back_on_cache_miss`
16. `test_profession_cache_falls_back_on_cache_miss`
17. `test_health_check_reports_degraded_on_service_error`
18. `test_monitoring_continues_on_metric_collection_error`
19. `test_logging_continues_on_log_aggregator_error`
20. `test_shutdown_completes_even_with_cleanup_errors`

**Expected Outcome:** +20 tests, +0.7 minutes, reliability greatly improved

---

**Phase 5 Total:** +70 tests, +2 minutes, critical gaps closed

---

## Phase 6: Long-Term Optimizations (Ongoing)

**Effort:** Continuous
**Impact:** Improved quality over time

### Task 6.1: Establish Test Quality Gates

**Implementation:** Update pre-commit hooks and CI/CD

**New Rules:**
1. **No Placeholder Assertions:** Reject tests with `assert True` without justification
2. **No Framework Behavior Tests:** Reject tests verifying library/framework behavior
3. **Meaningful Assertions Required:** All tests must have behavioral assertions
4. **AAA Pattern Required:** All tests must follow Arrange-Act-Assert
5. **Test Justification Required:** New tests must have docstring explaining value

**Implementation:**
```python
# Add to pre-commit configuration
# .pre-commit-config.yaml
  - repo: local
    hooks:
      - id: check-test-quality
        name: Check Test Quality
        entry: python scripts/check_test_quality.py
        language: python
        files: ^server/tests/.*test_.*\.py$
```

**Script:** `scripts/check_test_quality.py`
```python
# Reject tests with common anti-patterns
def check_test_quality(file_path):
    content = read_file(file_path)

    # Check for placeholder assertions
    if "assert True  # Placeholder" in content:
        raise ValueError(f"{file_path}: Placeholder assertion found")

    # Check for trivial isinstance without behavior
    if has_only_isinstance_assertions(content):
        warn(f"{file_path}: Consider testing behavior, not types")

    # More checks...
```

---

### Task 6.2: Monthly Test Quality Review

**Implementation:** Scheduled review process

**Monthly Tasks:**
1. Review slowest 10 tests for optimization opportunities
2. Review most frequently failing tests for fragility
3. Review newest tests for quality
4. Identify and remove any new low-value tests
5. Update this roadmap with findings

**Metrics to Track:**
- Total test count
- Test execution time
- Test failure rate
- Coverage percentage
- Tests added vs removed

---

### Task 6.3: Performance Optimization

**Investigation:** Profile slowest tests

**Approach:**
```bash
# Identify slowest tests
uv run pytest server/tests --durations=50

# For each slow test, investigate:
# - Is it doing unnecessary I/O?
# - Is it creating too much test data?
# - Can fixtures be optimized?
# - Can database operations be mocked?
```

**Target:** Optimize top 20 slowest tests

**Expected Outcome:** -2-3 minutes total execution time

---

### Task 6.4: Parallel Test Execution (Investigation)

**Goal:** Run independent tests in parallel

**Approach:**
```bash
# Install pytest-xdist
uv pip install pytest-xdist

# Run tests in parallel
uv run pytest server/tests -n auto
```

**Considerations:**
- Database tests must remain serial (per current config)
- WebSocket tests may have port conflicts
- Fixtures may need thread-safety review

**Potential Impact:** -10-15 minutes if successful (50% faster)

---

## Implementation Timeline

### Month 1: Pruning and Quick Wins
- **Week 1:** Phase 1 (Quick Wins) - Remove placeholder and trivial tests
- **Week 2:** Phase 2 (Infrastructure) - Reduce DI and framework tests
- **Week 3:** Phase 3 (Coverage) - Optimize coverage-driven tests
- **Week 4:** Review and verify no coverage regression

**Outcome:** -200 tests, -4 minutes, 12-18 hours effort

### Month 2: Consolidation and Additions
- **Week 5:** Phase 4 (Consolidation) - Parametrize repetitive tests
- **Week 6:** Phase 5 (Additions) - Add critical gap tests (MessageBroker, Container)
- **Week 7:** Phase 5 (Additions) - Add reliability tests (WebSocket, Error Recovery)
- **Week 8:** Phase 5 (Additions) - Add migration and configuration tests

**Outcome:** -170 consolidated, +70 added, +2 minutes, 20-30 hours effort

### Month 3+: Continuous Improvement
- **Ongoing:** Phase 6 (Quality Gates) - Prevent low-value test additions
- **Monthly:** Phase 6 (Reviews) - Identify new optimization opportunities
- **Quarterly:** Phase 6 (Performance) - Optimize slowest tests

**Outcome:** Sustained quality improvement

---

## Net Impact Projection

### After Month 1 (Pruning Phase)
- **Tests:** 4,965 → 4,765 (-200, -4%)
- **Time:** 30 min → 26 min (-4 min, -13%)
- **Coverage:** 82% → 81.5% (-0.5%)
- **Critical Coverage:** 95% → 95% (maintained)
- **Test Quality Score:** 85% → 93% (+8%)

### After Month 2 (Consolidation + Additions)
- **Tests:** 4,765 → 4,665 (-170 consolidated, +70 added)
- **Time:** 26 min → 24 min (-2 min, but +2 for additions = 26 min net)
- **Coverage:** 81.5% → 82.5% (+1%, gaps filled)
- **Critical Coverage:** 95% → 98% (+3%, critical gaps filled)
- **Test Quality Score:** 93% → 96% (+3%)

### After Month 3+ (Continuous Improvement)
- **Tests:** ~4,500-4,700 (stable, quality-focused)
- **Time:** ~22-25 min (optimized, possible parallel execution)
- **Coverage:** ~82-85% (high-value coverage)
- **Critical Coverage:** ~98-99% (comprehensive)
- **Test Quality Score:** ~96-98% (sustained high quality)

---

## Risk Mitigation Strategy

### Safety Measures

**1. Coverage Baseline:**
```bash
# Capture current coverage
make coverage > baseline_coverage.txt
git add baseline_coverage.txt
git commit -m "Test optimization baseline"
```

**2. Incremental Removal:**
- Remove max 20 tests per commit
- Run full test suite after each commit
- Verify coverage after each commit
- Easy rollback with `git revert`

**3. Test Removal Log:**
Create `TEST_REMOVAL_LOG.md` to track:
- Which test was removed
- Why it was removed
- Coverage impact
- Commit hash for rollback

**4. Staged Rollout:**
- Implement on feature branch
- Review with team before merging
- Monitor for 1 week after merge
- Rollback if issues found

---

## Monitoring and Validation

### Weekly Metrics

Track these metrics weekly during optimization:

| Metric | Week 0 (Baseline) | Target | Actual |
|--------|-------------------|--------|--------|
| Total Tests | 4,965 | 4,665 | ? |
| Execution Time | 30 min | 25 min | ? |
| Test Failures | ~10 | <10 | ? |
| Code Coverage | 82% | 81%+ | ? |
| Critical Coverage | 95% | 95%+ | ? |
| False Positives | ? | Reduced | ? |

### Monthly Review Questions

1. Did we maintain or improve coverage?
2. Did we reduce execution time?
3. Are test failures more meaningful?
4. Did we add tests for critical gaps?
5. Is test maintenance easier?

---

## Success Criteria

### Quantitative Goals

- ✅ Remove ≥200 low-value tests (10% reduction)
- ✅ Save ≥4 minutes execution time (13% faster)
- ✅ Maintain ≥80% code coverage
- ✅ Maintain ≥95% critical code coverage
- ✅ Add ≥50 tests for critical gaps

### Qualitative Goals

- ✅ Improve test signal-to-noise ratio from 85% to 95%+
- ✅ Reduce test maintenance burden
- ✅ Make test failures more actionable
- ✅ Improve team confidence in test suite
- ✅ Establish sustainable test quality process

---

## Rollback Plan

**If coverage drops below 80%:**

```bash
# Identify which commit caused drop
git log --oneline TEST_REMOVAL_LOG.md

# Revert the problematic commit
git revert <commit-hash>

# Re-run coverage
make coverage

# Document in TEST_REMOVAL_LOG.md why revert was needed
```

**If critical bug missed:**

1. Add regression test for the bug FIRST
2. Fix the bug
3. Review: Would any removed test have caught this?
4. If yes: Re-add that test category
5. Update pruning criteria to prevent similar removal

---

## Recommended Execution Order

**Start Here (Highest Confidence):**

1. ✅ Remove placeholder tests (40 tests, 0% risk)
2. ✅ Remove trivial type assertions (15 tests, 0% risk)
3. ✅ Remove duplicate tests (5 tests, 0% risk)
4. ✅ Delete empty file (0 tests, 0% risk)

**Then (High Confidence):**

5. ✅ Reduce DI function tests (25 tests, 5% risk)
6. ✅ Consolidate DI test files (35 tests, 10% risk)
7. ✅ Reduce coverage tests (40 tests, 10% risk)

**Then (Medium Confidence):**

8. ✅ Parametrize command validation (70 consolidated, 5% risk)
9. ✅ Parametrize error responses (55 consolidated, 5% risk)
10. ✅ Parametrize permission tests (35 consolidated, 5% risk)

**Finally (Strategic):**

11. ✅ Add MessageBroker tests (15 added, 0% risk)
12. ✅ Add Container tests (10 added, 0% risk)
13. ✅ Add migration tests (10 added, 0% risk)
14. ✅ Add WebSocket edge cases (15 added, 0% risk)
15. ✅ Add error recovery tests (20 added, 0% risk)

---

*"Optimization is not the enemy of quality — it is quality's closest ally, removing the noise so the signal may be heard clearly."*

— From the Necronomicon of Software Engineering, Chapter on Test Suite Hygiene
