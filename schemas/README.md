# Shared JSON Schemas for MythosMUD

This directory contains shared JSON schema definitions that are used by both the room validator tool and the server for validating room data.

## Overview

The schemas provide consistent validation of room definition files across the entire MythosMUD project, ensuring data integrity and preventing runtime errors.

## Schema Files

### `room_schema.json`
Schema for validating regular room definitions. Enforces:
- Required fields: `id`, `name`, `description`, `plane`, `zone`, `sub_zone`, `exits`
- Room ID pattern: `{plane}_{zone}_{sub_zone}_room_{street}_{number:03d}`
- Field length limits and data types
- Exit structure validation

### `intersection_schema.json`
Schema for validating intersection room definitions. Similar to room schema but with:
- Intersection ID pattern: `{plane}_{zone}_{sub_zone}_intersection_{street_a}_{street_b}`

### `unified_room_schema.json`
Master schema that validates both room types using conditional logic based on the `id` field pattern.

## Usage

### In Server Code

```python
from schemas.validator import create_validator

# Create a validator with the unified schema
validator = create_validator("unified")

# Validate room data
errors = validator.validate_room(room_data, "room_file.json")
if errors:
    print(f"Validation errors: {errors}")
```

### In Room Validator

The room validator automatically uses the shared schemas when available, falling back to its own implementation if not.

### Configuration

The server supports schema validation configuration in `server_config.yaml`:

```yaml
room_validation:
  enable_schema_validation: true  # Enable JSON schema validation
  strict_validation: false        # Fail on validation errors
  log_validation_errors: true     # Log errors to console
```

## Benefits

1. **Consistency**: Both server and validator use identical validation rules
2. **Runtime Safety**: Server validates room data during startup
3. **Development**: Better error messages and IDE support
4. **Maintainability**: Single source of truth for room structure

## Dependencies

- `jsonschema>=4.21.0` - Required for schema validation
- The schemas package is optional - systems will work without it but without validation

## Integration Status

- ✅ Shared schema files created
- ✅ Server integration with validation options
- ✅ Room validator integration with fallback
- ✅ Configuration options added
- ✅ Dependencies updated
