# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-10-27-player-death-respawn/spec.md

## Schema Changes

### 1. Players Table - Add Respawn Room Field

**Table:** `players`

**New Column:**
```sql
ALTER TABLE players
ADD COLUMN respawn_room_id VARCHAR(100) DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001';
```

**Column Specifications:**
- **Name:** `respawn_room_id`
- **Type:** `VARCHAR(100)`
- **Nullable:** `YES` (NULL means use default)
- **Default:** `'earth_arkhamcity_sanitarium_room_foyer_001'`
- **Purpose:** Store player's chosen respawn location
- **Index:** Not required initially (can add if respawn queries become frequent)

**Rationale:**
- Allows future feature: players choosing custom respawn points
- Defaults to Arkham Sanitarium for thematic appropriateness
- VARCHAR(100) accommodates current room ID format with room for growth
- Nullable allows explicit NULL to trigger default behavior

### 2. Player Stats JSON - HP Range Extension

**Column:** `players.stats` (JSON Text field)

**Current Structure:**
```json
{
  "strength": 10,
  "dexterity": 10,
  "constitution": 10,
  "intelligence": 10,
  "wisdom": 10,
  "charisma": 10,
  "sanity": 100,
  "occult_knowledge": 0,
  "fear": 0,
  "corruption": 0,
  "cult_affiliation": 0,
  "current_health": 100
}
```

**No Schema Change Required** - `current_health` already supports negative values as an integer field

**Application-Level Enforcement:**
- Minimum HP: -10 (enforced in `CombatService._apply_damage()`)
- Maximum HP: 100 (current maximum, enforced by game mechanics)
- Mortally Wounded Range: 0 to -10 (exclusive)
- Dead State: -10 or below (capped at -10)

### 3. Optional: Death Log Table (Future Enhancement)

**Note:** This table structure is provided for future reference but is NOT required for the initial implementation.

```sql
CREATE TABLE IF NOT EXISTS player_death_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id VARCHAR(50) NOT NULL,
    death_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    death_location VARCHAR(100) NOT NULL,
    killer_id VARCHAR(50),  -- NPC ID or player ID
    killer_name VARCHAR(100),
    final_hp INTEGER,  -- Should be -10
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

CREATE INDEX idx_death_log_player ON player_death_log(player_id);
CREATE INDEX idx_death_log_timestamp ON player_death_log(death_timestamp);
```

**Purpose:** Track player death history for statistics and achievements
**Deferred:** Implementation deferred to broader player metrics system

## Migration Strategy

### SQLite Migration (Development)

**File:** `scripts/migrations/add_respawn_room_id.sql` (NEW)

```sql
-- Migration: Add respawn_room_id to players table
-- Date: 2025-10-27
-- Purpose: Enable player death/respawn system

BEGIN TRANSACTION;

-- Add respawn_room_id column
ALTER TABLE players
ADD COLUMN respawn_room_id VARCHAR(100) DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001';

-- Verify column was added
SELECT name, type FROM pragma_table_info('players') WHERE name = 'respawn_room_id';

COMMIT;
```

### Manual Application

Since the project uses SQLite with manual schema management:

1. Update `server/database/schema.sql` to include `respawn_room_id` field
2. Run migration script on existing databases:
   - `data/local/players/local_players.db`
   - `data/unit_test/players/unit_test_players.db`
3. Update `Player` model in `server/models/player.py` to include field
4. Update test fixtures to include `respawn_room_id` in sample data

## Data Integrity Considerations

### Foreign Key Constraint (Optional)

Currently, room_id references are not enforced via foreign keys. Consider adding:

```sql
-- Optional: Add foreign key constraint to ensure respawn room exists
-- Note: Would require rooms table to exist first
ALTER TABLE players
ADD CONSTRAINT fk_respawn_room
FOREIGN KEY (respawn_room_id)
REFERENCES rooms(room_id);
```

**Decision:** NOT implementing for initial version
- **Reason:** Room data stored in JSON files, not database
- **Alternative:** Application-level validation in `PlayerRespawnService`

### Default Value Handling

**Strategy:**
- NULL `respawn_room_id` → use `DEFAULT_RESPAWN_ROOM` constant
- Invalid `respawn_room_id` → fallback to `DEFAULT_RESPAWN_ROOM` with warning log
- Missing respawn room file → fallback to `DEFAULT_RESPAWN_ROOM` with error log

## Backward Compatibility

- Existing players without `respawn_room_id` will use default (sanitarium)
- No data migration required for existing player records
- Column can be added via `ALTER TABLE` without rebuilding database
