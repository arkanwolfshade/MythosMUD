# Room Hierarchy Implementation Planning

## Overview

This document serves as the implementation roadmap for the Room Hierarchy feature outlined in `ROOM_HIERARCHY_FRD.md`. It provides detailed technical specifications, implementation steps, and development guidelines for extending the MythosMUD room system.

## Implementation Phases

### Phase 1: Schema Foundation (Priority: High)

#### 1.1 Create New Schema Files

**Location**: `room_validator/schemas/`

**Files to Create**:

- `zone_schema.json` - Zone configuration validation
- `subzone_schema.json` - Sub-zone configuration validation
- `room_hierarchy_schema.json` - Updated room schema with hierarchy

#### 1.2 Update Existing Room Schema

**File**: `room_validator/schemas/room_schema.json`

**Changes Required**:

- Add new required fields: `plane`, `zone`, `sub_zone`, `environment`
- Update room ID pattern to support hierarchical format
- Maintain backward compatibility with existing room format
- Add validation for environment inheritance

#### 1.3 Schema Validation Rules

**Environment Validation**:

```json
{
  "environment": {
    "type": "string",
    "enum": ["indoors", "outdoors", "underwater"],
    "description": "Environmental classification for this room"
  }
}
```

**Zone Type Validation**:

```json
{
  "zone_type": {
    "type": "string",
    "enum": ["city", "countryside", "mountains", "swamp", "tundra", "desert"],
    "description": "Biome classification for this zone"
  }
}
```

### Phase 2: Directory Structure Setup (Priority: High)

#### 2.1 Create New Directory Structure

**Base Path**: `data/rooms/`

**New Structure**:

```
data/rooms/
├── earth/
│   ├── arkham_city/
│   │   ├── zone_config.json
│   │   ├── french_hill/
│   │   │   ├── subzone_config.json
│   │   │   └── S_Garrison_St_001.json
│   │   └── downtown/
│   │       ├── subzone_config.json
│   │       └── main_street_001.json
│   └── innsmouth/
│       ├── zone_config.json
│       └── waterfront/
│           ├── subzone_config.json
│           └── dock_001.json
└── yeng/
    └── katmandu/
        ├── zone_config.json
        └── palace/
            ├── subzone_config.json
            └── palace_Ground_001.json
```

#### 2.2 Configuration File Templates

**Zone Configuration Template** (`zone_config.json`):

```json
{
  "zone_type": "city",
  "environment": "outdoors",
  "description": "A bustling urban area with eldritch undertones",
  "weather_patterns": ["fog", "rain", "overcast"],
  "special_rules": {
    "sanity_drain_rate": 0.1,
    "npc_spawn_modifier": 1.2
  }
}
```

**Sub-zone Configuration Template** (`subzone_config.json`):

```json
{
  "environment": "outdoors",
  "description": "A residential district with Victorian architecture",
  "special_rules": {
    "sanity_drain_rate": 0.05,
    "npc_spawn_modifier": 0.8
  }
}
```

### Phase 3: World Loader Updates (Priority: High)

#### 3.1 Update World Loader Module

**File**: `server/world_loader.py`

**New Functions Required**:

- `load_hierarchical_world()` - Main loading function
- `load_zone_config(zone_path)` - Load zone configuration
- `load_subzone_config(subzone_path)` - Load sub-zone configuration
- `generate_room_id(plane, zone, sub_zone, room_file)` - Generate hierarchical room IDs
- `resolve_room_reference(room_id)` - Resolve room references (both old and new formats)

#### 3.2 Room ID Resolution Logic

**Old Format Support**:

- Pattern: `{zone}_{room_number}`
- Example: `arkham_001`
- Resolution: Map to new hierarchical format

**New Format Support**:

- Pattern: `{plane}_{zone}_{sub_zone}_{room_file_name}`
- Example: `earth_arkham_city_french_hill_S_Garrison_St_001`
- Direct resolution from hierarchical structure

#### 3.3 Environment Inheritance Implementation

**Priority Chain**:

