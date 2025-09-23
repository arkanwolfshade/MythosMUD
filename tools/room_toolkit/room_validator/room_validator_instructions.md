# Room Pathing Validator Implementation Instructions

## Project Overview

Create a Python-based room pathing validator for a text-based game world. The validator checks room connectivity, validates JSON structure, and ensures proper pathing between game rooms organized in zones.

## Project Structure

Create the following directory structure:

```
room_validator/
├── validator.py              # Main CLI script
├── core/
│   ├── __init__.py
│   ├── room_loader.py        # File discovery and JSON parsing
│   ├── schema_validator.py   # JSON schema validation
│   ├── path_validator.py     # Room connectivity validation
│   └── reporter.py           # Output formatting and colors
├── schemas/
│   └── room_schema.json      # JSON schema definition
├── rules/
│   ├── __init__.py
│   ├── base_rule.py          # Abstract base class for rules
│   ├── connectivity_rules.py # Bidirectional, unreachable, dead-end rules
│   └── structure_rules.py    # Schema, duplicate ID rules
└── requirements.txt
```

## Requirements File (requirements.txt)

```
jsonschema>=4.17.0
colorama>=0.4.6
tqdm>=4.64.0
click>=8.1.0
```

## JSON Schema Design (schemas/room_schema.json)

### Enhanced Exit Format

The validator must support both legacy string format and new object format for exits:

**Legacy Format (backward compatible):**

```json
{
  "exits": {
    "north": "arkham_002",
    "south": null
  }
}
```

**New Format (with flags):**

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

**Supported Exit Flags:**

- `"one_way"` - Exit doesn't require bidirectional return path
- `"self_reference"` - Allow room to reference itself (for teleporters, etc.)

### Complete JSON Schema

Create a JSON schema that validates:

- Required fields: `id`, `name`, `description`, `zone`, `exits`
- Optional fields: `field1`, `field2`, `field3` (ignore these)
- Exit directions: `north`, `south`, `east`, `west`, `up`, `down`
- Exit values: either string/null or object with `target` and `flags`
- Data types and constraints

## Core Implementation Requirements

### 1. Room Loader (core/room_loader.py)

**Functionality:**

- Recursively scan `./data/rooms/` directory for all `.json` files
- Parse JSON files with error handling for malformed files
- Build room database indexed by room ID
- Support progress indicators for large datasets
- Log parsing errors but continue processing other files

**Key Methods:**

- `discover_room_files(base_path)` - Find all JSON files in subdirectories
- `load_room_data(file_path)` - Parse single room file with error handling
- `build_room_database(base_path)` - Create complete room index
- `get_zones()` - Return list of discovered zones

### 2. Schema Validator (core/schema_validator.py)

**Functionality:**

- Load and cache JSON schema
- Validate individual room files against schema
- Support both legacy and new exit formats
- Provide detailed validation error messages

**Key Methods:**

- `load_schema()` - Load room schema from file
- `validate_room(room_data, file_path)` - Validate single room
- `normalize_exits(room_data)` - Convert legacy format to new format internally

### 3. Path Validator (core/path_validator.py)

**Functionality:**

- Build room connectivity graph
- Perform graph traversal algorithms
- Check bidirectional connections (respecting one_way flags)
- Find unreachable rooms from starting point (earth_arkhamcity_intersection_derby_high)
- Detect dead ends (rooms with no exits)

**Key Methods:**

- `build_graph(room_database)` - Create adjacency graph
- `find_unreachable_rooms(start_room_id)` - BFS/DFS from starting room
- `check_bidirectional_connections(room_database)` - Verify return paths
- `find_dead_ends(room_database)` - Identify rooms with no exits

### 4. Reporter (core/reporter.py)

**Functionality:**

- Format validation results with colors
- Generate actionable error messages with suggestions
- Provide summary statistics
- Support multiple output formats (console, JSON)

**Key Methods:**

- `format_error(error_type, room_id, message, suggestion)` - Format single error
- `format_warning(warning_type, room_id, message)` - Format warning
- `print_summary(stats)` - Display validation summary
- `colorize_output(text, color)` - Apply terminal colors

## Validation Rules Implementation

### Base Rule Class (rules/base_rule.py)

Create abstract base class for all validation rules:

```python
from abc import ABC, abstractmethod

class ValidationRule(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def validate(self, room_database, zone_filter=None):
        """Return list of ValidationError objects"""
        pass
```

### Validation Rules to Implement

#### Structure Rules (rules/structure_rules.py)

1. **Schema Validation Rule**
   - Validate each room against JSON schema
   - Report file path and specific schema violations

2. **Duplicate ID Rule**
   - Check for duplicate room IDs across zones
   - Flag naming convention violations (e.g., `earth_arkhamcity_intersection_derby_high` in `dungeon` zone)

