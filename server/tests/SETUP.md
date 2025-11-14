# MythosMUD Test Environment Setup

This document describes the setup requirements for running MythosMUD server tests.

## Prerequisites

Before running any server tests, you must ensure that the test environment is properly configured.

## Required Environment Files

### `.env.unit_test`

The server tests require a `.env.unit_test` file located at `server/tests/.env.unit_test`. This file contains all the configuration variables needed for unit testing.

**CRITICAL**: This file is in `.gitignore` and will not be committed to version control. You must create it manually.

## Setup Instructions

### Option 1: Automatic Setup (Recommended)

Run the setup script to automatically create the required environment files:

```powershell
# From the project root
make setup-test-env
```

Or run the PowerShell script directly:

```powershell
pwsh scripts/setup_test_environment.ps1
```

### Option 2: Manual Setup

If you prefer to set up the environment manually:

1. Copy the example environment file:
   ```powershell
   Copy-Item "env.unit_test.example" "server\tests\.env.unit_test"
   ```

2. Verify the file was created:
   ```powershell
   Test-Path "server\tests\.env.unit_test"
   ```

## Environment File Contents

The `.env.unit_test` file must contain the following required variables:

- `SERVER_PORT=54731` - Port for test server
- `DATABASE_URL=...` - SQLite database URL for player data
- `DATABASE_NPC_URL=...` - SQLite database URL for NPC data
- `MYTHOSMUD_ADMIN_PASSWORD=...` - Admin password for tests
- And many other configuration variables (see `env.unit_test.example` for complete list)

## Running Tests

Once the environment is set up, you can run tests:

```powershell
# Run all tests (automatically sets up environment)
make test

# Run only server tests (use PYTEST_ADDOPTS to narrow scope if needed)
make test

# Run specific test file
uv run pytest server/tests/unit/commands/test_utility_commands.py -v
```

## Troubleshooting

### Error: "Test environment file not found"

This error occurs when `server/tests/.env.unit_test` is missing.

**Solution**: Run `make setup-test-env` or manually copy `env.unit_test.example` to `server/tests/.env.unit_test`

### Error: "Test environment file missing required variables"

This error occurs when the `.env.unit_test` file exists but is missing required configuration variables.

**Solution**: Ensure the file contains all required variables. You can recreate it by running `make setup-test-env -Force`

### Error: "ValidationError: Field required"

This error occurs when Pydantic configuration validation fails due to missing environment variables.

**Solution**: Ensure the `.env.unit_test` file exists and contains all required variables.

## File Locations

- **Example file**: `env.unit_test.example` (committed to version control)
- **Test environment**: `server/tests/.env.unit_test` (not committed, must be created)
- **Setup script**: `scripts/setup_test_environment.ps1`
- **Validation**: `server/tests/conftest.py` (validates environment on test startup)

## Security Notes

- The `.env.unit_test` file contains test-specific secrets and passwords
- These are not production values and are safe to use in test environments
- The file is in `.gitignore` to prevent accidental commits
- Never use test environment values in production

## Integration with CI/CD

In continuous integration environments, ensure that:

1. The test environment file is created before running tests
2. All required environment variables are properly set
3. Database paths are correctly configured for the CI environment

## Additional Resources

- See `server/tests/conftest.py` for detailed environment validation logic
- See `env.unit_test.example` for complete list of required variables
- See `scripts/setup_test_environment.ps1` for automated setup logic
