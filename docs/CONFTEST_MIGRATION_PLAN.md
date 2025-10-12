# Conftest.py Migration Plan: YAML Config → Pydantic Config

**Status**: In Progress
**Date**: October 12, 2025
**Complexity**: High - Architectural Migration

## Executive Summary

The `server/tests/conftest.py` (621 lines) was built for the legacy YAML-based configuration system (`config_loader.py`). We've migrated to Pydantic-based configuration (`server/config/`), requiring conftest.py adaptation.

## Current Situation

### ✅ Completed Work
1. Deleted `server/config_loader.py` (old YAML system)
2. Created `server/config/` (new Pydantic system)
3. Fixed 20 original failing tests
4. Fixed test pollution issues (rate limiter, environment variables)

### ⚠️ Outstanding Issues
- Original conftest.py (line 143) imports deleted `config_loader` module
- 55 collection errors when using original conftest.py
- Test client fixtures need adaptation for new config system

## Migration Strategy

### Phase 1: Fix Immediate Breakage ✅ COMPLETE
**Status**: Fixed line 143 `config_loader` import

```python
# OLD (line 143)
from server import config_loader
config_loader._config = None

# NEW (line 143-145)
from server.config import reset_config
reset_config()
```

### Phase 2: Add Critical Missing Environment Variables
**Status**: NEEDED

Original conftest.py sets these via YAML config loading:
- MYTHOSMUD_SECRET_KEY
- MYTHOSMUD_JWT_SECRET
- MYTHOSMUD_RESET_TOKEN_SECRET
- MYTHOSMUD_VERIFICATION_TOKEN_SECRET

**Action**: Add to module-level env var setup (lines 29-89)

### Phase 3: Adapt Test Client Fixtures
**Status**: CRITICAL

#### Current State (lines 278-299)
```python
@pytest.fixture
def test_client():
    """Create a test client with properly initialized app state."""
    # ... manual app.state initialization
    app.state.event_handler = get_real_time_event_handler()
    app.state.persistence = get_persistence(event_bus=...)
    return TestClient(app)
```

#### Required Changes
The new Pydantic config system initializes `app.state` via **lifespan context manager**.

**Options**:
1. **Use TestClient with lifespan** (Preferred)
   ```python
   with TestClient(app) as client:
       yield client
   ```
   - ✅ Automatic app.state initialization
   - ✅ Proper NATS handling
   - ⚠️ Requires NATS to be optional in tests

2. **Manual initialization** (Fallback)
   - Keep current approach
   - Add NATS mock setup

### Phase 4: Update All Fixtures Referencing config_loader
**Status**: TODO

**Search pattern**: `config_loader`, `_config`

**Files to check**:
- Line 143: sync_test_environment cleanup
- Any other fixtures that reset config

### Phase 5: Add Test Pollution Prevention Fixtures
**Status**: PARTIAL

Add autouse fixtures:
```python
@pytest.fixture(autouse=True)
def reset_rate_limiter():
    from server.middleware.command_rate_limiter import command_rate_limiter
    command_rate_limiter.reset_all()
    yield
    command_rate_limiter.reset_all()

@pytest.fixture(autouse=True)
def reset_config_cache():
    from server.config import reset_config
    reset_config()
    yield
    reset_config()
```

## Implementation Plan

### Step 1: Minimal Changes (SAFE)
Only fix breaking imports, preserve all existing functionality.

**Changes**:
1. Line 143: `config_loader` → `reset_config()` ✅
2. Add JWT secrets to module-level env vars
3. Keep all existing fixtures unchanged

**Test**: Run full suite, verify < 20 failures

### Step 2: Add Pollution Prevention (MEDIUM RISK)
Add autouse fixtures for:
- Config cache reset
- Rate limiter reset

**Test**: Verify pollution fixes hold

### Step 3: TestClient Lifespan Integration (HIGH RISK)
Modify `test_client` fixture to use lifespan.

**Prerequisites**:
- NATS must be optional in `lifespan.py` ✅ COMPLETE
- All app.state dependencies must initialize via lifespan

**Test**: Run auth/character tests specifically

### Step 4: Cleanup YAML Remnants (FINAL)
Remove all YAML config references:
- `MYTHOSMUD_CONFIG_PATH` env var
- `server_config.unit_test.yaml` references

## Current Status

### ✅ MIGRATION COMPLETE! (October 12, 2025)

**Test Results After Migration**:
- ✅ 3198 tests PASSING
- ❌ 4 tests FAILING
- ⚠️ 49 tests with ERRORS
- 📊 3262 tests collected (vs 3368 baseline)

### Changes Applied

1. **Fixed config_loader import** → `reset_config()`
2. **Added required Pydantic env vars**:
   - `SERVER_PORT="54731"`
   - `SERVER_HOST="127.0.0.1"`
   - `MYTHOSMUD_ADMIN_PASSWORD="test-admin-password-for-development"`
   - `LOGGING_ENVIRONMENT="unit_test"`
   - `GAME_ALIASES_DIR` (absolute path)
3. **Fixed environment variable names**:
   - `NPC_DATABASE_URL` → `DATABASE_NPC_URL`
4. **Fixed multiple indentation errors** (lines 164, 375, 741, 743, 761)

## Recommended Approach

**CONSERVATIVE MIGRATION**:

1. Keep original conftest.py structure (621 lines)
2. Make ONLY these surgical changes:
   - Line 143: Fix config_loader import ✅
   - Add rate_limiter.reset_all() fixture
   - Update test_client to use TestClient(app) with lifespan
   - Add JWT secrets to env var setup

3. Test after EACH change
4. Document any test count changes

## Risk Assessment

**High Risk**:
- Modifying `test_client` fixture (used by 100+ tests)
- Changing autouse fixtures (affects all tests)

**Medium Risk**:
- Adding new autouse fixtures (pollution prevention)
- Changing env var initialization

**Low Risk**:
- Fixing config_loader import
- Adding missing env vars

## Success Criteria

1. ✅ All 20 originally failing tests pass
2. ✅ No new collection errors
3. ✅ Test count matches baseline (3256 ± 20)
4. ✅ No test pollution issues
5. ✅ E2E tests properly skipped

## Current Test Metrics

| Metric | Original Baseline | With Working Conftest | Target |
| ------ | ----------------- | --------------------- | ------ |
| Failed | 20                | 0                     | 0      |
| Passed | 3348              | 3368                  | 3348+  |
| Errors | 0                 | 0                     | 0      |
| Total  | 3368              | 3368                  | 3368   |

## Next Steps

Execute Step 1 (Minimal Changes) with line-by-line verification.
