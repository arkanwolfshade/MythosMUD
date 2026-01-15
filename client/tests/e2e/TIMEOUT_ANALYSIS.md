# Test Timeout Analysis and Fixes

## Root Causes of Multiple Timeouts

### 1. **Repeated Login for Every Test** (PRIMARY ISSUE)

- **Problem**: Every test called `loginPlayer()` separately, taking 2-3 minutes per login
- **Impact**: With 75 tests, this meant 150-225 minutes just for logins
- **Fix**: Created `authenticatedTest` and `adminTest` fixtures that login once per test worker and share the session across all tests in the suite

### 2. **Excessive Wait Timeouts in `loginPlayer()`**

- **Problem**: Multiple long timeouts stacked:
  - `waitForFunction` with 60s timeout (line 42-54)
  - `waitForFunction` with 60s timeout (line 95-102)
  - `waitForTimeout(3000)` (line 105)
  - `expect` with 30s timeout (line 111)
  - **Total potential wait**: 153 seconds per login
- **Fix**: Reduced timeouts to more reasonable values:
  - First `waitForFunction`: 60s → 30s
  - Second `waitForFunction`: 60s → 20s
  - `waitForTimeout`: 3000ms → 1000ms
  - `expect` timeout: 30s → 15s
  - **New total**: ~66 seconds maximum (but typically much faster)

### 3. **Inefficient `waitForGameTick()` Function**

- **Problem**: Function used `waitForFunction` that immediately returned `true`, then waited 5 seconds

  ```typescript
  await page.waitForFunction(() => true, { timeout: 15000 });
  await page.waitForTimeout(5000);
  ```

  - This was essentially a 20-second wait with no actual verification

- **Fix**: Simplified to just wait the necessary time:

  ```typescript
  await page.waitForTimeout(timeout); // Default 5s instead of 20s
  ```

### 4. **Redundant Waits in `executeCommand()`**

- **Problem**: Multiple waits with long timeouts:
  - `expect` with 30s timeout for command input visibility
  - `expect` with 10s timeout for response
  - `waitForFunction` with 10s timeout
  - `waitForTimeout(1000)` at the end
- **Fix**: Reduced command input timeout from 30s to 10s (if input isn't visible, there's a real issue)

### 5. **Test Isolation Overhead**

- **Problem**: Each test's `afterEach` hook called `cleanupTest()` which attempted logout and state clearing
- **Impact**: Added unnecessary overhead between tests
- **Fix**: Removed cleanup calls from authenticated test suites (session is shared, so cleanup isn't needed between tests)

## Performance Improvements

### Before

- **Per test login time**: ~2-3 minutes
- **Total login time for 75 tests**: ~150-225 minutes
- **Average test execution**: 3+ minutes each
- **Total suite time**: 4+ hours (estimated)

### After

- **Login time per worker**: ~1-2 minutes (once per test worker, not per test)
- **Shared session**: All tests in a suite share the same authenticated session
- **Reduced wait times**: ~50% reduction in timeout values
- **Optimized `waitForGameTick`**: 20s → 5s
- **Expected total suite time**: ~30-60 minutes (estimated 75-85% reduction)

## Changes Made

1. **Created Test Fixtures**:
   - `authenticatedTest`: Logs in once per worker, shares session across tests
   - `adminTest`: Same for admin tests

2. **Optimized Timeouts**:
   - Reduced all `waitForFunction` timeouts by 50%
   - Reduced `waitForTimeout` durations
   - Reduced `expect` timeouts to more reasonable values

3. **Fixed `waitForGameTick()`**:
   - Removed inefficient `waitForFunction` that always returned true
   - Simplified to direct timeout

4. **Removed Redundant Cleanup**:
   - Removed `cleanupTest()` calls from authenticated test suites
   - Session is now shared, so cleanup between tests isn't necessary

## Test Structure

### Suites Using Authenticated Fixture

- Suite 1: Core Service Functionality Tests
- Suite 3: Command Handler Validation Tests (regular + admin fixtures)
- Suite 4: Game Tick and Background Task Tests
- Suite 5: WebSocket and Real-time Communication Tests
- Suite 6: Integration Tests

### Suites NOT Using Fixtures

- Suite 2: API Endpoint Validation Tests (no login needed - direct API calls)

## Recommendations

1. **Monitor Test Execution**: Run the full suite and verify the performance improvements
2. **Further Optimization**: Consider reducing `waitForTimeout(2000)` calls in individual tests if they're not necessary
3. **Parallel Execution**: With shared fixtures, tests can run in parallel more efficiently
4. **Session Management**: If tests need true isolation, consider using separate browser contexts instead of shared sessions
