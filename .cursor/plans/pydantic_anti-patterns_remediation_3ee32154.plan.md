---
name: Pydantic Anti-Patterns Remediation
overview: "Comprehensive remediation plan to address Pydantic v2 anti-patterns, semantic errors, and code quality violations identified across the codebase. Focus areas include: replacing old-style dict model_config in BaseSettings classes, eliminating unsafe dict[str, Any] types in model fields, ensuring consistent ConfigDict usage, and improving type safety throughout."
todos:
  - id: phase1-basesettings
    content: Update all 11 BaseSettings classes in server/config/models.py to use SettingsConfigDict instead of old-style dict syntax
    status: completed
  - id: phase2-weapon-stats
    content: Create WeaponStats typed model and update InventoryItem.weapon field in server/models/game.py
    status: completed
  - id: phase2-class-definitions
    content: Create ClassDefinition typed model and update AvailableClassesResponse.classes field
    status: completed
  - id: phase2-stats-dicts
    content: Create StatValues typed model and update stats fields in character_creation.py
    status: completed
  - id: phase2-room-data
    content: Create RoomData typed model and update room fields in room.py and player_respawn.py
    status: completed
  - id: phase2-container-data
    content: Create ContainerData and verify InventoryStack models, update container.py fields
    status: completed
  - id: phase2-metrics-data
    content: Create metrics typed models and update metrics.py fields
    status: completed
  - id: phase2-realtime-data
    content: Create PresenceData and HealthData models and update realtime.py fields
    status: completed
  - id: phase2-admin-data
    content: Create AdminSession and AuditLogEntry models and update npc_admin.py fields
    status: completed
  - id: phase2-target-metadata
    content: Create TargetMetadata model and update target_resolution.py
    status: completed
  - id: phase2-broadcast-stats
    content: Create BroadcastStatsDetail model and update game.py
    status: completed
  - id: phase3-auth-schemas
    content: Update auth schemas (user.py, invite.py) to use SecureBaseModel or add security ConfigDict
    status: completed
  - id: phase3-target-resolution
    content: Add ConfigDict to TargetMatch and TargetResolutionResult models
    status: completed
  - id: phase3-calendar-schemas
    content: Review and ensure calendar schemas have proper ConfigDict settings
    status: completed
isProject: false
---

# Pydantic Anti-Patterns Remediation Plan

## Analysis Summary

Analysis of the codebase against `.cursor/rules/pydantic.mdc` revealed several categories of violations:

1. **Old-style dictionary `model_config` in BaseSettings** (Rule 5 violation)
2. **Extensive `dict[str, Any]` usage in model fields** (Rule 2 violation - Strict Typing)
3. **Missing or incomplete `ConfigDict` in some models** (Rule 1 violation)
4. **Code quality concerns** (complex validation logic in `Stats` model)

## Findings by Category

### Category 1: BaseSettings Configuration (CRITICAL)

**Violation**: All `pydantic_settings.BaseSettings` classes use old-style dictionary syntax instead of `SettingsConfigDict` or `ConfigDict`.

**Files Affected**: `server/config/models.py` (11 classes)

- `ServerConfig` (line 73)
- `DatabaseConfig` (line 153)
- `NATSConfig` (line 257)
- `SecurityConfig` (line 280)
- `LoggingConfig` (line 326)
- `GameConfig` (line 451)
- `ChatConfig` (line 488)
- `TimeConfig` (line 517)
- `CORSConfig` (line 577)
- `PlayerStatsConfig` (line 781)
- `AppConfig` (line 826)

**Current Pattern**:

```python
model_config = {"env_prefix": "SERVER_", "case_sensitive": False, "extra": "ignore"}
```

**Required Pattern**:

```python
from pydantic_settings import SettingsConfigDict

model_config = SettingsConfigDict(
    env_prefix="SERVER_",
    case_sensitive=False,
    extra="ignore"
)
```

### Category 2: Unsafe `dict[str, Any]` Types in Model Fields (CRITICAL)

**Violation**: Multiple Pydantic models use `dict[str, Any]` as field types, violating strict typing requirements.

**Files and Models Affected**:

1. `**server/models/game.py**`:

- `InventoryItem.weapon: dict[str, Any] | None` (line 262)

1. `**server/schemas/players/player.py**`:

- `AvailableClassesResponse.classes: dict[str, dict[str, Any]]` (line 174)

1. `**server/schemas/players/character_creation.py**`:

- `RollStatsResponse.stats: dict[str, Any]` (line 27)
- `ValidateStatsResponse.stat_summary: dict[str, Any] | None` (line 75)

1. `**server/schemas/shared/target_resolution.py**`:

- `TargetResolutionResult.metadata: dict[str, Any]` (line 37)

1. `**server/schemas/game/game.py**`:

- `BroadcastStats.broadcast_stats: dict[str, Any]` (line 49)

1. `**server/schemas/rooms/room.py**`:

- `RoomListResponse.rooms: list[dict[str, Any]]` (line 20)

1. `**server/schemas/containers/container.py**`:

- `ContainerOpenResponse.container: dict[str, Any]` (line 19)
- `ContainerTransferResponse.container: dict[str, Any]` (line 40)
- `ContainerTransferResponse.player_inventory: list[dict[str, Any]]` (line 41)
- `ContainerLootAllResponse.container: dict[str, Any]` (line 81)
- `ContainerLootAllResponse.player_inventory: list[dict[str, Any]]` (line 82)

1. `**server/schemas/metrics/metrics.py**`:

- `MetricsResponse.metrics: dict[str, Any]` (line 16)
- `MetricsSummaryResponse.summary: dict[str, Any]` (line 36)
- `DLQMessagesResponse.messages: list[dict[str, Any]]` (line 70)

1. `**server/schemas/players/player_respawn.py**`:

- `RespawnPlayerData.room: dict[str, Any]` (line 29)

1. `**server/schemas/admin/npc_admin.py**`:

- `AdminSessionsResponse.sessions: list[dict[str, Any]]` (line 134)
  - `AdminAuditLogResponse.audit_log: list[dict[str, Any]]` (line 150)

1. `**server/schemas/realtime/realtime.py**`:

- `PresenceInfo.presence: dict[str, Any]` (line 72)
  - `HealthInfo.health: dict[str, Any]` (line 74)
  - `ConnectionStatisticsResponse.presence: dict[str, Any]` (line 117)
  - `ConnectionStatisticsResponse.sessions: dict[str, Any]` (line 118)
  - `ConnectionStatisticsResponse.errors: dict[str, Any]` (line 119)

**Remediation Strategy**: Create typed Pydantic models for each `dict[str, Any]` usage:

- `WeaponStats` model for `InventoryItem.weapon`
- `ClassDefinition` model for `AvailableClassesResponse.classes`
- `StatValues` model for stats dictionaries
- `RoomData` model for room dictionaries
- `ContainerData` model for container dictionaries
- `InventoryStack` model (may already exist) for inventory items
- `MetricsData` model for metrics dictionaries
- `PresenceData` and `HealthData` models for realtime schemas
- `AdminSession` and `AuditLogEntry` models for admin schemas

### Category 3: Missing or Incomplete ConfigDict

**Violation**: Some models inherit from `BaseModel` directly without explicit `model_config`, relying on defaults or inheritance.

**Files Affected**:

- `server/schemas/auth/user.py`: `UserBase` (line 14), `UserUpdate` (line 70) - have `ConfigDict` but only for `json_schema_extra`, missing security settings
- `server/schemas/auth/invite.py`: `InviteBase` (line 13), `InviteUpdate` (line 61) - same issue
- `server/schemas/shared/target_resolution.py`: `TargetMatch` (line 22), `TargetResolutionResult` (line 40) - no `model_config`
- `server/schemas/calendar/calendar.py`: Multiple models may be missing security `ConfigDict`

**Remediation Strategy**: Ensure all models either:

1. Inherit from `SecureBaseModel` or `ResponseBaseModel` (preferred)
2. Or explicitly define `model_config = ConfigDict(...)` with security settings

### Category 4: Code Quality Concerns

**Violation**: Complex validation logic in `Stats` model using `__init__` override and `object.__setattr__` to bypass validation.

**File**: `server/models/game.py` - `Stats` class (lines 122-164, 188-211)

**Note**: This is a code quality issue rather than a strict Pydantic anti-pattern. The current implementation works but could be simplified using proper `@model_validator` patterns.

## Remediation Tasks

### Phase 1: BaseSettings Configuration (Priority: CRITICAL)

**Task 1.1**: Update all BaseSettings classes to use `SettingsConfigDict`

- File: `server/config/models.py`
- Replace 11 instances of old-style dict `model_config` with `SettingsConfigDict`
- Import: `from pydantic_settings import SettingsConfigDict`
- Estimated effort: 1 hour

### Phase 2: Replace dict[str, Any] in Model Fields (Priority: CRITICAL)

**Task 2.1**: Create typed models for weapon stats

- Create `server/schemas/game/weapon.py` with `WeaponStats` model
- Update `server/models/game.py` - `InventoryItem.weapon` field
- Estimated effort: 2 hours

**Task 2.2**: Create typed models for class definitions

- Create `server/schemas/players/class_definition.py` with `ClassDefinition` model
- Update `server/schemas/players/player.py` - `AvailableClassesResponse.classes` field
- Estimated effort: 2 hours

**Task 2.3**: Create typed models for stats dictionaries

