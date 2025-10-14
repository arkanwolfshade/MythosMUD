# MythosMUD Test Suite

This directory contains the test suite for MythosMUD, including test data and database setup.

## 📋 Test Suite Refactoring

**Important:** The test suite is undergoing a major reorganization to improve maintainability and discoverability.

### Documentation
- 📖 [Test Refactoring Summary](../../docs/TEST_REFACTORING_SUMMARY.md) - Executive overview
- 🗺️ [Test Suite Refactoring Plan](../../docs/TEST_SUITE_REFACTORING_PLAN.md) - Complete strategy
- 📍 [Test Migration Mapping](../../docs/TEST_MIGRATION_MAPPING.md) - File-by-file mapping
- 🧭 [Test Organization Guide](./TEST_ORGANIZATION_GUIDE.md) - Quick reference for developers

### Tools
- 📊 [Migration Tracking Script](./scripts/track_migration.py) - Track refactoring progress

```bash
# Show migration summary
python server/tests/scripts/track_migration.py

# Show detailed status
python server/tests/scripts/track_migration.py --detailed

# Validate migration
python server/tests/scripts/track_migration.py --validate
```

### Quick Reference

**Where should I put a new test?** See the [Test Organization Guide](./TEST_ORGANIZATION_GUIDE.md)

**Current Status:** ✅ **MIGRATION & CONSOLIDATION COMPLETE!** All 210 files migrated and 28 legacy files consolidated into 181 optimized test files. See [Final Summary](../../docs/TEST_REFACTORING_FINAL_SUMMARY.md)

## Test Database

### Setup

The test database is located at `data/unit_test/players/unit_test_players.db` and contains:

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
│   ├── unit_test_players.db      # Test database
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

- **Database**: `data/unit_test/players/unit_test_players.db`
- **Log Directory**: `logs/unit_test/` (project root logs for unit tests)
- **Config File**: `.env.unit_test` (template: `.env.unit_test.example`)
- **Isolation**: Each test uses the same database but with proper cleanup
