# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-01-27-combat-system/spec.md

## Schema Changes

### No New Tables Required

The combat system will use existing database tables without requiring new schema changes. All combat-related data will be stored in existing JSON fields within the NPC definitions.

### Existing Table Modifications

#### NPC Definitions Table (`npc_definitions`)

**No structural changes required.** Combat data will be stored in existing JSON fields:

##### `base_stats` JSON Field Extensions

```json
{
  "hp": 10,
  "max_hp": 10,
  "xp_value": 5,
  "dexterity": 12,
  "strength": 10,
  "constitution": 8
}
```

**New Fields:**
- `xp_value` (integer): Experience points awarded when NPC is defeated
- `dexterity` (integer): NPC dexterity for turn order calculation
- `strength` (integer): NPC strength (for future expansion)
- `constitution` (integer): NPC constitution (for future expansion)

##### `behavior_config` JSON Field Extensions

```json
{
  "combat_messages": {
    "attack_attacker": "You swing your fist at {target_name} and hit for {damage} damage",
    "attack_defender": "{attacker_name} swings their fist at you and hits you for {damage} damage",
    "attack_other": "{attacker_name} swings their fist at {target_name} and hits for {damage} damage",
    "death_message": "The {npc_name} collapses, dead"
  },
  "combat_behavior": {
    "aggression_level": "passive",
    "retreat_threshold": 0.2,
    "combat_timeout": 300
  }
}
```

**New Fields:**
- `combat_messages` (object): Message templates for different combat perspectives
- `combat_behavior` (object): Combat behavior configuration

### Data Migration Strategy

#### Basic Data Migration Script

A simple migration script will add default combat data to existing NPCs:

```python
def migrate_npc_combat_data():
    """Add default combat data to existing NPCs."""
    npcs = get_all_npc_definitions()

    for npc in npcs:
        # Add default combat stats if not present
        if 'xp_value' not in npc.base_stats:
            npc.base_stats['xp_value'] = 1  # Default 1 XP
        if 'dexterity' not in npc.base_stats:
            npc.base_stats['dexterity'] = 10  # Default dexterity

        # Add default combat messages if not present
        if 'combat_messages' not in npc.behavior_config:
            npc.behavior_config['combat_messages'] = {
                'attack_attacker': "You swing your fist at {target_name} and hit for {damage} damage",
                'attack_defender': "{attacker_name} swings their fist at you and hits you for {damage} damage",
                'attack_other': "{attacker_name} swings their fist at {target_name} and hits for {damage} damage",
                'death_message': "The {npc_name} collapses, dead"
            }

        # Add default combat behavior if not present
        if 'combat_behavior' not in npc.behavior_config:
            npc.behavior_config['combat_behavior'] = {
                'aggression_level': 'passive',
                'retreat_threshold': 0.2,
                'combat_timeout': 300
            }

        save_npc_definition(npc)
```

### Data Validation

#### JSON Schema Validation

The existing JSON schema validation will be extended to include combat data validation:

```json
{
  "base_stats": {
    "type": "object",
    "properties": {
      "hp": {"type": "integer", "minimum": 0},
      "max_hp": {"type": "integer", "minimum": 1},
      "xp_value": {"type": "integer", "minimum": 0},
      "dexterity": {"type": "integer", "minimum": 1, "maximum": 20},
      "strength": {"type": "integer", "minimum": 1, "maximum": 20},
      "constitution": {"type": "integer", "minimum": 1, "maximum": 20}
    },
    "required": ["hp", "max_hp", "xp_value"]
  },
  "behavior_config": {
    "type": "object",
    "properties": {
      "combat_messages": {
        "type": "object",
        "properties": {
          "attack_attacker": {"type": "string"},
          "attack_defender": {"type": "string"},
          "attack_other": {"type": "string"},
          "death_message": {"type": "string"}
        },
        "required": ["attack_attacker", "attack_defender", "attack_other", "death_message"]
      },
      "combat_behavior": {
        "type": "object",
        "properties": {
          "aggression_level": {"type": "string", "enum": ["passive", "aggressive"]},
          "retreat_threshold": {"type": "number", "minimum": 0, "maximum": 1},
          "combat_timeout": {"type": "integer", "minimum": 60}
        }
      }
    }
  }
}
```

### Performance Considerations

#### Indexing Strategy

No additional indexes required. Existing indexes on `npc_definitions` table will handle combat queries efficiently.

#### Query Optimization

- Combat data will be cached in memory during combat
- Database queries will be minimized through in-memory state management
- JSON field queries will use existing database JSON query capabilities

### Data Integrity

#### Constraints

- `xp_value` must be non-negative integer
- `dexterity`, `strength`, `constitution` must be between 1-20
- Combat message templates must contain required variable placeholders
- Combat behavior settings must be within valid ranges

#### Validation Rules

- All combat messages must contain proper variable substitution syntax
- Death messages must be non-empty strings
- Combat behavior settings must be within defined ranges
- XP values should be reasonable for NPC difficulty level

### Backup and Recovery

#### Data Backup

- Existing database backup procedures will cover combat data
- JSON field data will be included in standard database backups
- No special backup procedures required for combat data

#### Data Recovery

- Combat data recovery follows existing database recovery procedures
- JSON field data will be restored with standard database recovery
- Migration script can be re-run to restore default combat data if needed

### Monitoring and Maintenance

#### Data Monitoring

- Monitor JSON field size and complexity
- Track combat data usage patterns
- Monitor database performance with extended JSON queries

#### Maintenance Procedures

- Regular validation of combat data integrity
- Cleanup of orphaned combat state data
- Performance monitoring of JSON field queries
- Regular backup verification of combat data