- Create `server/schemas/players/stat_values.py` with `StatValues` model
- Update `server/schemas/players/character_creation.py` - stats fields
- Estimated effort: 2 hours

**Task 2.4**: Create typed models for room data

- Create `server/schemas/rooms/room_data.py` with `RoomData` model
- Update `server/schemas/rooms/room.py` - `RoomListResponse.rooms` field
- Update `server/schemas/players/player_respawn.py` - `RespawnPlayerData.room` field
- Estimated effort: 3 hours

**Task 2.5**: Create typed models for container data

- Verify if `InventoryStack` model exists in `server/schemas/` or `server/models/`
- Create `server/schemas/containers/container_data.py` with `ContainerData` model
- Update `server/schemas/containers/container.py` - container and inventory fields
- Estimated effort: 4 hours

**Task 2.6**: Create typed models for metrics data

- Create `server/schemas/metrics/metrics_data.py` with metrics models
- Update `server/schemas/metrics/metrics.py` - metrics and summary fields
- Estimated effort: 3 hours

**Task 2.7**: Create typed models for realtime schemas

- Create `server/schemas/realtime/presence_data.py` with `PresenceData` and `HealthData` models
- Update `server/schemas/realtime/realtime.py` - presence and health fields
- Estimated effort: 2 hours

**Task 2.8**: Create typed models for admin schemas

- Create `server/schemas/admin/admin_data.py` with `AdminSession` and `AuditLogEntry` models
- Update `server/schemas/admin/npc_admin.py` - sessions and audit_log fields
- Estimated effort: 2 hours

**Task 2.9**: Create typed model for target resolution metadata

- Update `server/schemas/shared/target_resolution.py` - create `TargetMetadata` model
- Update `TargetResolutionResult.metadata` field
- Estimated effort: 1 hour

**Task 2.10**: Create typed model for broadcast stats

- Update `server/schemas/game/game.py` - create `BroadcastStatsDetail` model
- Update `BroadcastStats.broadcast_stats` field
- Estimated effort: 1 hour

### Phase 3: Ensure Consistent ConfigDict Usage (Priority: HIGH)

**Task 3.1**: Update auth schemas to inherit from SecureBaseModel

- Update `server/schemas/auth/user.py` - `UserBase`, `UserUpdate`
- Update `server/schemas/auth/invite.py` - `InviteBase`, `InviteUpdate`
- Add security `ConfigDict` settings or inherit from `SecureBaseModel`
- Estimated effort: 1 hour

**Task 3.2**: Add ConfigDict to target resolution schemas

- Update `server/schemas/shared/target_resolution.py` - add `ConfigDict` to `TargetMatch` and `TargetResolutionResult`
- Estimated effort: 30 minutes

**Task 3.3**: Review and update calendar schemas

- Review `server/schemas/calendar/calendar.py` - ensure all models have proper `ConfigDict`
- Estimated effort: 1 hour

### Phase 4: Code Quality Improvements (Priority: MEDIUM)

**Task 4.1**: Refactor Stats model validation logic

- Review `server/models/game.py` - `Stats` class
- Consider simplifying `__init__` and `@model_validator` logic
- Document complex validation requirements
- Estimated effort: 3 hours (optional, can be deferred)

## Implementation Notes

1. **Backward Compatibility**: When replacing `dict[str, Any]` with typed models, ensure:

- Existing serialization/deserialization continues to work
- Database persistence layers handle the new types correctly
- API responses maintain the same structure (may require `model_dump()` calls)

1. **Testing Requirements**: Each remediation task should include:

- Unit tests for new typed models
- Integration tests for affected API endpoints
- Validation that existing functionality remains intact

1. **Migration Strategy**: For `dict[str, Any]` replacements:

- Create new typed models first
- Update model fields to use new types
- Update all code that constructs/accesses these fields
- Update serialization/deserialization logic if needed
- Run full test suite to verify compatibility

1. **SettingsConfigDict vs ConfigDict**:

- Use `SettingsConfigDict` for `pydantic_settings.BaseSettings` subclasses
- Use `ConfigDict` for regular `BaseModel` subclasses

## Success Criteria

- All BaseSettings classes use `SettingsConfigDict` instead of dict syntax
- Zero `dict[str, Any]` types in Pydantic model field definitions
- All models have explicit `ConfigDict` or inherit from `SecureBaseModel`/`ResponseBaseModel`
- All new typed models follow Pydantic v2 best practices
- All tests pass after remediation
- No breaking changes to API contracts (response structures remain compatible)

## Estimated Total Effort

- Phase 1: 1 hour
- Phase 2: 22 hours
- Phase 3: 2.5 hours
- Phase 4: 3 hours (optional)
- **Total**: ~25.5 hours (28.5 hours with Phase 4)
