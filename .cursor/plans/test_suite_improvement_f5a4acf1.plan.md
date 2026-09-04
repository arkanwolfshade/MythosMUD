---
name: Test Suite Improvement
overview: Comprehensive remediation plan with detailed step-by-step instructions for addressing anti-patterns, best practice violations, and structural issues in the test suite.
todos:

  - id: audit-autouse-fixtures

    content: Run grep to find all autouse fixtures and document which modify global state
    status: completed

  - id: add-remaining-serial-markers

    content: Add @pytest.mark.serial and @pytest.mark.xdist_group to tests missing them
    status: completed
    dependencies:

      - audit-autouse-fixtures

  - id: verify-worker-stability

    content: Run parallel tests to verify no worker crashes after serial marker fixes
    status: completed
    dependencies:

      - add-remaining-serial-markers

  - id: delete-weak-coverage-tests

    content: Delete weak tests in test_error_logging_coverage.py that only raise exceptions
    status: completed

  - id: fix-assert-true-movement

    content: Fix assert True in test_movement_service.py line ~782
    status: completed

  - id: fix-assert-true-error-logging

    content: Fix assert True in test_error_logging.py line ~342
    status: completed

  - id: fix-assert-true-event-system

    content: Fix assert True in test_event_system.py line ~437
    status: completed

  - id: fix-assert-true-health-monitor

    content: Fix assert True in test_health_monitor.py line ~737
    status: completed

  - id: fix-assert-true-security-middleware

    content: Fix assert True in test_security_middleware.py line ~539
    status: completed

  - id: define-test-markers

    content: Add slow/integration/security/e2e markers to pyproject.toml
    status: completed

  - id: apply-integration-markers

    content: Add pytestmark = pytest.mark.integration to all files in integration/
    status: completed
    dependencies:

      - define-test-markers

  - id: apply-security-markers

    content: Add pytestmark = pytest.mark.security to all files in security/
    status: completed
    dependencies:

      - define-test-markers

  - id: apply-performance-markers

    content: Add @pytest.mark.slow to all files in performance/
    status: completed
    dependencies:

      - define-test-markers

  - id: move-fixtures-tests

    content: Move test_error_logging.py from fixtures/ to unit/utils/
    status: completed

  - id: final-verification

    content: Run make test to verify all changes work correctly
    status: completed
    dependencies:

      - verify-worker-stability

      - delete-weak-coverage-tests

      - fix-assert-true-movement

      - fix-assert-true-error-logging

      - fix-assert-true-event-system

      - fix-assert-true-health-monitor

      - fix-assert-true-security-middleware

      - apply-integration-markers

      - apply-security-markers

      - apply-performance-markers

      - move-fixtures-tests

---

# Test Suite Improvement Plan - Detailed Implementation Guide

This plan provides specific, actionable instructions for improving the MythosMUD test suite based on pytest, asyncio, PostgreSQL, Pydantic, SQLAlchemy, and Uvicorn best practices.---

## Phase 1: Worker Stability - Audit and Fix Global State Issues

### Task 1.1: Audit All Classes with Autouse Fixtures

**Goal:** Identify test classes that have `autouse=True` fixtures that modify global state.**Step 1:** Run this grep command to find all autouse fixtures:

```powershell
grep -r "autouse=True" server/tests --include="*.py" -B 2 -A 10
```

**Step 2:** For each autouse fixture found, check if it calls any of these global-state-modifying functions:

- `reset_config()`
- `get_config()`
- `EventBus()` creation or modification
- Any singleton pattern resets

**Files already known to have this issue:**

- [`server/tests/unit/config/test_feature_flags.py`](server/tests/unit/config/test_feature_flags.py) - FIXED (28 serial markers)
- [`server/tests/unit/infrastructure/test_config.py`](server/tests/unit/infrastructure/test_config.py) - FIXED (5 serial markers in TestAppConfig)
- [`server/tests/unit/events/test_event_bus.py`](server/tests/unit/events/test_event_bus.py) - Has 17 serial markers

**Step 3:** Document any classes found that need serial markers.

### Task 1.2: Add Serial Markers to Remaining Tests

**Goal:** Ensure ALL tests in classes with global-state autouse fixtures have serial markers.**Pattern to add before each test method in affected classes:**

```python
@pytest.mark.serial  # Class uses autouse fixture that modifies global config state
@pytest.mark.xdist_group(name="serial_config_tests")  # Force serial execution with pytest-xdist
def test_example(self) -> None:
```

**Verification command:**

```powershell
cd E:\projects\GitHub\MythosMUD
uv run pytest server/tests/unit/config/test_feature_flags.py -v -n 4 2>&1 | Select-Object -Last 30
```

All tests should pass with no worker crashes.---

## Phase 2: Remove Weak/Invalid Tests

### Task 2.1: Delete Weak Exception-Only Tests

**Goal:** Remove tests that only verify Python can raise exceptions without testing server code.**File to modify:** [`server/tests/coverage/test_error_logging_coverage.py`](server/tests/coverage/test_error_logging_coverage.py)**Tests to DELETE (they only test that exceptions can be raised, not server behavior):**

1. `test_websocket_connection_error_logging` - Only does `raise ConnectionError(...)`
2. `test_websocket_message_error_logging` - Only does `raise ValueError(...)`
3. `test_database_connection_error_logging` - Only does `raise DatabaseError(...)`
4. `test_database_session_error_logging` - Only does `raise DatabaseError(...)`

**How to identify these tests:** Search for this pattern:

