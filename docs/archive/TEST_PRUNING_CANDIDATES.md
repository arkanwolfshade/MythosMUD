# Test Pruning Candidates - Detailed List

> *"Not all rituals in the test chambers serve a purpose. Some are merely ceremonial, performing incantations that
verify the obvious while consuming precious time."*

**Purpose:** Specific tests recommended for removal or consolidation to optimize test suite quality and execution time.

---

## Immediate Pruning Candidates (High Confidence)

### Category A: Infrastructure Tests Testing Framework Behavior

#### File: `server/tests/unit/infrastructure/test_dependency_injection_functions.py`

**REMOVE (Low Value - 9 tests):**

1. **`test_dependency_functions_are_callable`**

   **Reason:** Tests that functions are callable (Python basic behavior)

   **Value:** Would fail at import time if broken
   - **Lines:** ~5

2. **`test_dependency_function_type_annotations`**

   **Reason:** Tests that type annotations exist (static analysis job)

   **Value:** Mypy catches this
   - **Lines:** ~15

3. **`test_dependency_functions_performance`**

   **Reason:** Non-failing benchmark (doesn't prevent bugs)

   **Value:** Performance monitoring, not regression protection
   - **Lines:** ~20

4. **`test_dependency_functions_memory_usage`**

   **Reason:** Non-failing memory check with placeholder assertion

   **Value:** `assert True  # Placeholder`
   - **Lines:** ~15

5. **`test_dependency_functions_thread_safety`**

   **Reason:** Thread safety is not a stated requirement

   **Value:** Testing unstated requirement
   - **Lines:** ~25

6. **`test_dependency_functions_request_parameter_validation`**

   **Reason:** Tests that None raises TypeError (Python behavior)

   **Value:** Would fail at runtime
   - **Lines:** ~10

7. **`test_dependency_functions_service_method_access`**

   **Reason:** Tests that methods exist with `hasattr` and `callable`

   **Value:** Would fail at runtime
   - **Lines:** ~15

8. **`test_get_player_service_for_testing_function`**

   **Reason:** Tests a testing utility function (meta-testing)

   **Value:** Testing test infrastructure
   - **Lines:** ~10

9. **`test_dependency_functions_with_testing_function`**

   **Reason:** Duplicate of above

   **Value:** Testing test infrastructure
   - **Lines:** ~10

**KEEP (Medium Value - 6 tests):**

- `test_get_player_service_function` - Verifies container DI integration
- `test_get_room_service_function` - Verifies container DI integration
- `test_dependency_functions_return_same_instances` - Verifies singleton pattern
- `test_dependency_functions_with_container_persistence` - Verifies shared persistence
- `test_dependency_function_error_handling` - Verifies error when container missing
- `test_dependency_functions_consistency` - Verifies singleton consistency

**Total Removal:** 9 tests, ~125 lines, ~0.5 minutes

---

#### File: `server/tests/unit/infrastructure/test_dependency_injection.py`

**REMOVE (Low Value - 8 tests):**

1. **`test_player_service_dependency_resolution`**

   **Reason:** Tests that DI returns non-None (trivial)

   **Value:** Would fail at runtime

2. **`test_room_service_dependency_resolution`**

   **Reason:** Same as above for room service

   **Value:** Would fail at runtime

3. **`test_dependency_injection_in_fastapi_app`**

   **Reason:** Tests FastAPI framework DI behavior

   **Value:** Tests framework, not our code

4. **`test_dependency_injection_with_real_services`**

   **Reason:** Tests that creating services works (trivial)

   **Value:** Would fail at startup

5. **`test_fastapi_depends_mechanism`**

   **Reason:** Tests FastAPI's `Depends` mechanism (framework test)

   **Value:** Testing framework behavior

6. **`test_service_instances_are_properly_configured`**

   **Reason:** Tests that instances have attributes (trivial)

   **Value:** Would fail at runtime

7. **`test_service_method_availability`**

   **Reason:** Tests methods exist with `hasattr` (trivial)

   **Value:** Would fail at runtime

8. **`test_app_state_consistency`**

   **Reason:** Tests that app.state assignments work (Python behavior)

   **Value:** Would fail at startup

**KEEP (Medium Value - 7 tests):**

- `test_get_player_service_creates_instance` - Verifies DI configuration
- `test_get_room_service_creates_instance` - Verifies DI configuration
- `test_dependency_injection_error_handling` - Verifies error scenarios
- `test_dependency_functions_return_same_instances` - Verifies singleton
- `test_dependency_functions_with_container_persistence` - Verifies shared state
- `test_dependency_functions_require_container` - Verifies requirements
- `test_dependency_functions_use_container_persistence` - Verifies persistence injection

**Total Removal:** 8 tests, ~100 lines, ~0.4 minutes

---

#### File: `server/tests/unit/infrastructure/test_app_factory.py`

**Analysis Needed:** Review for framework behavior tests

**Likely REMOVE (Estimate 3-5 tests):**

- Tests verifying middleware is added (FastAPI behavior)
- Tests verifying CORS headers exist (CORS library behavior)
- Tests that app is a FastAPI instance

**Likely KEEP:**

- Tests verifying our custom CORS configuration logic
- Tests verifying security headers configuration

---

#### File: `server/tests/unit/infrastructure/test_lifespan.py`

**Analysis Needed:** Review for framework vs application logic tests

**Likely KEEP (Most tests):**

- Lifespan tests verify critical startup/shutdown logic
- These could catch initialization bugs
- **Recommendation:** Keep most, review for duplicates

---

### Category B: Coverage Tests Written for Metrics

#### File: `server/tests/coverage/test_error_logging_coverage.py` (691 lines)

**REMOVE (Low Value - Estimate 15-20 tests):**

**Pattern to Remove:**
Tests that verify logs were written without verifying behavior:

```python
def test_error_is_logged():
    with patch('server.logging.logger') as mock_logger:
        do_something_that_errors()
        mock_logger.error.assert_called()  # Just verifies log call, not behavior
```

**KEEP:**

- Tests verifying error handling behavior (error recovery, fallbacks)
- Tests verifying error responses are correct
- Tests verifying critical errors are tracked

**Total Removal:** ~20 tests, ~250 lines, ~0.6 minutes

---

#### File: `server/tests/coverage/test_command_handler_coverage.py` (1,039 lines)

**REMOVE (Low Value - Estimate 15-20 tests):**

**Pattern to Remove:**
Tests that execute code with no meaningful assertions:

```python
def test_command_returns_result():
    result = process_command("say", ["hello"], ...)
    assert "result" in result  # Trivial assertion
```

**KEEP:**

- Tests verifying command validation logic
- Tests verifying error messages are correct
- Tests verifying security/rate limiting

**Total Removal:** ~20 tests, ~300 lines, ~0.6 minutes

---

### Category C: Model Property Tests

#### Files: `server/tests/unit/models/test_*.py`

**REMOVE Pattern (Estimate 30-50 tests across all model tests):**

```python
def test_player_name_getter():
    player = Player(name="Test")
    assert player.name == "Test"  # Tests Python assignment

def test_room_id_setter():
    room = Room(id="123")
    assert room.id == "123"  # Tests Python assignment

def test_player_repr():
    player = Player(name="Test")
    assert "Test" in repr(player)  # Tests __repr__ returns string
```

**KEEP:**

- Tests verifying calculated properties
- Tests verifying validation logic in setters
- Tests verifying complex model methods

**Total Removal:** ~40 tests, ~200 lines, ~0.3 minutes

---

## Pruning Summary

| Category                     | Files   | Tests to Remove | Lines to Remove | Time Saved   |
| ---------------------------- | ------- | --------------- | --------------- | ------------ |
| **Infrastructure DI Tests**  | 3       | ~25             | ~350            | ~1.2 min     |
| **Coverage Tests**           | 2       | ~40             | ~550            | ~1.2 min     |
| **Model Property Tests**     | ~10     | ~40             | ~200            | ~0.3 min     |
| **Framework Behavior Tests** | ~5      | ~15             | ~150            | ~0.5 min     |
| **Performance/Memory Tests** | ~3      | ~10             | ~80             | ~0.3 min     |
| **TOTAL**                    | **~23** | **~130**        | **~1,330**      | **~3.5 min** |

---

## Consolidation Candidates

### High-Impact Consolidations

#### 1. Command Validation Tests

**Current:** ~100 separate tests across multiple files
**Pattern:** Testing same validation logic with different commands

**Consolidation:**

```python
@pytest.mark.parametrize("command,args,expected_error", [
    ("say", [], "requires a message"),
    ("emote", [], "requires a message"),
    ("whisper", ["targetuser"], "requires a message"),
    ("go", [], "requires a direction"),
    # ... 50+ more cases

])
def test_command_validation_errors(command, args, expected_error):
    result = await process_command(command, args, ...)
    assert expected_error in result["result"].lower()
```

**Impact:** 100 tests → 25 parametrized tests, -75 test count, SAME coverage

---

#### 2. Error Response Tests

**Current:** ~80 separate tests for different error scenarios
**Pattern:** Verifying error messages for different invalid inputs

**Consolidation:**

```python
@pytest.mark.parametrize("endpoint,method,data,expected_status", [
    ("/api/players/", "POST", {}, 422),
    ("/api/players/", "POST", {"invalid": "data"}, 422),
    ("/api/rooms/nonexistent", "GET", None, 404),
    # ... 40+ more cases

])
def test_api_error_responses(endpoint, method, data, expected_status):
    if method == "POST":
        response = client.post(endpoint, json=data)
    else:
        response = client.get(endpoint)
    assert response.status_code == expected_status
```

**Impact:** 80 tests → 20 parametrized tests, -60 test count, SAME coverage

---

#### 3. Permission Check Tests

**Current:** ~50 separate tests for authorization checks
**Pattern:** Verifying different users can/cannot access resources

**Consolidation:**

```python
@pytest.mark.parametrize("user_role,endpoint,method,expected_status", [
    ("user", "/api/admin/teleport", "POST", 403),
    ("admin", "/api/admin/teleport", "POST", 200),
    ("user", "/api/players/", "GET", 200),
    # ... 30+ more cases

])
def test_authorization_checks(user_role, endpoint, method, expected_status):
    client = create_client_with_role(user_role)
    response = client.request(method, endpoint)
    assert response.status_code == expected_status
```

**Impact:** 50 tests → 15 parametrized tests, -35 test count, BETTER coverage

---

## Total Impact Estimate

### Conservative Estimate (Implement Phase A + Basic Parametrization)

**Tests Removed:** ~200 low-value tests

**Tests Consolidated:** ~170 tests → ~50 parametrized tests

**Net Reduction:** ~320 tests (6.4% of suite)

**Time Saved:** ~3.5 minutes (12% faster)

**Effort:** ~4-6 hours

### Aggressive Estimate (Full Optimization)

**Tests Removed:** ~350 low-value tests

**Tests Consolidated:** ~320 tests → ~100 parametrized tests

**Net Reduction:** ~570 tests (11.5% of suite)

**Time Saved:** ~5-6 minutes (17-20% faster)

**Effort:** ~12-16 hours

---

## Risk Mitigation

**Before removing any tests:**

1. **Run coverage comparison:**

   ```bash
   # Before pruning

   make coverage > coverage_before.txt

   # After pruning

   make coverage > coverage_after.txt

   # Verify no coverage loss

   diff coverage_before.txt coverage_after.txt
   ```

2. **Review git blame:**

   - Check when test was added
   - Check if test caught a bug in the past
   - Check commit message for context

3. **Gradual removal:**

   - Remove 10-20 tests at a time
   - Run full suite after each batch
   - Verify no coverage regression

4. **Keep detailed log:**

   - Document each removed test
   - Justify removal reasoning
   - Enable easy rollback if needed

---

## Recommended Pruning Order

### Week 1: Quick Wins (Low Risk)

1. Delete empty `test_simple_coverage_gaps.py`
2. Remove trivial assertions (`assert isinstance`, `assert callable`)
3. Remove `assert True` placeholder tests (40 tests)
4. Remove duplicate tests

**Total:** ~60 tests, ~1 minute saved

### Week 2: Infrastructure Tests (Medium Risk)

1. Reduce `test_dependency_injection_functions.py` by 60%
2. Reduce `test_dependency_injection.py` by 60%
3. Reduce `test_dependency_functions.py` by 50%
4. Review `test_app_factory.py` for framework tests

**Total:** ~70 tests, ~1.5 minutes saved

### Week 3: Coverage Tests (Medium Risk)

1. Review and prune `test_error_logging_coverage.py`
2. Review and prune `test_command_handler_coverage.py`
3. Merge remaining valuable tests into domain test files
4. Delete coverage test directory if empty

**Total:** ~50 tests, ~1 minute saved

### Week 4: Consolidation (Low Risk, High Maintenance Benefit)

1. Parametrize command validation tests
2. Parametrize error response tests
3. Parametrize permission check tests

**Total:** ~170 tests consolidated to ~50, maintains coverage, improves maintainability

---

## Specific Test Removal Justifications

### Pattern 1: Testing Python Language Features

```python
# REMOVE: Tests Python assignment

def test_player_name_property():
    player = Player(name="TestName")
    assert player.name == "TestName"

# REMOVE: Tests Python type checking

def test_service_is_instance():
    service = get_player_service(request)
    assert isinstance(service, PlayerService)

# REMOVE: Tests Python attribute existence

def test_service_has_method():
    service = get_player_service(request)
    assert hasattr(service, "create_player")
```

**Justification:** These would fail immediately at runtime if broken. No regression protection.

### Pattern 2: Testing Framework Behavior

```python
# REMOVE: Tests FastAPI DI mechanism

def test_fastapi_depends_works():
    # Tests that FastAPI's Depends() works
    # This is testing the framework, not our code

# REMOVE: Tests Pydantic validation

def test_pydantic_validates_required_fields():
    # Tests that Pydantic enforces required fields
    # This is testing the library, not our schema

```

**Justification:** We don't own the framework. Framework tests belong in the framework's test suite.

### Pattern 3: Tests with No Real Assertions

```python
# REMOVE: Placeholder test

def test_memory_usage():
    # ... do something ...

    assert True  # Placeholder assertion

# REMOVE: Non-failing benchmark

def test_performance_acceptable():
    elapsed = measure_operation()
    # No assertion, just prints timing

```

**Justification:** Tests that can't fail don't prevent bugs.

### Pattern 4: Testing the Test Infrastructure

```python
# REMOVE: Meta-testing

def test_mock_persistence_fixture():
    # Tests that our test fixture works

    mock = mock_persistence()
    assert mock is not None

# REMOVE: Testing test utilities

def test_get_player_service_for_testing_function():
    # Tests a function we only use in tests

    service = get_player_service_for_testing()
    assert service is not None
```

**Justification:** Testing test code, not application code. Low value.

---

## Coverage Impact Analysis

### Projected Coverage Impact

**Before Pruning:**

- Total Tests: 4,965
- Code Coverage: ~82%
- Critical Code Coverage: ~95%

**After Pruning (Conservative):**

- Total Tests: 4,645 (-320 tests)
- Code Coverage: ~81.5% (-0.5%)
- Critical Code Coverage: ~95% (no change)

**After Pruning (Aggressive):**

- Total Tests: 4,395 (-570 tests)
- Code Coverage: ~80.5% (-1.5%)
- Critical Code Coverage: ~95% (no change)

**Analysis:**

- Slight overall coverage decrease acceptable (still above 80% target)
- Critical code coverage maintained (security, core features)
- Coverage decrease is in low-value code paths (error logging, framework integration)

---

## Conclusion

**Recommended First Action:**

Remove the 40 tests with `assert True` / `# Placeholder` assertions immediately:

- Zero risk (they literally don't test anything)
- Quick win (~0.3 minutes saved)
- Easy to verify (just search and remove)

**Second Action:**

Review and remove 25 tests from `test_dependency_injection_functions.py`:

- Low risk (would fail at runtime if DI broke)
- Medium win (~0.7 minutes saved)
- Requires careful review of each test

**Third Action:**

Parametrize 100 command validation tests into 25 parametrized tests:

- Zero risk (same coverage)
- Major maintainability win
- ~0.5 minutes saved
- Much easier to add new test cases

---

*"Prune the test suite as one prunes a bonsai tree — carefully, deliberately, and with full understanding of the shape
you wish to achieve."*
