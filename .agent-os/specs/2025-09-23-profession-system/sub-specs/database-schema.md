# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-09-23-profession-system/spec.md

## Changes

### New Tables
- **professions**: Stores profession data including requirements and effects

### Table Modifications
- **players**: Add profession_id column with default value 0

### Indexes and Constraints
- Index on professions.is_available for efficient filtering
- Foreign key constraint on players.profession_id (added after professions table population)

## Specifications

### Professions Table
```sql
CREATE TABLE professions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    flavor_text TEXT NOT NULL,
    stat_requirements TEXT NOT NULL, -- JSON: {"strength": 12, "intelligence": 10}
    mechanical_effects TEXT NOT NULL, -- JSON: future bonuses/penalties
    is_available BOOLEAN NOT NULL DEFAULT 1
);

CREATE INDEX idx_professions_available ON professions(is_available);
```

### Player Table Modification
```sql
ALTER TABLE players ADD COLUMN profession_id INTEGER NOT NULL DEFAULT 0;
-- Foreign key constraint will be added after professions table is populated
```

### Seeded Data
```sql
INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects) VALUES
(0, 'Tramp', 'A wandering soul with no fixed abode', 'You have learned to survive on the streets, finding shelter where you can and making do with what you have.', '{}', '{}'),
(1, 'Gutter Rat', 'A street-smart survivor of the urban underbelly', 'You know the hidden passages and dark corners of the city, where others fear to tread.', '{}', '{}');
```

### Foreign Key Constraint (After Seeding)
```sql
-- Add foreign key constraint after professions are seeded
ALTER TABLE players ADD CONSTRAINT fk_players_profession
FOREIGN KEY (profession_id) REFERENCES professions(id);
```

## Rationale

### JSON Fields for Flexibility
- **stat_requirements**: JSON format allows for complex requirement structures (minimums, ranges, combinations) without schema changes
- **mechanical_effects**: JSON format enables future expansion of profession bonuses/penalties without database migrations

### Default Value Strategy
- **profession_id DEFAULT 0**: Ensures existing players automatically get "Tramp" profession without data migration
- **is_available DEFAULT 1**: Allows easy enabling/disabling of professions without data changes

### Performance Considerations
- **Index on is_available**: Enables efficient filtering of available professions for selection UI
- **Index on profession_id**: Optimizes player-profession lookups and foreign key operations

### Data Integrity Rules
- **UNIQUE constraint on name**: Prevents duplicate profession names
- **NOT NULL constraints**: Ensures all required profession data is present
- **Foreign key constraint**: Maintains referential integrity between players and professions
