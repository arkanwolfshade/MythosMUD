# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-01-27-combat-system/spec.md

## Endpoints

### POST /command

**Purpose:** Process combat commands through existing command system
**Parameters:**
- `command` (string): Combat command (e.g., "attack rat", "punch goblin")
**Response:**
```json
{
  "result": "You swing your fist at the rat and hit for 1 damage",
  "success": true,
  "combat_state": {
    "active": true,
    "target": "rat_001",
    "turn_order": ["player_123", "rat_001"]
  }
}
```
**Errors:**
- `INVALID_TARGET`: Target not found or not attackable
- `COMBAT_ERROR`: Combat system error
- `RATE_LIMIT_EXCEEDED`: Command rate limit exceeded

### WebSocket Events

#### Combat Events

**Event Type:** `combat_event`
**Purpose:** Broadcast combat actions to room occupants
**Data Structure:**
```json
{
  "event_type": "combat_event",
  "timestamp": "2025-01-27T10:30:00Z",
  "player_id": "player_123",
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
  "data": {
    "action": "attack",
    "attacker": "Ithaqua",
    "target": "rat",
    "damage": 1,
    "message": "Ithaqua swings their fist at the rat and hits for 1 damage",
    "perspective": "other"
  }
}
```

**Event Type:** `combat_started`
**Purpose:** Notify when combat begins
**Data Structure:**
```json
{
  "event_type": "combat_started",
  "timestamp": "2025-01-27T10:30:00Z",
  "player_id": "player_123",
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
  "data": {
    "participants": ["player_123", "npc_rat_001"],
    "turn_order": ["player_123", "npc_rat_001"],
    "initiator": "player_123"
  }
}
```

**Event Type:** `combat_ended`
**Purpose:** Notify when combat ends
**Data Structure:**
```json
{
  "event_type": "combat_ended",
  "timestamp": "2025-01-27T10:30:00Z",
  "player_id": "player_123",
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
  "data": {
    "participants": ["player_123", "npc_rat_001"],
    "winner": "player_123",
    "xp_awarded": 5,
    "reason": "target_defeated"
  }
}
```

#### Extended Existing Events

**Event Type:** `npc_attacked` (Extended)
**Purpose:** NPC attacked event with combat data
**Data Structure:**
```json
{
  "event_type": "npc_attacked",
  "timestamp": "2025-01-27T10:30:00Z",
  "npc_id": "npc_rat_001",
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
  "data": {
    "attacker_id": "player_123",
    "attacker_name": "Ithaqua",
    "damage": 1,
    "attack_type": "punch",
    "combat_state": "active"
  }
}
```

**Event Type:** `npc_took_damage` (Extended)
**Purpose:** NPC damage event with combat data
**Data Structure:**
```json
{
  "event_type": "npc_took_damage",
  "timestamp": "2025-01-27T10:30:00Z",
  "npc_id": "npc_rat_001",
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
  "data": {
    "damage": 1,
    "remaining_hp": 9,
    "attacker_id": "player_123",
    "combat_state": "active"
  }
}
```

**Event Type:** `npc_died` (Extended)
**Purpose:** NPC death event with combat data
**Data Structure:**
```json
{
  "event_type": "npc_died",
  "timestamp": "2025-01-27T10:30:00Z",
  "npc_id": "npc_rat_001",
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
  "data": {
    "killer_id": "player_123",
    "killer_name": "Ithaqua",
    "xp_awarded": 5,
    "death_message": "The rat collapses, dead",
    "combat_state": "ended"
  }
}
```

## Command Processing

### Combat Command Validation

**Input Validation:**
- Command format: `attack <target>` or `punch <target>`
- Target validation: Target must exist in current room
- Combat state validation: Player can only be in one combat at a time
- Rate limiting: Existing command rate limiting applies

**Target Resolution:**
- Use existing room occupant targeting logic
- Case-insensitive target matching
- Partial name matching support
- Target must be alive and attackable

### Combat State Management

**State Storage:**
- In-memory combat state tracking
- Combat participants and turn order
- Current combat target and status
- Combat timeout and cleanup

**State Transitions:**
- `idle` → `combat_started` (on first attack)
- `combat_started` → `combat_ended` (on target death or timeout)
- `combat_ended` → `idle` (after cleanup)

## Error Handling

### Combat-Specific Errors

**Error Types:**
- `TARGET_NOT_FOUND`: Target not found in current room
- `TARGET_DEAD`: Target is already dead
- `TARGET_NOT_ATTACKABLE`: Target cannot be attacked
- `COMBAT_IN_PROGRESS`: Player already in combat
- `COMBAT_TIMEOUT`: Combat session has timed out
- `INVALID_COMBAT_STATE`: Combat state is invalid

**Error Responses:**
```json
{
  "result": "You don't see a 'dragon' here. Perhaps it exists only in your fevered imagination?",
  "success": false,
  "error_type": "TARGET_NOT_FOUND",
  "combat_state": {
    "active": false
  }
}
```

### Thematic Error Messages

**Target Not Found:**
- "You don't see a '{target}' here. Perhaps it exists only in your fevered imagination?"
- "The shadows reveal no '{target}' to strike at."

**Target Dead:**
- "The {target} is already dead. Your blows strike only lifeless flesh."
- "You cannot harm what is already beyond the veil."

**Invalid Target:**
- "You cannot attack that. The very thought fills you with dread."
- "Your instincts warn against such a foolish action."

## Integration Points

### Existing Command System

**Command Registration:**
```python
# In command_service.py
self.command_handlers.update({
    "attack": handle_attack_command,
    "punch": handle_attack_command,  # Alias
    "kick": handle_attack_command,   # Alias
    "strike": handle_attack_command, # Alias
})
```

**Command Processing:**
- Use existing command validation pipeline
- Extend with combat-specific validation rules
- Leverage existing rate limiting and security measures
- Integrate with existing alias system

### Event System Integration

**Event Publishing:**
```python
# Publish combat events through existing NATS system
await event_publisher.publish_combat_event(
    event_type="combat_started",
    player_id=player_id,
    room_id=room_id,
    data=combat_data
)
```

**Event Subscribers:**
- Real-time event handler for combat message broadcasting
- Room occupant updates for combat state changes
- Player service integration for XP rewards
- NPC service integration for combat behavior

### Database Integration

**NPC Data Access:**
```python
# Access combat data from existing NPC definitions
npc_definition = get_npc_definition(npc_id)
combat_stats = npc_definition.base_stats
combat_messages = npc_definition.behavior_config.get('combat_messages', {})
```

**Player Data Updates:**
```python
# Update player XP through existing player service
await player_service.award_experience(player_id, xp_amount)
```

## Performance Considerations

### Event Publishing Optimization

- Batch combat events when possible
- Use efficient JSON serialization
- Minimize event payload size
- Cache frequently accessed combat data

### State Management Efficiency

- Use appropriate data structures for combat state
- Implement efficient cleanup procedures
- Minimize memory usage for combat state
- Optimize turn order calculations

### Database Query Optimization

- Cache NPC combat data in memory
- Minimize database queries during combat
- Use efficient JSON field queries
- Implement query result caching

## Security Considerations

### Input Validation

- Comprehensive target validation
- Command injection prevention
- Rate limiting for combat commands
- Input sanitization for combat messages

### State Security

- Combat state isolation between players
- Secure combat state cleanup
- Protection against state manipulation
- Audit logging for combat actions

### Event Security

- Secure event publishing
- Event payload validation
- Protection against event flooding
- Secure event subscription management