1. Room-level environment setting
2. Sub-zone environment setting (from `subzone_config.json`)
3. Zone environment setting (from `zone_config.json`)
4. Default: `outdoors`

**Implementation**:

```python
def get_room_environment(room_data, subzone_config, zone_config):
    """Determine room environment using inheritance chain."""
    if room_data.get('environment'):
        return room_data['environment']
    elif subzone_config.get('environment'):
        return subzone_config['environment']
    elif zone_config.get('environment'):
        return zone_config['environment']
    return 'outdoors'  # Default fallback
```

### Phase 4: Migration Utilities (Priority: Medium)

#### 4.1 Migration Script

**File**: `scripts/migrate_rooms.py`

**Functions**:

- `migrate_existing_rooms()` - Convert existing room files
- `create_zone_configs()` - Generate zone configuration files
- `create_subzone_configs()` - Generate sub-zone configuration files
- `update_room_references()` - Update exit references to new format
- `validate_migration()` - Verify migration integrity

#### 4.2 Migration Strategy

**Step 1**: Create new directory structure
**Step 2**: Generate configuration files with defaults
**Step 3**: Migrate existing room files
**Step 4**: Update room references and exits
**Step 5**: Validate all data integrity

#### 4.3 Backup and Rollback

**Backup Strategy**:

- Create timestamped backup of existing room structure
- Store original room files in `data/rooms/backup_{timestamp}/`
- Maintain mapping between old and new room IDs

**Rollback Plan**:

- Restore from backup if migration fails
- Maintain dual-format support during transition
- Provide rollback script for emergency situations

### Phase 5: Testing Framework (Priority: High)

#### 5.1 Schema Validation Tests

**File**: `room_validator/tests/test_hierarchical_schema.py`

**Test Cases**:

- Valid hierarchical room structure
- Environment inheritance validation
- Zone type validation
- Backward compatibility with old format
- Invalid configuration detection

#### 5.2 World Loader Tests

**File**: `server/tests/test_world_loader_hierarchy.py`

**Test Cases**:

- Hierarchical world loading
- Configuration file loading
- Room ID resolution (both formats)
- Environment inheritance
- Performance benchmarks

#### 5.3 Migration Tests

**File**: `scripts/tests/test_migration.py`

**Test Cases**:

- Room file migration
- Configuration file generation
- Reference updating
- Data integrity validation
- Rollback functionality

### Phase 6: Documentation Updates (Priority: Medium)

#### 6.1 Update Existing Documentation

**Files to Update**:

- `README.md` - Add hierarchical structure explanation
- `DEVELOPMENT.md` - Update development guidelines
- `docs/PRD.md` - Update product requirements

#### 6.2 Create New Documentation

**Files to Create**:

- `docs/ROOM_HIERARCHY_GUIDE.md` - User guide for room creation
- `docs/MIGRATION_GUIDE.md` - Step-by-step migration instructions
- `docs/SCHEMA_REFERENCE.md` - Complete schema documentation

## Technical Implementation Details

### Room ID Generation Algorithm

```python
def generate_room_id(plane: str, zone: str, sub_zone: str, room_file: str) -> str:
    """
    Generate hierarchical room ID from components.

    Args:
        plane: Plane identifier (e.g., 'earth', 'yeng')
        zone: Zone identifier (e.g., 'arkham_city')
        sub_zone: Sub-zone identifier (e.g., 'french_hill')
        room_file: Room file name without extension (e.g., 'S_Garrison_St_001')

    Returns:
        Hierarchical room ID (e.g., 'earth_arkham_city_french_hill_S_Garrison_St_001')
    """
    components = [plane, zone, sub_zone, room_file]
    return '_'.join(components)
```

### Environment Inheritance Algorithm

