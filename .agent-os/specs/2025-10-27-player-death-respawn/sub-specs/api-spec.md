# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-10-27-player-death-respawn/spec.md

## WebSocket Events (NATS-based)

### Outgoing Events (Server → Client)

#### 1. `player_mortally_wounded`

**Purpose:** Notify player and room when player becomes mortally wounded

**Trigger:** Player HP reaches 0 (but above -10)

**Payload to Player:**

```json
{
  "event_type": "player_mortally_wounded",
  "timestamp": "2025-10-27T15:30:00Z",
  "data": {
    "player_id": "player_123",
    "player_name": "Investigator Smith",
    "attacker_id": "npc_dr_francis_morgan_001",
    "attacker_name": "Dr. Francis Morgan",
    "current_hp": 0,
    "max_hp": 100,
    "message": "Dr. Francis Morgan's attack causes you to collapse as darkness begins closing in on your vision"
  }
}
```

**Payload to Room (other players):**

```json
{
  "event_type": "player_mortally_wounded",
  "timestamp": "2025-10-27T15:30:00Z",
  "data": {
    "player_id": "player_123",
    "player_name": "Investigator Smith",
    "attacker_name": "Dr. Francis Morgan",
    "room_id": "earth_arkhamcity_sanitarium_foyer_001",
    "message": "Investigator Smith collapses from Dr. Francis Morgan's attack and is on the verge of death!"
  }
}
```

#### 2. `player_hp_decay`

**Purpose:** Notify player of HP decay tick

**Trigger:** Game tick while player is mortally wounded

**Payload:**

```json
{
  "event_type": "player_hp_decay",
  "timestamp": "2025-10-27T15:30:01Z",
  "data": {
    "player_id": "player_123",
    "old_hp": -1,
    "new_hp": -2,
    "max_hp": 100,
    "message": "You feel your life force ebbing away... (-2 HP)"
  }
}
```

#### 3. `player_died`

**Purpose:** Notify player and room when player dies

**Trigger:** Player HP reaches -10

**Payload to All in Room:**

```json
{
  "event_type": "player_died",
  "timestamp": "2025-10-27T15:30:10Z",
  "data": {
    "player_id": "player_123",
    "player_name": "Investigator Smith",
    "death_location": "earth_arkhamcity_sanitarium_foyer_001",
    "death_location_name": "Sanitarium Foyer Entrance",
    "combat_id": "combat_uuid_here",
    "message": "Investigator Smith exhales their last breath."
  }
}
```

#### 4. `show_death_interstitial`

**Purpose:** Trigger death interstitial screen display

**Trigger:** Immediately after `player_died` event

**Payload:**

```json
{
  "event_type": "show_death_interstitial",
  "timestamp": "2025-10-27T15:30:10Z",
  "data": {
    "player_id": "player_123",
    "death_location": "earth_arkhamcity_sanitarium_foyer_001",
    "death_location_name": "Sanitarium Foyer Entrance",
    "narrative_text": "[THEMATIC_DEATH_MESSAGE]"
  }
}
```

#### 5. `player_respawned`

**Purpose:** Notify room when player respawns

**Trigger:** Player clicks "Rejoin the earthly plane" button

**Payload to Respawn Room:**

```json
{
  "event_type": "player_respawned",
  "timestamp": "2025-10-27T15:30:15Z",
  "data": {
    "player_id": "player_123",
    "player_name": "Investigator Smith",
    "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
    "current_hp": 100,
    "max_hp": 100,
    "message": "Patient Investigator Smith opens their eyes and awakens from their coma."
  }
}
```

### HTTP Endpoints

#### POST /api/player/respawn

**Purpose:** Handle player respawn request from death interstitial screen

**Authentication:** Required (JWT token)

**Request:**

```json
{
  "player_id": "player_123"
}
```

**Response (Success - 200):**

```json
{
  "success": true,
  "data": {
    "player_id": "player_123",
    "respawn_room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
    "current_hp": 100,
    "max_hp": 100,
    "room": {
      "id": "earth_arkhamcity_sanitarium_room_foyer_001",
      "name": "Sanitarium - Main Foyer",
      "description": "...",
      "exits": [...],
      "occupants": [...]
    }
  }
}
```

**Response (Error - 400):**

```json
{
  "success": false,
  "error": "Player is not dead",
  "code": "PLAYER_NOT_DEAD"
}
```

**Response (Error - 404):**

```json
{
  "success": false,
  "error": "Respawn room not found",
  "code": "RESPAWN_ROOM_NOT_FOUND"
}
```

**Rate Limiting:** 1 request per 5 seconds per player (prevent spam)

**Validation:**

- Player must be dead (HP <= -10)
- Respawn room must exist
- Player must not already be in respawn process

## NATS Subjects

### Published Subjects

`events.player.mortally_wounded.<room_id>` - Room-scoped mortally wounded events

- `events.player.died.<room_id>` - Room-scoped death events
- `events.player.respawned.<room_id>` - Room-scoped respawn events
- `events.player.hp_decay.<player_id>` - Player-scoped HP decay (personal message)

### Subscribed Subjects

**File:** `server/realtime/nats_message_handler.py`

Add subscriptions to:

- `events.player.mortally_wounded.*`
- `events.player.died.*`
- `events.player.respawned.*`
- `events.player.hp_decay.*`

## Error Handling

### Combat Service Errors

**HP Calculation Error:** Log warning, cap at -10, continue

**Death Handler Error:** Log error, force respawn to prevent player being stuck

**Respawn Room Missing:** Log error, use hardcoded default sanitarium room

### Death Service Errors

**HP Decay Processing Error:** Log error, skip player for this tick, continue with others

**Event Publishing Error:** Log error, continue processing (don't block game ticks)

### Respawn Service Errors

**Database Update Error:** Log error, retry once, then force update with default values

**Room Transfer Error:** Log critical error, force player to sanitarium

**Limbo Room Missing:** Log warning, create temporary limbo state in memory
