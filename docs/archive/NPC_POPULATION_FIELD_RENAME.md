# NPC Spawn Rule Field Rename: Players to Population

**Date**: October 14, 2025
**Status**: ✅ Complete
**Migration**: Required for existing databases

## Overview

The `npc_spawn_rules` table fields `min_players` and `max_players` have been renamed to `min_population` and `max_population` to correctly reflect their purpose: controlling **NPC/mob population counts**, not player count thresholds.

## Problem Statement

The original field names were misleading:

- `min_players` / `max_players` implied they controlled when NPCs spawn based on player counts
- Actually controlled how many NPC instances should be maintained (population limits)
- Code was incorrectly checking against player counts instead of NPC counts

## Changes Made

### 1. Database Model (`server/models/npc.py`)

✅ Renamed column: `min_players` → `min_population`

✅ Renamed column: `max_players` → `max_population`

✅ Renamed method: `can_spawn_for_player_count()` → `can_spawn_with_population()`
- ✅ Updated method logic to check NPC population instead of player count

**Before:**

```python
def can_spawn_for_player_count(self, player_count: int) -> bool:
    """Check if this rule allows spawning for given player count."""
    return self.min_players <= player_count <= self.max_players
```

**After:**

```python
def can_spawn_with_population(self, current_population: int) -> bool:
    """Check if this rule allows spawning given current NPC population."""
    return current_population < self.max_population
```

### 2. API Models (`server/api/admin/npc.py`)

✅ Updated `NPCSpawnRuleCreate` model

✅ Updated `NPCSpawnRuleResponse` model

✅ Updated `from_orm()` method

### 3. Service Layer (`server/services/npc_service.py`)

✅ Updated `create_spawn_rule()` method signature and parameters

✅ Updated validation logic and error messages

✅ Updated query ordering

### 4. Population Control (`server/npc/population_control.py`)

✅ Fixed spawning logic to check **NPC population** instead of player count

✅ Updated method calls to use `can_spawn_with_population()`

✅ Updated logging messages to reflect population checks

**Before (INCORRECT):**

```python
if not rule.can_spawn_for_player_count(self.current_game_state["player_count"]):
    logger.info(f"Spawn rule failed player count check (current players: {player_count})")
    continue
```

**After (CORRECT):**

```python
if not rule.can_spawn_with_population(current_npc_count):
    logger.info(f"Spawn rule failed population check (current NPCs: {current_npc_count}, max: {rule.max_population})")
    continue
```

### 5. Spawning Service (`server/npc/spawning_service.py`)

✅ Fixed spawning logic to check **NPC population** instead of player count

✅ Updated method calls and logging

### 6. SQL Schema (`server/sql/npc_schema.sql`)

✅ Updated table definition

✅ Updated table comments

### 7. Tests (`server/tests/unit/npc/test_npc_population_control.py`)

✅ Updated all fixture definitions

✅ Rewrote test from `test_npc_spawn_rule_player_count_validation` to `test_npc_spawn_rule_population_validation`

✅ Tests now validate NPC population limits instead of player count thresholds

### 8. Migration Script

✅ Created Alembic migration: `server/alembic/versions/rename_players_to_population.py`

✅ Handles SQLite table recreation approach

✅ Includes rollback functionality
- ✅ Preserves all data and indexes

## Migration Instructions

### For Development Databases

```bash
# Run the Alembic migration

cd server
alembic upgrade head
```

### For Production Databases

1. **Backup** the database before running migration
2. Run the Alembic migration during maintenance window
3. Verify data integrity after migration

### Manual Migration (if not using Alembic)

```sql
-- 1. Create new table with corrected column names
CREATE TABLE npc_spawn_rules_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    npc_definition_id INTEGER NOT NULL,
    sub_zone_id TEXT NOT NULL,
    min_population INTEGER DEFAULT 0 NOT NULL,
    max_population INTEGER DEFAULT 999 NOT NULL,
    spawn_conditions TEXT NOT NULL DEFAULT '{}',
    FOREIGN KEY (npc_definition_id) REFERENCES npc_definitions(id) ON DELETE CASCADE
);

-- 2. Copy data from old table
INSERT INTO npc_spawn_rules_new (id, npc_definition_id, sub_zone_id, min_population, max_population, spawn_conditions)
SELECT id, npc_definition_id, sub_zone_id, min_players, max_players, spawn_conditions
FROM npc_spawn_rules;

-- 3. Drop old table
DROP TABLE npc_spawn_rules;

-- 4. Rename new table
ALTER TABLE npc_spawn_rules_new RENAME TO npc_spawn_rules;

-- 5. Recreate indexes
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_sub_zone ON npc_spawn_rules(sub_zone_id);
CREATE INDEX IF NOT EXISTS idx_npc_spawn_rules_npc_def ON npc_spawn_rules(npc_definition_id);
```

## Semantic Clarification

### Field Purpose

**`min_population` / `max_population`** control:

- Minimum number of NPC instances of this type to maintain in the zone
- Maximum number of NPC instances of this type allowed in the zone

### Example Usage

```python
# Spawn rule: Keep 2-5 goblins in the forest

spawn_rule = NPCSpawnRule(
    npc_definition_id=goblin_def_id,
    sub_zone_id="forest/clearing",
    min_population=2,    # Always try to maintain at least 2 goblins
    max_population=5,    # Never spawn more than 5 goblins
    spawn_conditions='{"time_of_day": "night"}'
)

# Population check

current_goblin_count = 3
if spawn_rule.can_spawn_with_population(current_goblin_count):
    # Can spawn more (3 < 5)

    spawn_another_goblin()
```

## Breaking Changes

### Code Changes Required

Any code that directly accesses these fields must be updated:

```python
# OLD (will fail)

rule.min_players
rule.max_players
rule.can_spawn_for_player_count(player_count)

# NEW (correct)

rule.min_population
rule.max_population
rule.can_spawn_with_population(current_npc_count)
```

### Database Changes Required

Existing databases **must** run the migration

- No data loss - all values are preserved
- Column names change, semantics corrected

## Testing

All tests updated to verify correct behavior:
✅ Tests verify NPC population limits

✅ Tests verify spawning logic checks NPC counts

✅ Tests verify max_population prevents over-spawning

## Benefits

1. **Clarity**: Field names now accurately reflect their purpose
2. **Correctness**: Spawning logic now checks NPC population, not player count
3. **Maintainability**: Future developers won't be confused by misleading names
4. **Documentation**: Code is self-documenting with correct terminology

## References

Database model: `server/models/npc.py`

- API models: `server/api/admin/npc.py`
- Spawning logic: `server/npc/population_control.py`, `server/npc/spawning_service.py`
- Migration script: `server/alembic/versions/rename_players_to_population.py`

---

*"Proper nomenclature prevents the summoning of incorrect entities from the void of confusion."*
— The Pnakotic Manuscripts, Volume VII
