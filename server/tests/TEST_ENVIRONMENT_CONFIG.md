# Test Environment Configuration

This document describes the configuration approach for running the MythosMUD test suite.

## Configuration Architecture

MythosMUD uses a **two-tier configuration system** for tests:

1. **`server/server_config.unit_test.yaml`** - Structural configuration (committed to git)
2. **`server/tests/.env.unit_test`** - Secrets only (never committed)

This separation ensures:
- ✅ Behavioral settings are version-controlled and consistent
- ✅ Secrets are isolated and never accidentally committed
- ✅ Clear distinction between "how it works" vs "credentials"

## Structural Configuration (YAML)

**File**: `server/server_config.unit_test.yaml`

Contains all **non-secret** test configuration:
- Database paths (no credentials)
- Logging levels and formats
- Feature flags (enable_test_data, enable_debug_endpoints, etc.)
- Rate limits and timeouts
- NATS configuration
- Chat system settings
- Performance tuning
- Game mechanics

**This file IS committed to git** - it defines how the test server behaves.

## Secrets Configuration (.env)

**File**: `server/tests/.env.unit_test`

Contains **ONLY secrets**:

```env
# --- Database URLs (Test Databases) ---
DATABASE_URL=sqlite+aiosqlite:///data/unit_test/players/unit_test_players.db
NPC_DATABASE_URL=sqlite+aiosqlite:///data/unit_test/npcs/unit_test_npcs.db

# --- Security Secrets (Test Values Only - Not Real Secrets) ---
MYTHOSMUD_SECRET_KEY=test-secret-key-for-testing-only
MYTHOSMUD_JWT_SECRET=test-jwt-secret-for-testing-only
MYTHOSMUD_RESET_TOKEN_SECRET=test-reset-token-secret-for-testing-only
MYTHOSMUD_VERIFICATION_TOKEN_SECRET=test-verification-token-secret-for-testing-only
MYTHOSMUD_ADMIN_PASSWORD=test-admin-password
```

**This file is NOT committed to git** - it contains secrets (even if they're test secrets).

## Setting Up Test Environment

### Step 1: Create Secrets File

```bash
# Copy the example to create your local test secrets file
cp server/tests/env.unit_test.example server/tests/.env.unit_test

# No need to edit - the defaults work for testing
```

### Step 2: Run Tests

```bash
# From project root
make test-server

# Or directly with pytest
cd server
pytest
```

The test suite automatically:
1. Loads secrets from `server/tests/.env.unit_test` (via conftest.py)
2. Loads structural config from `server/server_config.unit_test.yaml` (via config_loader.py)
3. Creates test databases if they don't exist
4. Sets up proper directory structure

## What Changed (Migration from Old Approach)

### Old Approach ❌
- **`.env.unit_test`** (in project root) - Had EVERYTHING mixed together
- **`server/tests/test.env.example`** - Example file
- **`server/tests/test_server_config.yaml`** - Test config

### New Approach ✅
- **`server/server_config.unit_test.yaml`** - Structural configuration (committed)
- **`server/tests/.env.unit_test`** - Secrets only (not committed)
- **`server/tests/env.unit_test.example`** - Template for secrets

### Benefits
- ✅ Clear separation of secrets vs configuration
- ✅ Easier to review configuration changes in git
- ✅ Reduced risk of committing secrets
- ✅ Consistent with production/local/e2e test patterns

## Database Paths

- **Player Database**: `data/unit_test/players/unit_test_players.db`
- **NPC Database**: `data/unit_test/npcs/unit_test_npcs.db`
- **Aliases Directory**: `data/unit_test/players/aliases`

These are automatically created and managed by the test suite.

## Configuration Priority

1. **`.env.unit_test` secrets** (highest priority - overrides everything)
2. **`server_config.unit_test.yaml`** structural config
3. **Hardcoded defaults** in `conftest.py` (fallback)

## Security Note

**NEVER** use production security keys in test configurations. Always use test-specific values that are clearly marked as such.

The test values in `env.unit_test.example` are safe for testing but should still not be committed when you create your local `.env.unit_test` file.