3. **Exit Reference Rule**
   - Verify all exit targets exist or are null
   - Handle both string and object exit formats

#### Connectivity Rules (rules/connectivity_rules.py)

1. **Bidirectional Connection Rule**
   - Check that room A → room B implies room B → room A
   - Respect `one_way` flag to skip bidirectional check
   - Provide suggestions for adding missing return paths

2. **Unreachable Room Rule**
   - Use graph traversal from `earth_arkhamcity_intersection_derby_high` as starting point
   - Report rooms that cannot be reached
   - Suggest connection points

3. **Dead End Rule**
   - Find rooms with zero exits
   - Generate warnings (not errors) for rooms with only one exit

4. **Self Reference Rule**
   - Detect rooms that reference themselves
   - Allow if `self_reference` flag is present
   - Report as error otherwise

## Command Line Interface (validator.py)

### CLI Arguments

Use Click framework for command-line interface:

```python
@click.command()
@click.option('--zone', help='Validate specific zone only')
@click.option('--verbose', '-v', is_flag=True, help='Detailed output')
@click.option('--schema-only', is_flag=True, help='Only validate JSON schema')
@click.option('--ignore', help='Comma-separated list of rule types to ignore')
@click.option('--format', type=click.Choice(['console', 'json']), default='console')
@click.option('--base-path', default='./data/rooms', help='Base directory for room files')
def main(zone, verbose, schema_only, ignore, format, base_path):
    # Implementation here
```

### Validation Flow

1. **Discovery Phase**
   - Scan directory structure
   - Report zones found
   - Show progress for large datasets

2. **Loading Phase**
   - Parse all JSON files
   - Build room database
   - Report parsing errors

3. **Validation Phase**
   - Run enabled validation rules
   - Collect errors and warnings
   - Respect zone filters and ignore flags

4. **Reporting Phase**
   - Format and display results
   - Show summary statistics
   - Return appropriate exit code

## Sample Output Format

### Console Output

```
🔍 Room Validator v1.0
📁 Scanning ./data/rooms/...

✅ arkham zone: 7 rooms discovered
⚠️  dungeon zone: 0 rooms (empty zone)

🔄 Processing rooms... ████████████████████ 100% (7/7)

❌ ERRORS FOUND:

🏠 arkham_002.json (Miskatonic University Gates)
  ❌ Bidirectional: Exit 'south' → earth_arkhamcity_intersection_derby_high, but earth_arkhamcity_intersection_derby_high has no 'north' return
     💡 Suggestion: Add "north": "arkham_002" to earth_arkhamcity_intersection_derby_high or flag as one_way

🏠 arkham_006.json (Clock Tower)
  ❌ Unreachable: No path from starting room earth_arkhamcity_intersection_derby_high
     💡 Suggestion: Add connection from earth_arkhamcity_intersection_derby_high or another reachable room

⚠️  WARNINGS:
🏠 arkham_007.json (Underground Tunnels)
  ⚠️  Potential dead end: Only one exit (up)

📊 SUMMARY:
  Zones: 2 (1 populated, 1 empty)
  Rooms: 7 total
  Errors: 2 🔴
  Warnings: 1 🟡

❌ Validation failed - please fix errors above
```

### JSON Output Format

```json
{
  "summary": {
    "zones": 2,
    "rooms": 7,
    "errors": 2,
    "warnings": 1,
    "success": false
  },
  "errors": [
    {
      "type": "bidirectional",
      "file": "arkham_002.json",
      "room_id": "arkham_002",
      "message": "Exit 'south' → earth_arkhamcity_intersection_derby_high, but earth_arkhamcity_intersection_derby_high has no 'north' return",
      "suggestion": "Add \"north\": \"arkham_002\" to earth_arkhamcity_intersection_derby_high or flag as one_way"
    }
  ],
  "warnings": [
    {
      "type": "potential_dead_end",
      "file": "arkham_007.json",
      "room_id": "arkham_007",
      "message": "Only one exit (up)"
    }
  ]
}
```

## Implementation Notes

### Error Handling

- Continue processing after malformed JSON files
- Provide specific file paths in all error messages
- Use try-catch blocks around file operations
- Log but don't crash on unexpected errors

### Performance Considerations

- Use progress bars for operations > 1 second
- Lazy load room data when possible
- Efficient graph algorithms (BFS/DFS)
- Cache schema validation results

### Extensibility Design

- Plugin-style rule system
- Easy to add new validation rules
- Support for zone-specific rules in future
- Configuration file support for ignored rules

### Testing Strategy

Create test cases for:

- Valid room configurations
- Various error conditions
- Edge cases (empty zones, self-references, cycles)
- Command-line argument combinations
- Large dataset performance

## Migration Support

The validator must support gradual migration from legacy string exits to new object exits with flags. Always maintain backward compatibility while encouraging adoption of the new format in suggestions.
