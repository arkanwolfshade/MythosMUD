# Warning Remediation Plan
## MythosMUD Test Suite Warning Elimination

*As documented by the Department of Occult Studies, Miskatonic University*

---

## Executive Summary

**Original Warning Count:** 4,221 warnings
**After datetime.utcnow() Fix:** ~200 warnings (estimated)
**Warnings Eliminated:** ~4,000 (95%)
**Remaining Categories:** 3 major types

---

## Phase 1: datetime.utcnow() Deprecation ✅ COMPLETED

### Status: RESOLVED
**Impact:** Eliminated ~4,000 warnings (95% of total)

### Changes Made
Fixed all 29 instances across 11 files:

#### Production Code (4 files)
1. ✅ `server/logging/combat_audit.py` - 8 instances
2. ✅ `server/services/player_combat_service.py` - 3 instances
3. ✅ `server/services/combat_service.py` - 1 instance

#### Test Code (7 files)
4. ✅ `server/tests/test_combat_system.py` - 4 instances
5. ✅ `server/tests/test_player_combat_integration.py` - 1 instance
6. ✅ `server/tests/unit/services/test_player_combat_service.py` - 1 instance
7. ✅ `server/tests/unit/services/test_combat_service.py` - 2 instances
8. ✅ `server/tests/unit/test_combat_auto_progression_system.py` - 3 instances
9. ✅ `server/tests/unit/test_npc_passive_behavior_system.py` - 2 instances
10. ✅ `server/tests/unit/test_health_tracking_system.py` - 2 instances
11. ✅ `server/tests/unit/test_auto_progression_integration.py` - 2 instances

### Solution Applied
```python
# OLD (Deprecated)
from datetime import datetime
timestamp = datetime.utcnow()

# NEW (Python 3.12+ Compatible)
from datetime import UTC, datetime
timestamp = datetime.now(UTC)
```

---

## Phase 2: HTTP Status Code Deprecation ⚠️ IN PROGRESS

### Status: IDENTIFIED - AWAITING FIX
**Estimated Impact:** ~1 warning per test file using FastAPI responses

### Warning Details
```
DeprecationWarning: 'HTTP_422_UNPROCESSABLE_ENTITY' is deprecated.
Use 'HTTP_422_UNPROCESSABLE_CONTENT' instead.
```

### Affected Files
- `server/error_handlers/standardized_responses.py:49`
- Potentially other FastAPI endpoint handlers

### Recommended Fix
```python
# OLD (Deprecated)
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

# NEW (Current)
from starlette.status import HTTP_422_UNPROCESSABLE_CONTENT
```

### Implementation Steps
1. Search for all instances of `HTTP_422_UNPROCESSABLE_ENTITY`
2. Replace with `HTTP_422_UNPROCESSABLE_CONTENT`
3. Update any related error messages or documentation
4. Run tests to verify error handling still works correctly

### Priority: MEDIUM
**Reason:** FastAPI deprecation but not affecting functionality yet

---

## Phase 3: RuntimeWarning - Unawaited Coroutines ⚠️ MODERATE PRIORITY

### Status: IDENTIFIED - REQUIRES INVESTIGATION
**Estimated Impact:** ~100-150 warnings

### Warning Details
```
RuntimeWarning: coroutine 'countdown_loop' was never awaited
RuntimeWarning: coroutine '_execute_mock_call' was never awaited
RuntimeWarning: coroutine '_check_and_process_disconnect' was never awaited
```

### Affected Areas

#### 1. Test Mocking Issues
**Files:**
- `tests/unit/commands/test_shutdown_countdown.py`
- `tests/unit/commands/test_shutdown_graceful_sequence.py`
- `tests/performance/test_combat_performance.py`
- Various other test files

**Cause:** Mock objects not properly awaited in async tests

**Solution:**
```python
# WRONG
mock_function.return_value = some_value
result = await function_under_test()

# RIGHT
mock_function.return_value = AsyncMock(return_value=some_value)
# OR use pytest-asyncio's async mocks
```

#### 2. Background Task Management
**Files:**
- `server/app/memory_cleanup_service.py:93`
- `server/commands/admin_shutdown_command.py:320`

**Cause:** Background tasks created but not properly managed

**Solution:**
- Use `asyncio.create_task()` and store task references
- Implement proper task cancellation in cleanup
- Add task tracking to service lifecycle management

#### 3. SQLAlchemy/Database Operations
**Files:**
- Various database test files
- `server/infrastructure/test_database.py`

**Cause:** Async database operations in synchronous context

**Solution:**
- Ensure all database operations use proper async/await
- Review connection manager lifecycle
- Add proper cleanup in test fixtures

### Implementation Steps
1. **Audit Phase (Week 1)**
   - Categorize all unawaited coroutine warnings
   - Identify test vs. production code issues
   - Prioritize by risk and frequency

2. **Fix Phase (Week 2-3)**
   - Fix production code issues first (highest priority)
   - Update test mocking patterns
   - Add proper async test fixtures

3. **Validation Phase (Week 4)**
   - Run full test suite with warnings enabled
   - Verify no functionality regressions
   - Document new async patterns for team

### Priority: HIGH
**Reason:** Can indicate actual bugs in async code handling

---

## Phase 4: ResourceWarning - Unclosed Event Loops 🔴 HIGH PRIORITY

### Status: IDENTIFIED - REQUIRES IMMEDIATE ATTENTION
**Estimated Impact:** ~50-70 warnings

### Warning Details
```
ResourceWarning: unclosed event loop <ProactorEventLoop running=False closed=False debug=False>
```

