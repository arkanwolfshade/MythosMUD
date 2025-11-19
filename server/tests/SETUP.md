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
- `DATABASE_URL=...` - **PostgreSQL** database URL for player data (format: `postgresql+asyncpg://user:password@host:port/database`)
- `DATABASE_NPC_URL=...` - **PostgreSQL** database URL for NPC data (format: `postgresql+asyncpg://user:password@host:port/database`)
- `MYTHOSMUD_ADMIN_PASSWORD=...` - Admin password for tests
- And many other configuration variables (see `env.unit_test.example` for complete list)

**CRITICAL**: Tests require PostgreSQL - SQLite is no longer supported. The default configuration uses:
- Database: `mythos_unit`
- User: `postgres`
- Password: `Cthulhu1` (as configured in `.env.unit_test`)
- Host: `localhost:5432`

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

## PostgreSQL Setup

Before running tests, you must ensure PostgreSQL is properly configured:

### 1. Install PostgreSQL

If PostgreSQL is not installed:
- Download from: https://www.postgresql.org/download/windows/
- Install with default settings
- Note the password you set for the `postgres` user

### 2. Verify PostgreSQL Connection

Run the diagnostic script to check PostgreSQL connectivity:

```powershell
# From project root
pwsh scripts/check_postgresql.ps1
```

This will verify:
- PostgreSQL service is running
- Network connectivity to the server
- Authentication credentials
- Database existence

### 3. Create Test Database

If the database doesn't exist, create it:

```powershell
# From project root
pwsh scripts/setup_postgresql_test_db.ps1
```

Or manually:

```powershell
# Set password (replace with your actual postgres password)
$env:PGPASSWORD = "Cthulhu1"
psql -U postgres -c "CREATE DATABASE mythos_unit;"
```

### 4. Update Password if Needed

If your PostgreSQL `postgres` user has a different password, either:

**Option A**: Update `.env.unit_test`:
```powershell
# Edit server/tests/.env.unit_test
# Change: DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/mythos_unit
```

**Option B**: Change PostgreSQL password to match `.env.unit_test`:
```powershell
psql -U postgres -c "ALTER USER postgres WITH PASSWORD 'Cthulhu1';"
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

### Error: "password authentication failed for user 'postgres'"

This error occurs when PostgreSQL authentication fails.

**Solutions**:
1. **Check PostgreSQL is running**:
   ```powershell
   Get-Service -Name "*postgresql*"
   Start-Service -Name "postgresql-x64-*"  # Adjust service name as needed
   ```

2. **Verify password matches**:
   ```powershell
   # Run diagnostic
   pwsh scripts/check_postgresql.ps1
   ```

3. **Reset PostgreSQL password** (if needed):
   ```powershell
   psql -U postgres -c "ALTER USER postgres WITH PASSWORD 'Cthulhu1';"
   ```

4. **Check database exists**:
   ```powershell
   pwsh scripts/setup_postgresql_test_db.ps1
   ```

### Error: "connection to server at 'localhost' (127.0.0.1), port 5432 failed"

This error occurs when PostgreSQL is not running or not accessible.

**Solutions**:
1. **Start PostgreSQL service**:
   ```powershell
   Get-Service -Name "*postgresql*" | Start-Service
   ```

2. **Check PostgreSQL is listening on port 5432**:
   ```powershell
   netstat -an | findstr :5432
   ```

3. **Verify firewall settings** (if using remote PostgreSQL)

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
