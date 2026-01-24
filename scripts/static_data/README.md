# Static Data SQL Generation

This directory contains scripts for generating SQL seed data files from JSON
source data.

## Purpose

The `generate_sql.mjs` script reads JSON data files and generates PostgreSQL
INSERT statements for:

**World data**: Zones, subzones, rooms, and room links

**Calendar data**: Holidays and NPC schedules

**Emotes**: Player emotes and aliases

**Zone configurations**: Zone and subzone configuration mappings

## Output

The script generates a single SQL file:

**Output location**: `data/db/00_world_and_emotes.sql`

**Format**: PostgreSQL-compatible INSERT statements with `ON CONFLICT` handling

**Structure**: Transaction-wrapped with proper dependency ordering

## Usage

### Prerequisites

Install Node.js dependencies:

```bash
cd scripts/static_data
npm install
```

### Generate SQL

From the project root:

```bash
node scripts/static_data/generate_sql.mjs
```

Or from this directory:

```bash
node generate_sql.mjs
```

### Output

The script will:

1. Validate all JSON files against their schemas
2. Generate deterministic UUIDs using v5 UUIDs with a project namespace
3. Create INSERT statements with proper SQL escaping
4. Write the output to `data/db/00_world_and_emotes.sql`

## Source Data

The script reads from:

- `data/local/rooms/**/*.json` - Room definitions and configurations
- `data/local/calendar/holidays.json` - Holiday definitions
- `data/local/calendar/schedules/npc.json` - NPC schedule definitions
- `data/local/emotes.json` - Emote definitions

## Schemas

JSON schemas are located in:

- `db/static/schemas/room.schema.json`
- `db/static/schemas/holidays.schema.json`
- `db/static/schemas/npc_schedules.schema.json`
- `db/static/schemas/emotes.schema.json`

## Validation

The script uses AJV (Another JSON Schema Validator) to validate all input data
before generating SQL. Validation errors will cause the script to exit with
an error.

## UUID Generation

All IDs are generated using UUID v5 with a deterministic namespace:

**Namespace UUID**: `c8e7f86d-b1c9-4074-8b2e-9f3c6c8a9f2a`

**Format**: `uuidv5("table_name:stable_id", NAMESPACE)`

**Deterministic**: Same input always produces same UUID

## Files

**`generate_sql.mjs`** - Main generation script

**`validate.mjs`** - Standalone validation script (if needed)

**`package.json`** - Node.js dependencies

**`temp_debug.txt`** - Temporary debug output (can be deleted)

## Integration

The generated SQL file (`data/db/00_world_and_emotes.sql`) is:

- Used by seed data loading scripts
- Referenced in `data/db/README.md`
- Part of the DML baseline (see `data/db/README.md`)

## Notes

The script automatically handles SQL escaping (single quotes, etc.)

- All INSERT statements use `ON CONFLICT DO NOTHING` for idempotency

- Zone and subzone configurations are updated with `ON CONFLICT DO UPDATE` to

  allow config changes

- Room links only include links where both endpoints exist in the dataset
