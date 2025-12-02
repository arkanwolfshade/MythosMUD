# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-11-11-inventory-equipment/spec.md

## Proposed Changes

- Create a new `player_inventories` table keyed off the existing players table (`players`), with exactly one row per player storing the entire inventory payload as a JSON CLOB for rapid delivery.
  - Columns: `player_id` (INTEGER PRIMARY KEY REFERENCES player_state(id) ON DELETE CASCADE), `inventory_json` (TEXT NOT NULL DEFAULT '[]'), `equipped_json` (TEXT NOT NULL DEFAULT '{}').
  - Table design anticipates future normalization into per-slot rows; migration path will replace the JSON CLOBs with structured records later.
- Introduce a migration script under `server/scripts/` using the SQLite CLI to create the table, populate one row per existing player with empty JSON payloads, and optionally port legacy inventory data.
- Ensure application logic handles JSON serialization/deserialization consistently, with validation that total slot counts and equipped mappings remain within spec.

## Specifications

- SQLite migration outline:
  - `CREATE TABLE player_inventories (player_id INTEGER PRIMARY KEY REFERENCES player_state(id) ON DELETE CASCADE, inventory_json TEXT NOT NULL DEFAULT '[]', equipped_json TEXT NOT NULL DEFAULT '{}');`
  - Add verification step ensuring every existing player receives exactly one row (INSERT OR IGNORE followed by lucidity check).
- Migration script loads any legacy JSON blobs, storing them verbatim in `inventory_json`/`equipped_json`, and removes deprecated columns after verification.
- For PostgreSQL parity: mirror table with `jsonb` columns and identical primary key relationship.
- Validation scripts confirm table existence, one-to-one row count with players, and JSON validity prior to server startup.
- JSON validation leverages the companion schema documented in `sub-specs/inventory-schema.json`; application tests must reference this schema to reject malformed payloads.

## Rationale

- JSON serialization keeps schema flexible while we iterate on inventory semantics; future normalization is blocked out by the dedicated table.
- One-row-per-player layout minimizes migration complexity now but still provides a clear upgrade path to normalized slots/items.
- Constraints rely on application-level validation for slot limits; adding indexes is unnecessary until table normalization introduces per-slot rows.