```python
def resolve_environment(room_path: str, world_config: dict) -> str:
    """
    Resolve room environment using inheritance chain.

    Args:
        room_path: Path to room file
        world_config: Loaded world configuration

    Returns:
        Resolved environment string
    """
    # Extract hierarchy from path
    path_parts = room_path.split('/')
    plane = path_parts[-4]  # data/rooms/earth/arkham_city/french_hill/room.json
    zone = path_parts[-3]
    sub_zone = path_parts[-2]

    # Check inheritance chain
    if room_data.get('environment'):
        return room_data['environment']

    subzone_config = world_config.get(f"{plane}/{zone}/{sub_zone}")
    if subzone_config and subzone_config.get('environment'):
        return subzone_config['environment']

    zone_config = world_config.get(f"{plane}/{zone}")
    if zone_config and zone_config.get('environment'):
        return zone_config['environment']

    return 'outdoors'  # Default
```

### Configuration Loading Strategy

```python
def load_world_configuration(base_path: str) -> dict:
    """
    Load all zone and sub-zone configurations.

    Args:
        base_path: Base path to rooms directory

    Returns:
        Dictionary of all configurations indexed by path
    """
    configs = {}

    for plane_dir in os.listdir(base_path):
        plane_path = os.path.join(base_path, plane_dir)
        if not os.path.isdir(plane_path):
            continue

        for zone_dir in os.listdir(plane_path):
            zone_path = os.path.join(plane_path, zone_dir)
            if not os.path.isdir(zone_path):
                continue

            # Load zone config
            zone_config_path = os.path.join(zone_path, 'zone_config.json')
            if os.path.exists(zone_config_path):
                with open(zone_config_path, 'r') as f:
                    configs[f"{plane_dir}/{zone_dir}"] = json.load(f)

            # Load sub-zone configs
            for subzone_dir in os.listdir(zone_path):
                subzone_path = os.path.join(zone_path, subzone_dir)
                if not os.path.isdir(subzone_path):
                    continue

                subzone_config_path = os.path.join(subzone_path, 'subzone_config.json')
                if os.path.exists(subzone_config_path):
                    with open(subzone_config_path, 'r') as f:
                        configs[f"{plane_dir}/{zone_dir}/{subzone_dir}"] = json.load(f)

    return configs
```

## Development Guidelines

### Code Quality Standards

1. **Type Hints**: Use comprehensive type hints for all new functions
2. **Error Handling**: Implement proper exception handling for file operations
3. **Logging**: Add structured logging for debugging and monitoring
4. **Documentation**: Include docstrings for all new functions and classes
5. **Testing**: Achieve minimum 80% code coverage for new functionality

### Performance Considerations

1. **Lazy Loading**: Load configurations only when needed
2. **Caching**: Cache frequently accessed room data and configurations
3. **Memory Management**: Implement efficient data structures for large worlds
4. **File I/O**: Minimize file system operations through batching

### Security Considerations

1. **Path Validation**: Validate all file paths to prevent directory traversal
2. **JSON Validation**: Validate all JSON input to prevent injection attacks
3. **Access Control**: Ensure proper file permissions for configuration files
4. **Input Sanitization**: Sanitize all user-provided room data

## Success Metrics

### Functional Metrics

- [ ] All existing rooms successfully migrated
- [ ] New hierarchical structure supports planned world locations
- [ ] Environment inheritance works correctly
- [ ] Zone types are properly classified
- [ ] Room ID resolution works for both formats

### Performance Metrics

- [ ] World loading time remains under 5 seconds
- [ ] Room lookup performance within 100ms
- [ ] Memory usage increase less than 20%
- [ ] No regression in existing functionality

### Quality Metrics

- [ ] All tests pass with 80%+ coverage
- [ ] No linting errors (ruff compliance)
- [ ] Documentation complete and accurate
- [ ] Migration utilities handle edge cases

## Risk Mitigation

### Technical Risks

1. **Migration Complexity**: Comprehensive testing and validation
2. **Performance Impact**: Benchmarking and optimization
3. **Data Loss**: Backup and rollback procedures
4. **Breaking Changes**: Dual-format support during transition

### Operational Risks

1. **Development Time**: Phased implementation approach
2. **Testing Coverage**: Automated testing and validation
3. **Documentation**: Comprehensive documentation updates
4. **User Impact**: Backward compatibility maintenance

---

*This planning document will be updated as implementation progresses and new requirements are discovered.*
