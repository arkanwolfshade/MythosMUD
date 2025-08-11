# MythosMUD Data Directory

This directory contains the main production data for MythosMUD.

## Database Files

### `players.db` - Main Production Database
- **Location**: `data/players.db`
- **Purpose**: Production player and room data
- **Created by**: `scripts/bootstrap_db.py`
- **Used by**: Production server instances

### Test Databases
- **Location**: `server/data/test_players.db` (if exists)
- **Purpose**: Legacy test database (no longer used)
- **Note**: Tests now use temporary databases created during test execution

## Database Schema

### Players Table
```sql
CREATE TABLE players (
    id TEXT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    strength INTEGER,
    dexterity INTEGER,
    constitution INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    sanity INTEGER,
    occult_knowledge INTEGER,
    fear INTEGER,
    corruption INTEGER,
    cult_affiliation INTEGER,
    current_room_id TEXT,
    created_at TEXT,
    last_active TEXT,
    experience_points INTEGER,
    level INTEGER
);
```

### Rooms Table
```sql
CREATE TABLE rooms (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    exits TEXT,
    zone TEXT
);
```

## Configuration

The database path can be configured using the `MYTHOS_DB_PATH` environment variable:

```bash
export MYTHOS_DB_PATH="/path/to/custom/players.db"
```

## Testing

Tests use temporary databases created during test execution to ensure isolation. No persistent test database files are created in this directory.