```python
with pytest.raises(SomeError):
    raise SomeError("message")  # This is the anti-pattern - raising manually instead of calling server code
```

**Action:** Delete the entire test method for each weak test found.

### Task 2.2: Fix `assert True` Anti-Patterns

**Goal:** Replace meaningless `assert True` statements with actual assertions.**File 1:** [`server/tests/unit/world/test_movement_service.py`](server/tests/unit/world/test_movement_service.py) line ~782**Find:**

```python
# Verify that the service handled movements correctly
# (no exceptions should have been raised)

assert True  # If we get here, no exceptions were raised
```

**Replace with:**

```python
# Verify the service completed without exceptions
# The test implicitly passes if no exception was raised during execution
# No explicit assertion needed - pytest will fail on any uncaught exception

```

Or add a meaningful assertion like:

```python
assert result is not None, "Movement service should return a result"
```

**File 2:** [`server/tests/unit/utils/test_error_logging.py`](server/tests/unit/utils/test_error_logging.py) line ~342**Find:**

```python
# If we get here without memory issues, the test passes

assert True
```

**Replace with:** Remove the assert True entirely, or add a meaningful assertion about the test's actual outcome.**File 3:** [`server/tests/unit/events/test_event_system.py`](server/tests/unit/events/test_event_system.py) line ~437**File 4:** [`server/tests/unit/realtime/monitoring/test_health_monitor.py`](server/tests/unit/realtime/monitoring/test_health_monitor.py) line ~737**File 5:** [`server/tests/unit/middleware/test_security_middleware.py`](server/tests/unit/middleware/test_security_middleware.py) line ~539**For each file:** Read the context around `assert True`, understand what the test is actually verifying, and either:

1. Remove the `assert True` if the test passes by not raising exceptions
2. Add a meaningful assertion about actual state/output

---

## Phase 3: Add Test Markers for Categorization

### Task 3.1: Define Test Markers in Configuration

**Goal:** Add custom pytest markers to enable selective test execution.**File to modify:** [`pyproject.toml`](pyproject.toml) or [`pytest.ini`](pytest.ini)**Add this configuration:**

```ini
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests that require database or external services",
    "security: marks security-focused tests",
    "e2e: marks end-to-end tests",
    "performance: marks performance benchmark tests",
]
```

### Task 3.2: Apply Markers to Existing Tests

**Goal:** Categorize tests with appropriate markers.**Tests to mark as `@pytest.mark.slow`:**

- Any test with `time.sleep()` or `asyncio.sleep()` > 1 second
- Tests in [`server/tests/performance/`](server/tests/performance/) directory

**Example:**

```python
@pytest.mark.slow
@pytest.mark.asyncio
async def test_websocket_load(self):
    ...
```

**Tests to mark as `@pytest.mark.integration`:**

- All tests in [`server/tests/integration/`](server/tests/integration/) directory

**Add at file level or class level:**

```python
import pytest

pytestmark = pytest.mark.integration  # Marks all tests in this file
```

**Tests to mark as `@pytest.mark.security`:**

- All tests in [`server/tests/security/`](server/tests/security/) directory

---

## Phase 4: Reorganize Tests

### Task 4.1: Move Misplaced Tests from Fixtures Directory

**Goal:** Move test files from fixtures/ to proper test directories.**File to move:** [`server/tests/fixtures/test_error_logging.py`](server/tests/fixtures/test_error_logging.py)**Steps:**

1. Read the file to understand what it tests

2. Move to [`server/tests/unit/utils/test_error_logging_fixtures.py`](server/tests/unit/utils/) (or merge with existing test file)

3. Update any imports if necessary

4. Run tests to verify nothing broke:

```powershell
uv run pytest server/tests/unit/utils/ -v 2>&1 | Select-Object -Last 20
```

---

## Phase 5: Add Parametrized Tests (Optional Enhancement)

### Task 5.1: Identify Candidates for Parametrization

**Goal:** Consolidate repetitive tests using `@pytest.mark.parametrize`.**Example pattern to look for:**

```python
def test_validation_case_1(self):
    with pytest.raises(ValidationError):
        Model(field="invalid1")

def test_validation_case_2(self):
    with pytest.raises(ValidationError):
        Model(field="invalid2")
```

**Refactored version:**

```python
@pytest.mark.parametrize("invalid_value", ["invalid1", "invalid2", "invalid3"])
def test_validation_rejects_invalid(self, invalid_value):
    with pytest.raises(ValidationError):
        Model(field=invalid_value)
```

**Files likely to benefit:**

- [`server/tests/unit/config/test_feature_flags.py`](server/tests/unit/config/test_feature_flags.py) - Many similar validation tests
- [`server/tests/unit/infrastructure/test_config.py`](server/tests/unit/infrastructure/test_config.py) - Port/URL validation tests

---

## Verification Commands

After completing each phase, run these commands to verify:**Phase 1 verification (worker stability):**

```powershell
cd E:\projects\GitHub\MythosMUD
uv run pytest server/tests/unit/config/ server/tests/unit/events/ -v -n 4 2>&1 | Select-Object -Last 40
```

Expected: All tests pass, no worker crashes**Phase 2 verification (weak tests removed):**

```powershell
uv run pytest server/tests/coverage/test_error_logging_coverage.py -v 2>&1
```

Expected: Fewer tests, all meaningful**Phase 3 verification (markers work):**

```powershell
uv run pytest server/tests/ -m "not slow" --collect-only 2>&1 | Select-Object -Last 20
```

Expected: Slow tests excluded from collection**Full suite verification:**

```powershell
make test


























```
