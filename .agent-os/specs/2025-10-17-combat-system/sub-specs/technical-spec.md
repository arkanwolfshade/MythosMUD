# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-01-27-combat-system/spec.md

## Technical Requirements

### Architecture Overview

The combat system will be implemented using a modular approach that integrates with existing MythosMUD systems:

```
server/game/
├── combat_service.py          # Core combat business logic
├── combat_state_manager.py    # Combat state tracking and management
└── combat_message_service.py  # Combat message generation and formatting

server/commands/
├── combat_commands.py         # Combat command handlers (attack, punch)

server/events/
├── combat_events.py           # Combat-specific event types
```

### Core Combat Mechanics

**Round-Based System**: Combat rounds last 100 server ticks (10 realtime seconds) with automatic progression

**Auto-Progression**: Combat automatically continues through rounds every 10 seconds (100 ticks) until completion

**Round Execution**: All combatants act in each round, executing actions sequentially in initiative order
 (dexterity-based, highest first)

**Action Queuing**: Commands and spells can be queued for execution in the next round

- **Damage System**: Fixed 1 damage per attack for MVP
- **Health Tracking**: Real-time health display during combat with on-demand status checking
- **Combat State**: In-memory state management with automatic cleanup and turn progression
- **Target Validation**: Room occupant targeting with existing look command logic
- **NPC Passive Behavior**: NPCs perform non-combat actions during their turns (defensive maneuvers, taunts, thematic behaviors)

### Command System Integration

**Primary Command**: `attack <target>` with target validation

**Aliases**: `punch`, `kick`, `strike` (all do 1 damage)

**Validation**: Extended validation with combat-specific rules

- **Rate Limiting**: Leverage existing command rate limiting system
- **Security**: Use existing security measures plus combat-specific validation

### Event System Integration

**Extend Existing Events**: Add combat data to `NPCAttacked`, `NPCTookDamage`, `NPCDied`

**New Combat Events**: `CombatStarted`, `CombatEnded`, `PlayerAttacked`

**Event Publishing**: Use existing NATS event publishing system

- **Event Broadcasting**: Combat messages to Game Info panel via existing event system

### Database Integration

**No Schema Changes**: Use existing JSON fields in NPC definitions

**Combat Data Storage**: Store in `base_stats` and `behavior_config` JSON fields

**Data Structure**:

  ```json
  {
    "base_stats": {
      "hp": 10,
      "max_hp": 10,
      "xp_value": 5
    },
    "behavior_config": {
      "combat_messages": {
        "attack_attacker": "You swing your fist at {target_name} and hit for {damage} damage",
        "attack_defender": "{attacker_name} swings their fist at you and hits you for {damage} damage",
        "attack_other": "{attacker_name} swings their fist at {target_name} and hits for {damage} damage",
        "death_message": "The {npc_name} collapses, dead"
      }
    }
  }
  ```

### State Management

**In-Memory Storage**: Combat state stored in memory using dictionaries/lists

**Round Progression**: Automatic round advancement every 10 seconds (100 ticks) with all participants acting each round

**State Cleanup**: Automatic cleanup of stale combat states (timeout-based)

- **Player Disconnection**: Combat continues with timeout-based cleanup
- **Server Restart**: All combat states cleared on server restart
- **Health Tracking**: Real-time health updates stored in combat state (NPC health in-memory only, player health
 persisted to database)

### Messaging System

**Message Templates**: NPC-specific templates with variable substitution and health information

**Perspective-Based**: Different messages for attacker/defender/other players with health updates

**Thematic Content**: Cthulhu Mythos-themed messages including NPC non-combat actions

- **Broadcasting**: Real-time messages to all room occupants with automatic turn progression
- **Message Storage**: Combat messages in Game Info panel with health tracking
- **Health Display**: Real-time health updates in combat messages (e.g., "9/10 HP remaining")

### Integration Points

**Room Service**: Use existing room occupant tracking for targeting

**Player Service**: Integrate with existing player XP and stats system, persist player health changes to database

**NPC Service**: Extend existing NPC behaviors and lifecycle management, track NPC health in memory only

- **Event System**: Full integration with existing event bus architecture
- **Command System**: Extend existing command validation and processing
- **Security System**: Leverage existing rate limiting and input validation

### Performance Considerations

**Efficient Data Structures**: Use appropriate data structures for combat state

**Minimal Database Queries**: Cache combat data in memory

**Event Optimization**: Efficient event publishing and handling

- **Memory Management**: Automatic cleanup of stale combat states

### Error Handling

**Extended Error Handling**: Comprehensive error messages and logging

**Graceful Degradation**: Combat ends cleanly on errors

**Thematic Error Messages**: Cthulhu Mythos-themed error messages

- **Error Recovery**: Basic error recovery with combat state cleanup

### Testing Requirements

**Unit Tests**: Test individual combat functions and components

**Integration Tests**: Test integration with NPC, event, and messaging systems

**Comprehensive Coverage**: Test all combat functionality including edge cases

- **Performance Tests**: Basic performance benchmarks to ensure no server degradation

### Configuration Management

**YAML Configuration**: System-level combat settings in existing config files

**Database Configuration**: NPC-level combat settings in database JSON fields

**Runtime Changes**: Support for runtime configuration changes

- **Feature Flags**: Combat system enable/disable via feature flags

### Security Requirements

**Extended Security**: Combat-specific security measures and validation

**Rate Limiting**: Leverage existing command rate limiting

**Input Validation**: Comprehensive input validation for combat commands

- **Audit Logging**: Combat actions logged for security monitoring

### Deployment Strategy

**Feature Flag Deployment**: Deploy with feature flag for easy enable/disable

**Direct Deployment**: Deploy directly to production with feature flag

**Rollback Strategy**: Simple rollback via feature flag disable

- **Basic Monitoring**: Essential combat metrics and error alerting

## External Dependencies

No new external dependencies required. The combat system will leverage existing MythosMUD infrastructure including:

- Existing event system (EventBus, NATS)
- Existing command validation system
- Existing database persistence layer
- Existing messaging and real-time communication
- Existing security and rate limiting systems