### Affected Areas
- `tests/unit/infrastructure/test_connection_manager.py`
- Various async test files
- Integration tests with WebSocket connections

### Root Causes

#### 1. Test Fixture Issues
**Problem:** Event loops created in test setup but not properly closed

**Solution:**
```python
# In conftest.py or test fixtures
@pytest.fixture
async def event_loop():
    """Create an event loop for the test."""
    loop = asyncio.new_event_loop()
    yield loop
    # Properly close the loop
    loop.close()
```

#### 2. WebSocket Connection Leaks
**Problem:** WebSocket connections not properly closed in tests

**Solution:**
```python
# Add explicit cleanup
async def test_websocket_connection():
    ws = await connect_websocket()
    try:
        # Test code
        pass
    finally:
        await ws.close()
```

#### 3. Async Context Manager Issues
**Problem:** Resources not properly cleaned up

**Solution:**
- Use `async with` for all resource management
- Implement proper `__aenter__` and `__aexit__` methods
- Add explicit cleanup in test teardown

### Implementation Steps
1. **Immediate Actions**
   - Add event loop cleanup to all async test fixtures
   - Review all WebSocket test patterns
   - Add explicit connection cleanup

2. **Systematic Fix (Week 1)**
   - Audit all async resource usage
   - Add context managers where missing
   - Implement proper cleanup in all test fixtures

3. **Prevention (Week 2)**
   - Add pre-commit hook to check for resource leaks
   - Create test fixture templates
   - Document async resource management patterns

### Priority: CRITICAL
**Reason:** Resource leaks can cause memory issues in production

---

## Phase 5: Verification and Monitoring 📊

### Post-Fix Validation Process

#### 1. Run Complete Test Suite
```bash
make test-comprehensive
```
**Target:** < 50 warnings remaining

#### 2. Run Specific Test Categories
```bash
# Unit tests
uv run pytest server/tests/unit -v -W default

# Integration tests
uv run pytest server/tests/integration -v -W default

# Performance tests
uv run pytest server/tests/performance -v -W default
```

#### 3. Enable Warning Reporting
Temporarily modify `scripts/test_runner.py`:
```python
# Line 157 - Comment out for verification runs
# "--disable-warnings",  # Temporarily enabled for warning audit
```

#### 4. Continuous Monitoring
- Add CI/CD check for warning count
- Set threshold: Fail if warnings > 50
- Monthly review of new warnings

---

## Implementation Timeline

### Week 1: Critical Issues
- ✅ **Day 1-2:** datetime.utcnow() fixes (COMPLETED)
- 🔴 **Day 3-4:** ResourceWarning - Event loop cleanup
- 🟡 **Day 5:** HTTP status code deprecation

### Week 2-3: RuntimeWarnings
- 🟠 **Days 1-5:** Unawaited coroutine fixes in production code
- 🟠 **Days 6-10:** Test mocking pattern updates
- 🟠 **Days 11-15:** Background task management

### Week 4: Validation and Documentation
- 📊 **Days 1-3:** Full test suite validation
- 📝 **Days 4-5:** Update documentation and team training

---

## Success Metrics

### Target Goals
| Metric | Baseline | Target | Achieved |
|--------|----------|--------|----------|
| Total Warnings | 4,221 | < 50 | TBD |
| datetime.utcnow() | ~4,000 | 0 | ✅ 0 |
| HTTP Deprecation | ~1 | 0 | ⏳ Pending |
| RuntimeWarning | ~150 | < 30 | ⏳ Pending |
| ResourceWarning | ~70 | 0 | ⏳ Pending |

### Quality Gates
- ✅ All tests must pass after fixes
- ✅ No functionality regressions
- ✅ Code coverage maintained at 80%+
- ✅ Performance benchmarks unchanged

---

## Appendix A: Quick Reference Commands

### Find Remaining Warnings
```bash
# Run tests with warnings visible
cd server
uv run pytest -v -o addopts="" 2>&1 | grep -i "warning"

# Count warnings by type
cd server
uv run pytest -v -o addopts="" 2>&1 | grep "Warning:" | sort | uniq -c
```

### Test Specific Files
```bash
# Test a single file with warnings
cd server
uv run pytest tests/path/to/test_file.py -v -o addopts=""
```

### Verify Fixes
```bash
# Run full suite and check warning count
make test-comprehensive 2>&1 | grep "warnings in"
```

---

## Appendix B: Common Patterns and Solutions

### Pattern 1: Async Test Fixtures
```python
import pytest
import asyncio

@pytest.fixture
async def async_resource():
    """Async fixture with proper cleanup."""
    resource = await create_resource()
    yield resource
    await resource.cleanup()

@pytest.fixture(scope="function")
def event_loop():
    """Ensure event loop is properly closed."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()
```

### Pattern 2: Mock Async Functions
```python
from unittest.mock import AsyncMock

# Correct async mocking
async def test_async_function():
    mock_service = AsyncMock()
    mock_service.fetch_data.return_value = {"data": "test"}

    result = await mock_service.fetch_data()
    assert result == {"data": "test"}
```

### Pattern 3: Context Manager for Resources
```python
class ManagedResource:
    async def __aenter__(self):
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cleanup()

# Usage
async with ManagedResource() as resource:
    await resource.use()
```

---

*"In eliminating these warnings, we maintain the integrity of our research into the forbidden territories of asynchronous programming."*

**— Department of Occult Studies, Miskatonic University**

Last Updated: 2025-10-28
Status: Phase 1 Complete, Phases 2-5 In Progress
