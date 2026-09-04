---
name: Pydantic Anti-Patterns Remediation
overview: Remediate Pydantic anti-patterns, semantic issues, and bad code across the codebase based on the Pydantic best practices rules. Focus on mutable defaults, unsafe Any types, missing model configurations, and inconsistent security settings.
todos:

  - id: fix-mutable-defaults

    content: Fix mutable default values in server/schemas/player.py (Field(default=[]) -> Field(default_factory=list))
    status: completed

  - id: standardize-model-config

    content: Convert old dict-style model_config to ConfigDict in server/schemas/nats_messages.py and server/api/admin/npc.py
    status: completed

  - id: add-security-config

    content: Add security model_config (extra=forbid, validate_assignment=True, etc.) to all models missing it
    status: completed

  - id: create-typed-stats-model

    content: Create PlayerStatsModel and replace dict[str, Any] stats in server/schemas/player.py
    status: completed

  - id: replace-inventory-any

    content: Replace list[dict[str, Any]] inventory with list[InventoryItem] in server/schemas/player.py
    status: completed

  - id: replace-status-effects-any

    content: Replace list[dict[str, Any]] status_effects with list[StatusEffect] in server/schemas/player.py
    status: completed

  - id: create-npc-typed-models

    content: Create typed models for NPC base_stats, behavior_config, ai_integration_stub, spawn_conditions in server/api/admin/npc.py
    status: completed

  - id: fix-profession-types

    content: Replace dict[str, Any] with proper types in server/schemas/profession.py ProfessionResponse
    status: completed

  - id: fix-websocket-types

    content: Use CommandMessageData and ChatMessageData instead of dict[str, Any] in server/schemas/websocket_messages.py
    status: completed

  - id: update-tests

    content: Update unit and integration tests to work with new typed models
    status: completed

  - id: run-type-checking

    content: Run mypy to verify type safety after all changes
    status: completed

  - id: verify-validation

    content: Test that extra fields are rejected and validation works correctly
    status: completed

  - id: add-field-validators

    content: Add @field_validator and @model_validator where needed for custom validation logic following Pydantic v2 patterns
    status: completed

  - id: create-base-model-classes

    content: Create SecureBaseModel and ResponseBaseModel base classes with standard security configuration, then refactor existing models to inherit from them
    status: completed

  - id: consolidate-duplicate-patterns

    content: Review validation logic for duplication, extract common validators to shared utilities, and ensure consistent naming conventions
    status: completed
---

# Pydantic Anti-Patterns Remediation Plan

## Executive Summary

This plan addresses Pydantic anti-patterns identified across the codebase, focusing on security vulnerabilities, type safety issues, and code quality problems. The remediation follows the Pydantic v2 best practices defined in `.cursor/rules/pydantic.mdc`.

## Critical Issues Identified

### 1. Mutable Default Values (Rule 3 Violation)

**Location**: `server/schemas/player.py:35-36`

- `Field(default=[])` should be `Field(default_factory=list)`
- `Field(default={...})` should use `default_factory` or proper typed models

**Risk**: Shared mutable state across model instances leading to unexpected behavior.

### 2. Unsafe `dict[str, Any]` Types (Rule 2 Violation)

**Locations**:

- `server/schemas/player.py` - stats, inventory, status_effects (lines 34-36, 65-67, 127-129)
- `server/schemas/nats_messages.py` - event_data (line 62)
- `server/api/admin/npc.py` - base_stats, behavior_config, ai_integration_stub, spawn_conditions (lines 65-67, 77-79, 92-94, 146, 159)
- `server/schemas/profession.py` - stat_requirements, mechanical_effects (lines 84-85)
- `server/schemas/websocket_messages.py` - data fields (lines 29, 45)
- Multiple other schemas using `dict[str, Any]` for structured data

**Risk**: Type confusion attacks, lack of validation, potential security vulnerabilities.

### 3. Old-Style model_config (Rule 1 Violation)

**Locations**:

- `server/schemas/nats_messages.py:35` - Uses dict syntax instead of ConfigDict
- `server/api/admin/npc.py:85, 152` - Uses dict syntax for model_config

**Risk**: Inconsistent patterns, potential deprecation issues.

### 4. Missing Security Configuration

**Locations**: Many models missing:

- `extra="forbid"` - Prevents field injection
- `validate_assignment=True` - Runtime validation
- `str_strip_whitespace=True` - Input sanitization

**Examples**:

- `server/schemas/player.py` - PlayerBase, PlayerCreate, PlayerRead, PlayerUpdate
- `server/schemas/websocket_messages.py` - BaseWebSocketMessage and subclasses
- `server/schemas/profession.py` - All models
- `server/api/admin/npc.py` - NPCDefinitionCreate, NPCDefinitionUpdate, NPCSpawnRequest, NPCMoveRequest

### 5. Missing model_config Entirely

**Locations**: Several models have no configuration:

- `server/schemas/nats_messages.py` - ChatMessageSchema, EventMessageSchema
- Various response models in multiple schema files

## Remediation Strategy

### Phase 1: Critical Security Fixes (High Priority)

#### Task 1.1: Fix Mutable Default Values

**Files**: `server/schemas/player.py`

- Replace `Field(default=[])` with `Field(default_factory=list)` for inventory and status_effects
- Replace `Field(default={...})` with `Field(default_factory=dict)` for stats (or better, use typed model)

#### Task 1.2: Standardize model_config Usage

**Files**:

- `server/schemas/nats_messages.py` - Convert dict syntax to ConfigDict
- `server/api/admin/npc.py` - Convert dict syntax to ConfigDict

**Pattern**:

```python
# OLD (BAD)

model_config = {"extra": "forbid", "strict": True}

# NEW (GOOD)

model_config = ConfigDict(extra="forbid", strict=True)
```

#### Task 1.3: Add Security Configuration to All Models

**Files**: All Pydantic model files

- Add `extra="forbid"` to prevent field injection
- Add `validate_assignment=True` for runtime validation
- Add `str_strip_whitespace=True` for input sanitization
- Add `validate_default=True` to validate default values

**Base Pattern**:

```python
model_config = ConfigDict(
    extra="forbid",
    validate_assignment=True,
    str_strip_whitespace=True,
    validate_default=True,
)
```

### Phase 2: Type Safety Improvements (Medium Priority)

#### Task 2.1: Replace dict[str, Any] with Typed Models

**Priority Order**:

1. **Player Stats** (`server/schemas/player.py`)

   - Create `PlayerStatsModel` based on `server/models/game.py:Stats`
   - Replace `dict[str, Any]` in PlayerCreate, PlayerRead, PlayerUpdate

2. **Inventory Items** (`server/schemas/player.py`)

   - Use existing `InventoryItem` from `server/models/game.py:239`
   - Replace `list[dict[str, Any]]` with `list[InventoryItem]`

3. **Status Effects** (`server/schemas/player.py`)

   - Use existing `StatusEffect` from `server/models/game.py:53`
   - Replace `list[dict[str, Any]]` with `list[StatusEffect]`

4. **NPC Configuration** (`server/api/admin/npc.py`)

   - Create `NPCBaseStatsModel` for base_stats
   - Create `NPCBehaviorConfigModel` for behavior_config
   - Create `NPCAIIntegrationModel` for ai_integration_stub
   - Create `NPCSpawnConditionsModel` for spawn_conditions

5. **Profession Data** (`server/schemas/profession.py`)

   - Already has `StatRequirement` and `MechanicalEffect` models
   - Replace `dict[str, Any]`in `ProfessionResponse` with proper types

6. **NATS Event Data** (`server/schemas/nats_messages.py`)

   - Create typed models for known event types
   - Keep `dict[str, Any]` only for truly dynamic/unknown event structures

7. **WebSocket Message Data** (`server/schemas/websocket_messages.py`)

   - Already has `CommandMessageData` and `ChatMessageData`
   - Use these instead of `dict[str, Any]` in parent classes

#### Task 2.2: Add Field Validators Where Needed

Add `@field_validator` for fields that need custom validation

- Add `@model_validator` for cross-field validation
- Ensure all validators follow Pydantic v2 patterns

### Phase 3: Code Organization (Low Priority)

#### Task 3.1: Create Base Model Classes

Create `SecureBaseModel` with standard security configuration

- Create `ResponseBaseModel` for API response models
- Refactor existing models to inherit from appropriate base classes

#### Task 3.2: Consolidate Duplicate Patterns

Review validation logic for duplication

- Extract common validators to shared utilities
- Ensure consistent naming conventions

## Implementation Details

### File-by-File Changes

#### `server/schemas/player.py`

1. Fix mutable defaults (lines 35-36)
2. Add model_config to PlayerBase, PlayerCreate, PlayerRead, PlayerUpdate
3. Create/import typed models for stats, inventory, status_effects
4. Replace all `dict[str, Any]` with proper types

#### `server/schemas/nats_messages.py`

1. Convert model_config dict to ConfigDict (line 35)
2. Add model_config to ChatMessageSchema, EventMessageSchema
3. Consider typed models for event_data where structure is known

#### `server/api/admin/npc.py`

1. Convert model_config dicts to ConfigDict (lines 85, 152)
2. Add model_config to NPCDefinitionCreate, NPCDefinitionUpdate, NPCSpawnRequest, NPCMoveRequest
3. Create typed models for base_stats, behavior_config, ai_integration_stub, spawn_conditions

#### `server/schemas/profession.py`

1. Add model_config to all models
2. Replace dict[str, Any] in ProfessionResponse with proper types (use existing StatRequirement and MechanicalEffect)

#### `server/schemas/websocket_messages.py`

1. Add model_config with security settings to BaseWebSocketMessage
2. Use CommandMessageData and ChatMessageData instead of dict[str, Any] where possible

#### `server/schemas/calendar.py`

Already follows best practices (uses default_factory correctly)

- Verify model_config is present and secure

#### `server/models/game.py`

Already follows best practices

- Verify all models have proper model_config

#### `server/models/container.py`

Already follows best practices

- No changes needed

#### `server/models/alias.py`

Already follows best practices

- No changes needed

#### `server/models/command_base.py`

Already follows best practices

- No changes needed

## Testing Strategy

1. **Unit Tests**: Update existing tests to work with new typed models
2. **Integration Tests**: Verify API endpoints still work with new schemas
3. **Type Checking**: Run mypy to ensure type safety
4. **Validation Tests**: Test that extra fields are rejected, validation works correctly

## Risk Assessment

**Low Risk**:

- Adding model_config to existing models
- Converting dict syntax to ConfigDict
- Fixing mutable defaults

**Medium Risk**:

- Replacing dict[str, Any] with typed models (may require API changes)
- Adding new validators (may break existing valid data)

**Mitigation**:

- Test thoroughly before deployment
- Consider backward compatibility for API changes
- Document breaking changes

## Success Criteria

1. All models use `default_factory` for mutable defaults
2. All models have proper `model_config` with security settings
3. All `model_config` uses `ConfigDict` instead of dict syntax
4. `dict[str, Any]` replaced with typed models where structure is known
5. All models pass mypy type checking
6. All existing tests pass
7. No security vulnerabilities from field injection
