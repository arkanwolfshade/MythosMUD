# Test Data Structure

This directory mirrors the production data structure (`/data`) to provide isolated test data for the MythosMUD test suite.

## Structure

```
server/tests/data/
├── players/
│   └── test_players.db          # Test SQLite database for player data
├── rooms/
│   └── arkham/
│       ├── arkham_001.json      # Test room: Town Square (central hub)
│       ├── arkham_002.json      # Test room: University Gates
│       ├── arkham_003.json      # Test room: Old South Docks
│       ├── arkham_004.json      # Test room: East Market Bazaar
│       ├── arkham_005.json      # Test room: West Alley Shadows
│       ├── arkham_006.json      # Test room: University Quad
│       └── arkham_007.json      # Test room: Foggy Riverside Path
└── README.md                    # This file
```

## Purpose

- **Isolation**: Test data is completely separate from production data
- **Consistency**: Structure matches production for realistic testing
- **Simplicity**: Mock rooms have minimal exits for focused testing
- **Reliability**: Tests can run without affecting production data

## Usage

The test suite should be configured to use this data directory instead of the production `/data` directory. This ensures:

1. Tests don't interfere with production data
2. Test results are predictable and repeatable
3. Mock data can be tailored for specific test scenarios
4. Database operations are isolated

## Room Layout

The test rooms form a complex network matching the production mock data:
- `arkham_001` (Town Square) - Central hub with exits in all directions
- `arkham_002` (University Gates) - North of town square, connects to University Quad
- `arkham_003` (Old South Docks) - South of town square, connects to Riverside Path
- `arkham_004` (East Market Bazaar) - East of town square
- `arkham_005` (West Alley Shadows) - West of town square
- `arkham_006` (University Quad) - North of University Gates
- `arkham_007` (Foggy Riverside Path) - South of Old South Docks

This provides comprehensive movement testing with multiple paths and dead ends.
