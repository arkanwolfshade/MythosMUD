# Test Environment Configuration

This document describes the environment variables required for running the MythosMUD test suite.

## Required Environment Variables

The test suite requires the following environment variables to be set:

### Database Configuration

```bash
# Main player database for tests
DATABASE_URL=sqlite+aiosqlite:///server/tests/data/players/test_players.db

# NPC database for tests
NPC_DATABASE_URL=sqlite+aiosqlite:///server/tests/data/npcs/test_npcs.db
```

### Security Configuration (Test Values)

```bash
# Security keys for testing (use test values only)
MYTHOSMUD_SECRET_KEY=test-secret-key-for-testing-only
MYTHOSMUD_JWT_SECRET=test-jwt-secret-for-testing-only
MYTHOSMUD_RESET_TOKEN_SECRET=test-reset-token-secret-for-testing-only
MYTHOSMUD_VERIFICATION_TOKEN_SECRET=test-verification-token-secret-for-testing-only
MYTHOSMUD_ADMIN_PASSWORD=test-admin-password
```

### Additional Test Configuration

```bash
# Alias storage for tests
ALIASES_DIR=server/tests/data/players/aliases

# Development settings for tests
DEBUG=true
LOG_LEVEL=DEBUG

# Test-specific settings
ENVIRONMENT=test
ENABLE_TEST_DATA=true
ENABLE_DEBUG_ENDPOINTS=true
```

## Setting Up Test Environment

### Option 1: Environment Variables

Set these variables in your shell before running tests:

```bash
export DATABASE_URL="sqlite+aiosqlite:///server/tests/data/players/test_players.db"
export NPC_DATABASE_URL="sqlite+aiosqlite:///server/tests/data/npcs/test_npcs.db"
# ... other variables
```

### Option 2: Test Configuration File

Create a `.env.test` file in the project root with the above configuration:

```bash
# Copy the example configuration
cp server/tests/test.env.example .env.test
# Edit as needed
```

### Option 3: Programmatic Configuration

The test suite automatically configures these variables in `conftest.py` if they are not already set.

## Database Paths

- **Player Database**: `server/tests/data/players/test_players.db`
- **NPC Database**: `server/tests/data/npcs/test_npcs.db`

These databases are automatically created and managed by the test suite.

## Security Note

**NEVER** use production security keys in test configurations. Always use test-specific values that are clearly marked as such.
