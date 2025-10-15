# Room Hierarchy Feature Requirements Document

## Overview

This document outlines the requirements for extending the MythosMUD room schema to support a hierarchical world structure with enhanced environmental and zone type classifications. The new system will provide better organization for complex world-building while maintaining backward compatibility.

## Current State Analysis

### Existing Schema

- **Current Structure**: Flat room-based organization with simple zone identifiers
- **File Organization**: `data/local/rooms/{zone}/{zone}_{room_number}.json`
- **Schema Location**: `room_validator/schemas/room_schema.json`
- **Example**: `data/local/rooms/arkham/arkham_001.json`

### Current Limitations

- No support for multi-dimensional world structures
- Limited environmental context
- No zone type classification
- Flat hierarchy doesn't support complex world-building

## Proposed Hierarchical Structure

### 1. Four-Level Hierarchy

```
Plane → Zone → Sub-zone → Room
```

#### Examples

- **Earth → Arkham City → French Hill → S_Garrison_St_001.json**
- **Yeng → Katmandu → palace → palace_Ground_001.json**

### 2. Directory Structure

```
data/local/rooms/
├── earth/
│   ├── arkhamcity/
│   │   ├── french_hill/
│   │   │   ├── S_Garrison_St_001.json
│   │   │   └── S_Garrison_St_002.json
│   │   └── downtown/
│   │       ├── main_street_001.json
│   │       └── library_001.json
│   └── innsmouth/
│       └── waterfront/
│           ├── dock_001.json
│           └── warehouse_001.json
└── yeng/
    └── katmandu/
        └── palace/
            ├── palace_Ground_001.json
            └── palace_Upper_001.json
```

## New Schema Requirements

### 1. Environment Classification

**Applicable Levels**: Zone, Sub-zone, Room

**Values**: `["indoors", "outdoors", "underwater"]`

**Purpose**:

- Determines environmental effects and restrictions
- Affects player abilities and equipment requirements
- Influences atmospheric descriptions and gameplay mechanics

### 2. Zone Type Classification

**Applicable Levels**: Zone only

**Values**: `["city", "countryside", "mountains", "swamp", "tundra", "desert"]`

**Purpose**:

- Provides biome context for gameplay mechanics
- Affects NPC behavior and spawn rates
- Influences weather patterns and environmental hazards

## Schema Extensions

### 1. Room Schema Updates

#### New Required Fields

```json
{
  "plane": "string (required)",
  "zone": "string (required)",
  "sub_zone": "string (required)",
  "environment": "string (required) - enum: [indoors, outdoors, underwater]"
}
```

#### Updated Room ID Format

- **Current**: `arkham_001`
- **New**: `earth_arkhamcity_french_hill_S_Garrison_St_001`

### 2. Zone Configuration Schema (New)

Create `zone_config.json` files at each zone level:

```json
{
  "zone_type": "string (required) - enum: [city, countryside, mountains, swamp, tundra, desert]",
  "environment": "string (required) - enum: [indoors, outdoors, underwater]",
  "description": "string (optional)",
  "weather_patterns": "array (optional)",
  "special_rules": "object (optional)"
}
```

### 3. Sub-zone Configuration Schema (New)

Create `subzone_config.json` files at each sub-zone level:

```json
{
  "environment": "string (required) - enum: [indoors, outdoors, underwater]",
  "description": "string (optional)",
  "special_rules": "object (optional)"
}
```

## Implementation Requirements

### 1. Schema Validation Updates

- Update `room_validator/schemas/room_schema.json`
- Create new schemas for zone and sub-zone configurations
- Implement hierarchical validation rules
- Ensure backward compatibility during migration

### 2. World Loader Updates

- Modify `server/world_loader.py` to support hierarchical loading
- Implement configuration file loading for zones and sub-zones
- Update room ID generation and resolution
- Maintain existing room reference compatibility

### 3. Migration Strategy

#### Phase 1: Schema Preparation

- Create new schemas with backward compatibility
- Update validation rules
- Create migration utilities

#### Phase 2: Data Migration

- Convert existing room files to new format
- Create zone and sub-zone configuration files
- Update room IDs and references
- Validate all data integrity

#### Phase 3: Code Updates

- Update world loader implementation
- Modify room reference resolution
- Update any hardcoded room ID patterns

### 4. Backward Compatibility

- Maintain support for existing room ID format during transition
- Provide migration utilities for existing room files
- Ensure existing room references continue to work
- Support both old and new formats during transition period

## Technical Specifications

### 1. File Naming Conventions

#### Room Files

- **Format**: `{descriptive_name}_{room_number}.json`
- **Example**: `S_Garrison_St_001.json`, `library_main_001.json`

#### Configuration Files

- **Zone**: `zone_config.json`
- **Sub-zone**: `subzone_config.json`

### 2. ID Generation Rules

#### Room IDs

- **Format**: `{plane}_{zone}_{sub_zone}_{room_file_name}`
- **Example**: `earth_arkhamcity_french_hill_S_Garrison_St_001`

#### Validation Rules

- All components must match `^[a-zA-Z0-9_]+$` pattern
- No duplicate room IDs across the entire world
- Case-sensitive matching

### 3. Environment Inheritance

#### Priority Order (highest to lowest)

1. Room-level environment setting
2. Sub-zone environment setting
3. Zone environment setting

#### Default Values

- **Zone**: `outdoors` (default for most zones)
- **Sub-zone**: Inherits from zone
- **Room**: Inherits from sub-zone

## Testing Requirements

### 1. Schema Validation Tests

- Test new hierarchical schema validation
- Verify backward compatibility
- Test environment inheritance rules
- Validate zone type restrictions

### 2. World Loader Tests

- Test hierarchical room loading
- Verify configuration file loading
- Test room ID resolution
- Validate backward compatibility

### 3. Migration Tests

- Test room file migration utilities
- Verify data integrity after migration
- Test room reference updates
- Validate configuration file generation

## Success Criteria

### 1. Functional Requirements

- [ ] All existing rooms can be migrated to new format
- [ ] New hierarchical structure supports all planned world locations
- [ ] Environment flags work correctly with inheritance
- [ ] Zone types are properly classified and validated
- [ ] Room ID resolution works for both old and new formats

### 2. Performance Requirements

- [ ] World loading performance remains within acceptable limits
- [ ] Room lookup performance is not degraded
- [ ] Memory usage remains reasonable for large worlds

### 3. Quality Requirements

- [ ] All existing tests continue to pass
- [ ] New tests achieve minimum 80% code coverage
- [ ] Schema validation catches all invalid configurations
- [ ] Migration utilities handle edge cases gracefully

## Risks and Mitigation

### 1. Migration Complexity

- **Risk**: Complex migration process may introduce data corruption
- **Mitigation**: Comprehensive testing and validation utilities

### 2. Performance Impact

- **Risk**: Hierarchical loading may impact performance
- **Mitigation**: Optimize loading algorithms and implement caching

### 3. Backward Compatibility

- **Risk**: Breaking changes may affect existing functionality
- **Mitigation**: Maintain dual-format support during transition

## Future Considerations

### 1. Additional Environment Types

- Consider expanding environment types (e.g., "underground", "aerial")
- Plan for custom environment types per plane

### 2. Advanced Zone Types

- Consider biome subtypes (e.g., "coastal_city", "mountain_peak")
- Plan for custom zone types per plane

### 3. Cross-Plane Travel

- Plan for inter-planar connections and travel mechanics
- Consider plane-specific rules and restrictions

---

*This document will be updated as requirements evolve and implementation progresses.*
