# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-11-12-item-system-implementation/spec.md

## Schema Changes

Create `item_instances` table

- Columns: `item_instance_id` (PRIMARY KEY, TEXT, UUIDv7), `prototype_id` (TEXT, NOT NULL, FOREIGN KEY → `item_prototypes.prototype_id` if promoted), `owner_type` (TEXT CHECK in `('player','room','npc','container')`), `owner_id` (TEXT, NOT NULL), `location_context` (TEXT, NULLABLE), `quantity` (INTEGER DEFAULT 1 CHECK quantity > 0), `condition` (INTEGER), `flags_override` (INTEGER, NULLABLE), `binding_state` (TEXT), `attunement_state` (JSON/TEXT), `custom_name` (TEXT), `metadata` (JSON/TEXT), `created_at` (DATETIME DEFAULT CURRENT_TIMESTAMP), `updated_at` (DATETIME DEFAULT CURRENT_TIMESTAMP).
- Indexes: composite index on `(owner_type, owner_id)`, partial index for `location_context` when not NULL.
- Create `item_component_states` table
  - Columns: `id` (PRIMARY KEY AUTOINCREMENT), `item_instance_id` (TEXT, FOREIGN KEY → `item_instances.item_instance_id` ON DELETE CASCADE), `component_id` (TEXT NOT NULL), `state_payload` (JSON/TEXT NOT NULL), `updated_at` (DATETIME DEFAULT CURRENT_TIMESTAMP).
  - Indexes: composite index `(item_instance_id, component_id)`.
- Environment-specific databases:
  - Instantiate SQLite files at `/data/e2e_test/items/e2e_items.db`, `/data/local_test/items/local_items.db`, `/data/unit_test/items/unit_test_items.db`.
  - Synchronize schema migrations across all three via shared Alembic configuration or `uv`-driven migration script.

## Seed Data Specifications

Minimum seed inventory: at least two prototypes per equip slot (`HEAD`, `TORSO`, `LEGS`, `MAIN_HAND`, `OFF_HAND`, `ACCESSORY`, `RING`, `AMULET`, `BELT`, `BOOTS`, etc.).

- Each prototype entry includes descriptive metadata, wear flags, durability (if applicable), and stack rules to exercise mutation guard logic.
- Deterministic IDs for seeded prototypes (e.g., `equipment.head.artifact_veil`, `weapon.main_hand.hunters_knife`).
- Provide regeneration scripts (`scripts/items/seed_environment.ps1 --target e2e|local|unit`) ensuring idempotent seed application.

## Migration Strategy

Alembic migration adds new tables and indexes; leverage `op.create_table`, `op.create_index`, and `op.add_column` for existing join tables if integration needed.

- Migration includes backfill path for existing inventory data, mapping legacy payloads into the new `item_instances` table with generated UUIDs.
- Down migration removes tables while preserving archival dumps written to `/data/backups/items/YYYYMMDD/*.sql`.
