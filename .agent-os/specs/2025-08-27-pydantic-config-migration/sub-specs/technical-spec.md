# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-08-27-pydantic-config-migration/spec.md

## Technical Requirements

**Import Statement Update**: Add `ConfigDict` to the import statement in `server/models/health.py`

**Configuration Migration**: Replace `class Config:` with `model_config = ConfigDict()` in the `HealthResponse` model

**Schema Preservation**: Maintain the exact same `json_schema_extra` configuration in the new format
- **Pattern Consistency**: Follow the same pattern already established in `server/schemas/` files
- **Backward Compatibility**: Ensure no breaking changes to model behavior or API responses

## Implementation Details

### Current Pattern (Deprecated)

```python
class HealthResponse(BaseModel):
    # ... fields ...

    class Config:
        json_schema_extra = {
            "example": { ... }
        }
```

### Target Pattern (Modern)

```python
class HealthResponse(BaseModel):
    # ... fields ...

    model_config = ConfigDict(
        json_schema_extra={
            "example": { ... }
        }
    )
```

### Required Changes

1. **File**: `server/models/health.py`

   **Line 8**: Update import to include `ConfigDict`

   **Line 68-85**: Replace `class Config:` with `model_config = ConfigDict()`
   - **Line 70**: Move `json_schema_extra` configuration to `ConfigDict` parameters

### Validation Requirements

All existing tests must continue to pass

- No deprecation warnings should appear during test execution
- Model serialization/deserialization behavior must remain identical
- API responses must maintain the same structure and validation rules
