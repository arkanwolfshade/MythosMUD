# Configuration Files Reference

## Complete Configuration Architecture

MythosMUD uses **paired configuration files** for each environment:

### Configuration Tuples

| Environment           | Structural Config (YAML)               | Secrets (.env)                | Purpose                |
| --------------------- | -------------------------------------- | ----------------------------- | ---------------------- |
| **Local Development** | `server/server_config.local.yaml`      | `.env.local`                  | Daily development work |
| **Unit Testing**      | `server/server_config.unit_test.yaml`  | `server/tests/.env.unit_test` | pytest test runs       |
| **E2E Testing**       | `server/server_config.e2e_test.yaml`   | `.env.e2e_test`               | Playwright E2E tests   |
| **Production**        | `server/server_config.production.yaml` | `.env.production`             | Production deployment  |

### File Responsibilities

**YAML Config Files** (✅ Committed to Git):
- Behavioral settings (rate limits, timeouts, feature flags)
- Database paths (not credentials)
- Logging configuration
- NATS settings
- Chat system rules
- Game mechanics
- Feature toggles

**.env Secret Files** (❌ NEVER Committed):
- Passwords and secret keys
- API credentials
- SMTP passwords
- External service tokens
- SSL certificate paths (if sensitive)

## Setup Instructions

### 1. Local Development

```powershell
# Create secrets file
cp env.local.example .env.local

# Edit with your actual secrets (minimal - just ~7 lines)
notepad .env.local

# Start server
.\scripts\start_local.ps1
```

**Files Used**:
- ✅ `server/server_config.local.yaml` (already in git)
- ✅ `.env.local` (you create from template)

### 2. Unit Testing

```powershell
# Create secrets file
cp server/tests/env.unit_test.example server/tests/.env.unit_test

# No editing needed - defaults work!

# Run tests
make test-server
```

**Files Used**:
- ✅ `server/server_config.unit_test.yaml` (already in git)
- ✅ `server/tests/.env.unit_test` (you create from template)

### 3. E2E Testing

```powershell
# Create secrets file
cp env.e2e_test.example .env.e2e_test

# No editing needed - defaults work!

# Start E2E test server
.\scripts\start_e2e_test.ps1

# In another terminal, run E2E tests
cd client
npm run test:e2e:runtime
```

**Files Used**:
- ✅ `server/server_config.e2e_test.yaml` (already in git)
- ✅ `.env.e2e_test` (you create from template)

### 4. Production

```powershell
# Create production config from template (when needed)
cp server/server_config.local.yaml server/server_config.production.yaml
# Edit for production settings

# Create production secrets
cp env.production.example .env.production
# Add REAL production secrets (NEVER commit!)

# Deploy and start
.\scripts\start_server.ps1 -Environment production
```

**Files Used**:
- ✅ `server/server_config.production.yaml` (create when needed)
- ✅ `.env.production` (create with REAL secrets)

## Complete File Matrix

| File Name                       | Location        | Committed? | Created By | Purpose                            |
| ------------------------------- | --------------- | ---------- | ---------- | ---------------------------------- |
| `server_config.local.yaml`      | `server/`       | ✅ Yes      | Git        | Local dev behavior                 |
| `.env.local`                    | project root    | ❌ No       | Developer  | Local dev secrets                  |
| `env.local.example`             | project root    | ✅ Yes      | Git        | Template for .env.local            |
| `server_config.unit_test.yaml`  | `server/`       | ✅ Yes      | Git        | Unit test behavior                 |
| `.env.unit_test`                | `server/tests/` | ❌ No       | Developer  | Unit test secrets                  |
| `env.unit_test.example`         | `server/tests/` | ✅ Yes      | Git        | Template for .env.unit_test        |
| `server_config.e2e_test.yaml`   | `server/`       | ✅ Yes      | Git        | E2E test behavior                  |
| `.env.e2e_test`                 | project root    | ❌ No       | Developer  | E2E test secrets                   |
| `env.e2e_test.example`          | project root    | ✅ Yes      | Git        | Template for .env.e2e_test         |
| `server_config.production.yaml` | `server/`       | ✅ Yes      | Developer  | Production behavior (when created) |
| `.env.production`               | project root    | ❌ No       | DevOps     | Production secrets                 |
| `env.production.example`        | project root    | ✅ Yes      | Git        | Template for .env.production       |

## Environment Variable Priority

For each environment, configuration is loaded in this order (highest to lowest priority):

1. **.env secret file** (highest priority - overrides everything)
2. **YAML config file** (structural configuration)
3. **Hardcoded defaults** in `config_loader.py` (fallback only)

## Quick Reference

### To Start Server in Different Modes

```powershell
# Local development (default)
.\scripts\start_local.ps1

# E2E testing
.\scripts\start_e2e_test.ps1

# Explicit local
.\scripts\start_server.ps1 -Environment local

# Explicit test (E2E)
.\scripts\start_server.ps1 -Environment test

# Production (future)
.\scripts\start_server.ps1 -Environment production
```

### To Run Tests

```powershell
# Unit tests (uses server_config.unit_test.yaml + .env.unit_test)
make test-server

# E2E tests (uses server_config.e2e_test.yaml + .env.e2e_test)
.\scripts\start_e2e_test.ps1  # Terminal 1
cd client; npm run test:e2e:runtime  # Terminal 2
```

## Complete Architecture Summary

✅ **3 Complete Tuples**:
1. `server_config.local.yaml` ↔ `.env.local`
2. `server_config.unit_test.yaml` ↔ `server/tests/.env.unit_test`
3. `server_config.e2e_test.yaml` ↔ `.env.e2e_test`

✅ **3 Example Templates**:
1. `env.local.example`
2. `server/tests/env.unit_test.example`
3. `env.e2e_test.example`

✅ **Explicit Configuration**:
- Server REQUIRES `MYTHOSMUD_CONFIG_PATH` to be set
- No dangerous fallbacks
- Clear error messages if misconfigured

The architecture is now complete and consistent!
