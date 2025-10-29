# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-10-27-player-death-respawn/spec.md

## Technical Requirements

### Backend Changes

#### 1. Player Health State Management

**File:** `server/models/player.py`

- Add method: `get_health_state() -> str` returning "alive", "mortally_wounded", or "dead"
- Add method: `is_mortally_wounded() -> bool` (0 >= HP > -10)
- Add method: `is_dead() -> bool` (HP <= -10)
- Update `is_alive()` to return `current_health > 0` (currently correct)

#### 2. Combat Service HP Capping

**File:** `server/services/combat_service.py`

- Update `_apply_damage()` method to cap player HP at minimum -10
- Add `_check_player_death_state(player_id)` method to detect mortally wounded/dead states
- Add `_handle_player_mortally_wounded(player_id, attacker_id, combat_id)` method
- Add `_handle_player_death(player_id, combat_id, death_location)` method
- Update `process_attack()` to check for mortally wounded/death state after damage application
- Implement threat queue logic: remove dead players, continue combat if others remain

#### 3. HP Decay System

**File:** `server/services/player_death_service.py` (NEW)

- Create new service: `PlayerDeathService`
- Method: `process_mortally_wounded_tick(player_id)` - Apply 1 HP decay, check for death
- Method: `get_mortally_wounded_players() -> list[str]` - Query all players with 0 >= HP > -10
- Integration with game tick loop in `server/app/lifespan.py`
- Publish `PlayerHPDecayEvent` for each tick of decay

#### 4. Respawn Service

**File:** `server/services/player_respawn_service.py` (NEW)

- Create new service: `PlayerRespawnService`
- Method: `move_player_to_limbo(player_id, death_location)` - Move to limbo room, record death location
- Method: `respawn_player(player_id)` - Restore HP, move to respawn room, reset UI state
- Method: `get_respawn_room(player_id) -> str` - Get player's respawn room (from DB or default)
- Default respawn room constant: `DEFAULT_RESPAWN_ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"`

#### 5. Event Types

**File:** `server/events/event_types.py`

- Add `PlayerMortallyWoundedEvent` - Triggered when HP reaches 0
- Add `PlayerDiedEvent` - Triggered when HP reaches -10
- Add `PlayerRespawnedEvent` - Triggered when player respawns
- Add `PlayerHPDecayEvent` - Triggered for each HP decay tick

#### 6. Message Broadcasting

**File:** `server/services/combat_messaging_integration.py`

- Add method: `broadcast_player_mortally_wounded(player_id, player_name, attacker_name, room_id)`
- Add method: `broadcast_player_death(player_id, player_name, room_id, death_location)`
- Add method: `broadcast_player_respawn(player_id, player_name, room_id)`
- Add method: `send_hp_decay_message(player_id, current_hp)`

#### 7. Limbo Room

**File:** `data/local/rooms/limbo/limbo_room.json` (NEW)

- Create special "limbo" room with ID: `limbo_death_void`
- Room has no exits, no NPCs, no other players visible
- Used for complete isolation during interstitial screen

### Frontend Changes

#### 1. Mortally Wounded UI State

**File:** `client/src/components/GameTerminalWithPanels.tsx`

- Add state: `isMortallyWounded: boolean`
- Add state: `isDead: boolean`
- Listen for `PlayerMortallyWoundedEvent` to trigger red UI mode
- Apply CSS class `mortally-wounded` to all panels when state is active
- Disable command input field when mortally wounded
- Listen for `PlayerHPDecayEvent` to display decay messages

**File:** `client/src/styles/GameTerminal.css` (or equivalent)

- Add `.mortally-wounded` class with red color scheme
- Add `.border-effect` class for pulsing/glowing border effect
- Ensure negative HP values display correctly in Player Information panel

#### 2. Death Interstitial Screen

**File:** `client/src/components/DeathInterstitial.tsx` (NEW)

- Create full-screen modal component
- Display thematic death narrative text (Lovecraftian atmosphere)
- Show death location information
- Display "Rejoin the earthly plane" button
- Button triggers respawn API call
- Component appears when `isDead` state is true

**Interstitial Message (Placeholder):**

```
The darkness consumes you utterly, and for a timeless moment, you drift through
the spaces between worlds. Whispers in languages older than humanity echo around
you, speaking of things mortal minds were never meant to comprehend.

But the threads binding you to the waking world are not yet severed. The sanitarium
calls you back from the threshold of oblivion...

You died at: [DEATH_LOCATION_NAME]
```

#### 3. Respawn Integration

**File:** `client/src/components/GameTerminalWithPanels.tsx`

- Listen for `PlayerRespawnedEvent` to:
  - Close death interstitial
  - Reset UI to normal colors
  - Clear mortally wounded state
  - Update room to respawn location
  - Re-enable command input

### API Changes

**File:** `server/routes/game_routes.py` or appropriate router

- Add endpoint: `POST /api/player/respawn`
  - Triggers player respawn
  - Returns new room data and player state
  - Called by "Rejoin the earthly plane" button

### Game Tick Integration

**File:** `server/app/lifespan.py`

- Update `game_tick_loop()` to call `PlayerDeathService.process_all_mortally_wounded_players()`
- Process HP decay for all mortally wounded players each tick
- Broadcast decay messages via NATS

### Combat Service Integration

**File:** `server/services/combat_service.py`

- Update `process_attack()` flow:
  1. Apply damage
  2. Cap HP at -10 if player
  3. Check if player became mortally wounded (HP reached 0)
  4. Check if player died (HP reached -10)
  5. Remove dead players from combat
  6. Check if combat should end (all players dead)
  7. Broadcast appropriate events

### Performance Considerations

- HP decay processing should be O(n) where n = number of mortally wounded players
- Death location storage should use simple string (room_id + timestamp)
- Limbo room should not process normal room logic (optimized no-op)
- UI state transitions should debounce to prevent flickering

### Security Considerations

- Validate respawn room exists before teleporting player
- Prevent respawn exploitation (e.g., respawning mid-combat)
- Ensure dead players cannot execute commands via API
- Sanitize death location data in interstitial screen (prevent XSS)

### Testing Requirements

- Unit tests for HP capping at -10
- Unit tests for mortally wounded state detection
- Unit tests for HP decay logic
- Unit tests for threat queue management
- Integration tests for complete death → respawn flow
- E2E tests for UI state transitions
- E2E tests for multi-player combat with death scenarios

## External Dependencies

None required. This feature uses existing libraries and frameworks.
