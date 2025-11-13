# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-11-13-sanity-system-expansion/spec.md

## Schema Changes

### Table: `player_sanity`

- `player_id` INTEGER PRIMARY KEY REFERENCES `players(id)` ON DELETE CASCADE
- `current_san` INTEGER NOT NULL DEFAULT 100 CHECK (current_san BETWEEN -100 AND 100)
- `current_tier` TEXT NOT NULL CHECK (current_tier IN ('lucid','uneasy','fractured','deranged','catatonic'))
- `liabilities` JSON NOT NULL DEFAULT '[]'
- `last_updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
- `catatonia_entered_at` DATETIME NULL
- Index: `idx_player_sanity_tier` on (`current_tier`)

### Table: `sanity_adjustment_log`

- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `player_id` INTEGER NOT NULL REFERENCES `players(id)` ON DELETE CASCADE
- `delta` INTEGER NOT NULL
- `reason_code` TEXT NOT NULL
- `metadata` JSON NOT NULL DEFAULT '{}'
- `location_id` TEXT NULL
- `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
- Index: `idx_sanity_adjustment_player_created` on (`player_id`,`created_at`)

### Table: `sanity_exposure_state`

- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `player_id` INTEGER NOT NULL REFERENCES `players(id)` ON DELETE CASCADE
- `entity_archetype` TEXT NOT NULL
- `encounter_count` INTEGER NOT NULL DEFAULT 0
- `last_encounter_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
- Unique constraint on (`player_id`,`entity_archetype`)

### Table: `sanity_cooldowns`

- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `player_id` INTEGER NOT NULL REFERENCES `players(id)` ON DELETE CASCADE
- `action_code` TEXT NOT NULL
- `cooldown_expires_at` DATETIME NOT NULL
- Unique constraint on (`player_id`,`action_code`)

## Migration Notes

- Populate `player_sanity` with existing players (`current_san = 100`, `current_tier = 'lucid'`).
- Backfill `sanity_exposure_state` only when encounters occur; no initial data required.
- Ensure migrations run under a transaction; create indexes after data backfill to minimize lock duration.

## Rationale

- Separate logs allow telemetry without bloating core player table.
- Exposure state supports first-time/repeat loss rules with efficient lookups.
- Cooldowns table unifies recovery actions and hallucination timers, keeping logic server-driven.
