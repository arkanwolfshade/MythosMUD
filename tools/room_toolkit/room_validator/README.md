# Room Pathing Validator

A comprehensive validation tool for room connectivity and structure in the
MythosMUD world. This validator implements the dimensional mapping techniques
described in the Pnakotic Manuscripts to ensure proper eldritch architecture.

## Features

**JSON Schema Validation**: Validates room definitions against a comprehensive schema

**Connectivity Analysis**: Checks for unreachable rooms and dead ends

**Bidirectional Path Validation**: Ensures proper return paths between rooms

**Support for Exit Flags**: Handles one-way exits and

self-references

**Zone-based Validation**: Validate specific zones or the entire world

**Multiple Output Formats**: Console output with colors or structured JSON

- **Progress Indicators**: Visual feedback for large room sets
- **Automatic Fixing**: Fix common issues automatically (with backup option)

## Installation

1. Install dependencies:

```bash
uv pip install -r requirements.txt
```

1. Run the validator:

```bash
python validator.py --base-path ../data/local/rooms
```

## Usage

### Basic Validation

```bash
# Validate all rooms in the default location

python validator.py

# Validate rooms in a specific directory

python validator.py --base-path ./my_rooms/
```

### Zone-specific Validation

```bash
# Validate only the arkham zone

python validator.py --zone arkham
```

### Output Formats

```bash
# Console output with colors (default)

python validator.py

# JSON output for programmatic consumption

python validator.py --format json

# Disable colors for terminal compatibility

python validator.py --no-colors
```

### Verbose Mode

```bash
# Show detailed progress and processing information

python validator.py --verbose
```

### Schema-only Validation

```bash
# Only validate JSON schema, skip connectivity checks

python validator.py --schema-only
```

### Automatic Fixing

```bash
# Automatically fix common issues (use with caution)

python validator.py --fix

# Create backups before fixing

python validator.py --fix --backup

# Fix specific zone only

python validator.py --zone arkham --fix --backup
```

## Exit Format Support

The validator supports both legacy string format and new object format for exits:

### Legacy Format

```json
{
  "exits": {
    "north": "arkham_002",
    "south": null
  }
}
```

### New Format (with flags)

```json
{
  "exits": {
    "north": {
      "target": "arkham_002",
      "flags": ["one_way"]
    },
    "south": {
      "target": "arkham_004",
      "flags": []
    }
  }
}
```

### Supported Exit Flags

`"one_way"`: Exit doesn't require bidirectional return path

- `"self_reference"`: Allow room to reference itself (for teleporters, etc.)

## Validation Rules

### Structure Rules

**Schema Validation**: Ensures rooms conform to JSON schema

**Duplicate ID Detection**: Checks for duplicate room IDs across zones

**Exit Reference Validation**: Verifies all exit targets exist

### Connectivity Rules

**Bidirectional Connections**: Ensures room A → room B implies room B →
room A

**Unreachable Room Detection**: Finds rooms that cannot be reached from
starting point

**Dead End Detection**: Identifies rooms with no exits (true dead ends)

**Self Reference Validation**: Checks for proper self-reference flags

## Sample Output

### Console Output

```text
🔍 Room Validator v1.0
📁 Scanning ../data/local/rooms...

✅ arkham zone: 7 rooms discovered

🔄 Processing rooms... ████████████████████ 100% (7/7)

❌ ERRORS FOUND:

🏠 arkham_002.json (Miskatonic University Gates)
  ❌ Bidirectional: Exit 'south' →
  earth_arkhamcity_intersection_derby_high, but
  earth_arkhamcity_intersection_derby_high has no 'north' return
     💡 Suggestion: Add "north": "arkham_002" to
     earth_arkhamcity_intersection_derby_high or flag as one_way

⚠️  WARNINGS:
🏠 arkham_007.json (Underground Tunnels)
  ⚠️  Self-reference: Room references itself without proper flag

📊 SUMMARY:
  Zones: 1
  Rooms: 7 total
  Errors: 1 🔴
  Warnings: 1 🟡

❌ Validation failed - please fix errors above
```

### JSON Output

```json
{
  "summary": {
    "zones": 1,
    "rooms": 7,
    "errors": 1,
    "warnings": 1,
    "success": false
  },
  "errors": [
    {
      "type": "bidirectional",
      "room_id": "arkham_002",
      "message": "Exit 'south' → earth_arkhamcity_intersection_derby_high, but
      earth_arkhamcity_intersection_derby_high has no 'north' return",
      "suggestion": "Add \"north\": \"arkham_002\" to
      earth_arkhamcity_intersection_derby_high or flag as one_way"
    }
  ],
  "warnings": [
    {
      "type": "self_reference",
      "room_id": "arkham_007",
      "message": "Room references itself without proper flag"
    }
  ]
}
```

## Architecture

The CLI is a single-command tool by design (one entry point in `validator.py`). If subcommands
are added later (e.g. `validate`, `report`, `fix`), the layout will be refactored to a click Group
and a `commands/` package (e.g. `commands/validate.py`) with `cli.add_command(...)`.

The validator is organized into several modules:

**`core/room_loader.py`**: Discovers and loads room files

**`core/schema_validator.py`**: Validates JSON schema compliance

**`core/path_validator.py`**: Analyzes room connectivity using graph algorithms

**`core/reporter.py`**: Formats and displays validation results

- **`core/fixer.py`**: Automatically fixes common validation issues
- **`rules/`**: Extensible rule system for validation logic
- **`schemas/room_schema.json`**: JSON schema definition for rooms

## Automatic Fixes

The validator can automatically fix the following issues:

### Schema Issues

**Missing Required Fields**: Add missing `exits`, `field1`, `field2`, `field3` fields

**Empty Exit Objects**: Initialize empty exit objects with proper structure

### Connectivity Issues

**Missing Return Paths**: Add bidirectional connections automatically

**Self-Reference Flags**: Add `self_reference` flags to self-referencing exits

### Safety Features

**Backup Creation**: Create timestamped backups before making changes

**Selective Fixing**: Only fix issues that can be safely resolved

**Error Reporting**: Report any fixes that fail to apply

### Usage Examples

```bash
# Fix all issues with backups

python validator.py --fix --backup

# Fix only specific zone

python validator.py --zone arkham --fix

# Validate first, then fix if needed

python validator.py --verbose
python validator.py --fix --backup
```

## Contributing

To add new validation rules:

1. Create a new rule class inheriting from `ValidationRule`
2. Implement the `validate()` method
3. Add the rule to the validation pipeline in `validator.py`

## License

This validator is part of the MythosMUD project and follows the same licensing terms.
