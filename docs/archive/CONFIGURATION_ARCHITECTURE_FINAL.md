# Configuration Architecture - Final Design ✅

## Complete Configuration Tuples

MythosMUD uses **paired configuration files** for each environment - a clean separation between structure and secrets:

### Tuple 1: Local Development 🖥️

```
server/server_config.local.yaml  ← Structural config (committed)
.env.local                       ← Secrets (NOT committed)
env.local.example                ← Template (committed)
```

**Startup**: `.\scripts\start_local.ps1`

### Tuple 2: Unit Testing 🧪

```
server/server_config.unit_test.yaml  ← Structural config (committed)
server/tests/.env.unit_test          ← Secrets (NOT committed)
server/tests/env.unit_test.example   ← Template (committed)
```

**Startup**: Automatic via `conftest.py` when running `make test`

### Tuple 3: E2E Testing 🎭

```
server/server_config.e2e_test.yaml  ← Structural config (committed)
.env.e2e_test                       ← Secrets (NOT committed)
env.e2e_test.example                ← Template (committed)
```

**Startup**: `.\scripts\start_e2e_test.ps1`

### Tuple 4: Production 🚀 (Future)

```
server/server_config.production.yaml  ← Structural config (committed when created)
.env.production                       ← Secrets (NEVER committed)
env.production.example                ← Template (committed)
```

**Startup**: `.\scripts\start_server.ps1 -Environment production`

## Architecture Principles

### 1. Explicit Configuration (No Fallbacks)

❌ **Deleted**: `server/server_config.yaml` (dangerous default)

✅ **Required**: `MYTHOSMUD_CONFIG_PATH` must be set

✅ **Fail-Fast**: Fatal error if configuration missing

### 2. Secrets Separation

**YAML files** (committed): Structure, limits, behavior, toggles

**.env files** (NOT committed): Passwords, keys, credentials

### 3. Symmetrical Design

Every environment follows the same pattern:

```
server_config.<env>.yaml + .env.<env> + env.<env>.example
```

## Files Created/Modified

### New Configuration Files (Committed)

✅ `server/server_config.local.yaml`

✅ `server/server_config.unit_test.yaml`

✅ `server/server_config.e2e_test.yaml`

### New Secret Templates (Committed)

✅ `env.local.example`

✅ `server/tests/env.unit_test.example`

✅ `env.e2e_test.example`

### Deleted Files

❌ `server/server_config.yaml` (dangerous fallback)

❌ `scripts/start_dev.ps1` (redundant with start_local.ps1)

### Updated Files

✅ `server/config_loader.py` - Requires explicit configuration

✅ `scripts/start_server.ps1` - Environment-based config selection

✅ `scripts/start_local.ps1` - Uses local config

- ✅ `scripts/start_e2e_test.ps1` - Uses E2E test config, loads .env.e2e_test
- ✅ `server/tests/conftest.py` - Uses unit test config
- ✅ `.gitignore` - Ignores all .env secret files

## Developer Setup

### One-Time Setup

```powershell
# 1. Local development secrets

cp env.local.example .env.local
notepad .env.local  # Add your MYTHOSMUD_ADMIN_PASSWORD

# 2. Unit test secrets

cp server/tests/env.unit_test.example server/tests/.env.unit_test
# No editing needed - defaults are fine

# 3. E2E test secrets

cp env.e2e_test.example .env.e2e_test
# No editing needed - defaults are fine

```

### Daily Use

```powershell
# Start local development

.\scripts\start_local.ps1

# Run unit tests

make test

# Run E2E tests

.\scripts\start_e2e_test.ps1  # Terminal 1
cd client; npm run test:e2e:runtime  # Terminal 2
```

## What Each .env File Contains

### `.env.local` (7 items)

```env
SECRET_KEY=<your-dev-secret>
MYTHOSMUD_ADMIN_PASSWORD=<your-password>
# Optional overrides

DATABASE_URL=
SENTRY_DSN=
REDIS_URL=
SLACK_WEBHOOK_URL=
EMAIL_SMTP_* credentials
SSL_* certificate paths
```

### `server/tests/.env.unit_test` (7 items)

```env
DATABASE_URL=sqlite+aiosqlite:///data/unit_test/players/unit_test_players.db
NPC_DATABASE_URL=sqlite+aiosqlite:///data/unit_test/npcs/test_npcs.db
MYTHOSMUD_SECRET_KEY=test-secret-key-for-testing-only
MYTHOSMUD_JWT_SECRET=test-jwt-secret-for-testing-only
MYTHOSMUD_RESET_TOKEN_SECRET=test-reset-token-secret
MYTHOSMUD_VERIFICATION_TOKEN_SECRET=test-verification-token-secret
MYTHOSMUD_ADMIN_PASSWORD=test-admin-password
```

### `.env.e2e_test` (5 items)

```env
MYTHOSMUD_SECRET_KEY=e2e-test-secret-key-for-playwright
MYTHOSMUD_JWT_SECRET=e2e-test-jwt-secret-for-playwright
MYTHOSMUD_RESET_TOKEN_SECRET=e2e-test-reset-token-secret
MYTHOSMUD_VERIFICATION_TOKEN_SECRET=e2e-test-verification-token-secret
MYTHOSMUD_ADMIN_PASSWORD=e2e-test-admin-password
```

## Configuration Loading Flow

```
1. Script starts (start_local.ps1, start_e2e_test.ps1, etc.)
   ↓
2. Script loads .env file (if exists)
   ↓
3. Script sets MYTHOSMUD_CONFIG_PATH environment variable
   ↓
4. Server starts and config_loader.py runs
   ↓
5. config_loader.py checks MYTHOSMUD_CONFIG_PATH
   ↓
6. If NOT set → FATAL ERROR (no fallback!)
   ↓
7. If set → Loads YAML config
   ↓
8. .env secrets override YAML values (where applicable)
   ↓
9. Server starts with explicit, known configuration
```

## Benefits of This Architecture

1. **Security** ✅

   - Secrets never committed to git
   - Clear separation prevents accidental exposure

2. **Explicitness** ✅

   - Always know which config is being used
   - No hidden fallbacks or assumptions

3. **Consistency** ✅

   - Same pattern across all environments
   - Predictable file locations

4. **Safety** ✅

   - Server won't start without proper configuration
   - Fail-fast prevents silent misconfiguration

5. **Maintainability** ✅

   - Configuration changes reviewable in git
   - Easy to see differences between environments

6. **Testability** ✅

   - Test configurations isolated from production
   - No risk of tests touching production data

## Summary

**Complete and Clean Architecture**:

- 3 configuration tuples (local, unit test, E2E test)
- 1 future tuple (production)
- No fallback configuration
- Explicit configuration required
- Secrets properly separated
- Symmetrical design across all environments

The configuration architecture is now **production-ready**! 🎉
