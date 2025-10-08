# Environment Configuration Refactoring

## Overview

MythosMUD has been refactored to use a **two-tier configuration architecture** that properly separates secrets from structural configuration.

## The Problem

Previously, `.env` files contained a mix of:
- ❌ Secrets (passwords, API keys) - Should NEVER be committed
- ❌ Structural config (rate limits, feature flags) - SHOULD be committed
- ❌ This mixing made it unclear what should/shouldn't be in git
- ❌ Configuration drift between environments was hard to track

## The Solution

**Two-Tier Architecture**:

1. **YAML Config Files** (`server/server_config.*.yaml`) - Structural configuration
   - Committed to git
   - Defines HOW the server behaves
   - Examples: rate limits, timeouts, feature flags, logging format

2. **`.env` Files** - Secrets only
   - NEVER committed (in `.gitignore`)
   - Contains ONLY sensitive data
   - Examples: passwords, API keys, database credentials

## Configuration Files by Environment

### Local Development

| File                              | Purpose            | Committed? | Contains                        |
| --------------------------------- | ------------------ | ---------- | ------------------------------- |
| `server/server_config.local.yaml` | Local dev behavior | ✅ Yes      | Rate limits, features, timeouts |
| `.env.local`                      | Local dev secrets  | ❌ No       | Admin password, secret keys     |
| `env.local.example`               | Template           | ✅ Yes      | Shows what secrets are needed   |

### Unit Testing (pytest)

| File                                  | Purpose       | Committed? | Contains                                  |
| ------------------------------------- | ------------- | ---------- | ----------------------------------------- |
| `server/server_config.unit_test.yaml` | Test behavior | ✅ Yes      | Test-specific settings, disabled features |
| `server/tests/.env.unit_test`         | Test secrets  | ❌ No       | Test database URLs, test secrets          |
| `server/tests/env.unit_test.example`  | Template      | ✅ Yes      | Shows what test secrets are needed        |

### E2E Testing (Playwright)

| File                                 | Purpose           | Committed? | Contains                                   |
| ------------------------------------ | ----------------- | ---------- | ------------------------------------------ |
| `server/server_config.e2e_test.yaml` | E2E test behavior | ✅ Yes      | E2E-specific settings, test database paths |
| (none needed)                        | E2E secrets       | -          | Uses same test secrets as unit tests       |

### Production

| File                        | Purpose             | Committed? | Contains                                 |
| --------------------------- | ------------------- | ---------- | ---------------------------------------- |
| `server/server_config.yaml` | Production behavior | ✅ Yes      | Production settings                      |
| `.env.production`           | Production secrets  | ❌ No       | REAL passwords, API keys                 |
| `env.production.example`    | Template            | ✅ Yes      | Shows what production secrets are needed |

## Migration Guide

### For Developers

**Old Way**:
```bash
cp env.development.example .env.local
# Edit all 142 lines (mostly non-secrets!)
```

**New Way**:
```bash
cp env.local.example .env.local
# Edit only ~11 lines (actual secrets only!)
```

The structural configuration is already in `server/server_config.local.yaml` (committed to git).

### For CI/CD

**Old Way**:
```yaml
- name: Set up test environment
  run: |
    echo "DATABASE_URL=..." >> .env.test
    echo "DEBUG=true" >> .env.test
    echo "LOG_LEVEL=DEBUG" >> .env.test
    # ... 30+ more lines
```

**New Way**:
```yaml
- name: Set up test secrets
  run: |
    echo "DATABASE_URL=..." >> server/tests/.env.unit_test
    echo "MYTHOSMUD_SECRET_KEY=test" >> server/tests/.env.unit_test
    # Only ~7 lines (secrets only!)
```

Structural config is already in `server/server_config.unit_test.yaml` (in git).

## Key Principles

### What Goes in YAML Config (Committed)

✅ Behavioral settings (how things work)
✅ Limits and thresholds (rate limits, timeouts, pool sizes)
✅ Feature toggles (enable_combat, enable_weather)
✅ Non-sensitive paths (data directories, log locations)
✅ CORS allowed origins (not secrets)
✅ Logging configuration (format, level, rotation)

### What Goes in .env (Never Committed)

✅ Passwords and secrets
✅ API keys and tokens
✅ SMTP credentials
✅ Database connection strings with credentials
✅ SSL certificate paths (if they contain sensitive data)

## Configuration Loading Order

1. **Load YAML config** (`server/server_config.*.yaml`)
   - Via `MYTHOSMUD_CONFIG_PATH` environment variable
   - Falls back to `server/server_config.yaml` if not set

2. **Load .env secrets** (`.env.local`, `.env.unit_test`, etc.)
   - Via `python-dotenv` in conftest.py or startup scripts
   - Secrets **override** YAML values where applicable

3. **Apply hardcoded defaults** (in `config_loader.py`)
   - Used only if neither YAML nor .env provides a value

## Files Created in This Refactoring

### New Config Files
- ✅ `server/server_config.local.yaml` - Local development structural config
- ✅ `server/server_config.unit_test.yaml` - Unit test structural config
- ✅ `server/server_config.e2e_test.yaml` - E2E test structural config

### New Secret Templates
- ✅ `env.local.example` - Local dev secrets template
- ✅ `server/tests/env.unit_test.example` - Unit test secrets template

### Updated Files
- ✅ `server/tests/conftest.py` - Now loads `.env.unit_test` instead of `.env.test`
- ✅ `.gitignore` - Updated to ignore new `.env.unit_test` file
- ✅ `scripts/start_e2e_test.ps1` - Uses `server_config.e2e_test.yaml`

### Documentation
- ✅ `.ENV_REFACTORING_SUMMARY.md` - Summary of local dev refactoring
- ✅ `server/tests/TEST_ENVIRONMENT_CONFIG.md` - Updated test environment guide
- ✅ `docs/ENVIRONMENT_CONFIGURATION_REFACTORING.md` - This file

## Next Steps

### For Local Development
1. Create `.env.local` from `env.local.example`
2. Fill in your actual secrets
3. Start server normally - it will use `server_config.local.yaml` + `.env.local`

### For Unit Testing
1. Create `server/tests/.env.unit_test` from `server/tests/env.unit_test.example`
2. Defaults work fine - no editing needed
3. Run `make test-server` - uses `server_config.unit_test.yaml` + `.env.unit_test`

### For E2E Testing
1. Run `./scripts/start_e2e_test.ps1` - uses `server_config.e2e_test.yaml`
2. Run `npm run test:e2e:runtime` in client directory
3. Uses test database: `data/unit_test/players/unit_test_players.db`

## Benefits

1. **Security**: Clear separation prevents accidentally committing secrets
2. **Clarity**: Obvious what belongs in git vs what doesn't
3. **Consistency**: Same pattern across all environments
4. **Reviewability**: Config changes are reviewable in git
5. **Maintainability**: Easier to manage structural configuration
6. **Documentation**: Configuration files self-document expected behavior
