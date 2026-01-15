# Session Sharing Implementation

## Overview

Implemented Playwright's `storageState` feature to share authentication sessions across tests, dramatically reducing test execution time.

## Key Changes

### 1. Session Sharing with `storageState`

**Before**: Each test logged in separately (75+ logins for full suite)
**After**: Login happens once, session is saved and reused across all tests

**Implementation**:

- Created `setupAuthStorage()` function that logs in once and saves the browser context's storage state (cookies, localStorage, sessionStorage)
- Modified `authenticatedTest` and `adminTest` fixtures to:
  1. Create a temporary context for authentication
  2. Login and save storage state to `.auth/user-auth.json` or `.auth/admin-auth.json`
  3. Create a new context with the saved storage state
  4. All subsequent tests use this authenticated context

**Benefits**:

- Login happens once per test worker instead of once per test
- Session is persisted across test runs (valid for 1 hour)
- Tests start immediately with authenticated state

### 2. Login Function Optimizations

**Removed**:

- All `waitForLoadState('networkidle')` calls - these wait for 500ms of no network activity, which is extremely slow with WebSockets and background requests
- Redundant `waitForFunction` calls
- Excessive timeout values

**Optimized**:

- Changed `waitUntil: 'networkidle'` to `'load'` for faster page loads
- Reduced all timeout values:
  - Login form wait: 10s → 5s
  - Character selection wait: 10s → 5s
  - MOTD handling: Multiple 10s waits → Single 5s wait
  - Command input verification: 15s → 5s
- Simplified MOTD handling: Try Enter key first (fastest), then button clicks
- Removed redundant intermediate waits

**Target**: ~30 seconds per login (matching manual login time)

### 3. File Structure

```
client/tests/e2e/
├── .auth/                    # Authentication storage state (gitignored)
│   ├── user-auth.json       # Regular user session
│   └── admin-auth.json      # Admin user session
└── di-migration-validation.spec.ts
```

## Performance Impact

### Before

- **Login time per test**: 3-4 minutes
- **Total login time for 75 tests**: ~225-300 minutes (3.75-5 hours)
- **Total suite time**: 4+ hours

### After (Expected)

- **Login time per worker**: ~30 seconds (once)
- **Subsequent tests**: Start immediately with authenticated state
- **Total suite time**: ~30-60 minutes (estimated 85-90% reduction)

## Usage

The fixtures work automatically - no changes needed to individual tests:

```typescript
authenticatedTest('My Test', async ({ page }) => {
  // Page is already logged in and ready to use
  await executeCommand(page, 'look');
});
```

## Storage State Management

- **Location**: `client/tests/e2e/.auth/`
- **Lifetime**: Storage state is valid for 1 hour (can be adjusted in `setupAuthStorage`)
- **Refresh**: Storage state is automatically recreated if:
  - It doesn't exist
  - It's older than 1 hour
  - Authentication verification fails

## Security Notes

- Storage state files contain session cookies and should never be committed to version control
- Added `.auth/` directory to `.gitignore`
- Storage state is local to the test environment only

## Troubleshooting

If tests fail with authentication errors:

1. Delete `.auth/` directory to force fresh login
2. Check that server is running and accessible
3. Verify login credentials are correct
4. Check server logs for authentication issues

## Next Steps

1. Monitor test execution time to verify performance improvements
2. Consider reducing storage state lifetime if sessions expire quickly
3. Add storage state cleanup in CI/CD pipelines
4. Consider parallel test execution now that login is fast
