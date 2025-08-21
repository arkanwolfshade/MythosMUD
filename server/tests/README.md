# MythosMUD Test Suite

This directory contains the test suite for MythosMUD, including test data and database setup.

## Test Database

### Setup

The test database is located at `server/tests/data/test_players.db` and contains:

- **Schema**: Same as production database (players and rooms tables)
- **Test Data**: Pre-populated with test player data
- **Purpose**: Provides consistent test data for all tests

### Initialization

To initialize the test database:

```bash
cd server/tests
python init_test_db.py
```

This script will:
1. Create the test database with proper schema
2. Load test player data from JSON (if available)
3. Verify the database was created successfully

### Verification

To verify the test database:

```bash
cd server/tests
python verify_test_db.py
```

This will show:
- Database location and size
- Tables present
- Test players loaded
- Schema information

### Test Data

The test database contains:

- **Test Player**: `cmduser` in room `arkham_001`
- **Stats**: Pre-configured character attributes
- **Schema**: Full database schema matching production

### Usage in Tests

Tests automatically use the test database through the `patch_persistence_layer` fixture in `test_command_handler_unified.py`. This ensures:

- Consistent test data across all tests
- Isolation from production data
- Fast test execution (no database creation per test)

### Maintenance

If you need to update test data:

1. Modify the JSON data (if recreating from JSON)
2. Run `init_test_db.py` to recreate the database
3. Run tests to verify everything works

### File Structure

```
server/tests/
├── data/
│   ├── test_players.db      # Test database
│   └── test_persistence.log # Test log file
├── init_test_db.py          # Database initialization script
├── verify_test_db.py        # Database verification script
├── test_command_handler_unified.py  # Unified command handler tests
└── README.md               # This file
```

## Running Tests

```bash
cd server
python -m pytest tests/ -v
```

## Test Configuration

Tests use the following configuration:

- **Database**: `server/tests/data/test_players.db`
- **Log File**: `server/tests/data/test_persistence.log`
- **Isolation**: Each test uses the same database but with proper cleanup
