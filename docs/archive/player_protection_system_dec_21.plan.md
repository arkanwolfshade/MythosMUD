---
name: Player Protection System
overview: Implement a configurable protection system that grants players immunity from damage and targeting for a configurable duration (default 10 seconds) after login or respawn. Players can move during protection but cannot attack or use abilities. Protection is visible to both the protected player and others.
todos:

  - id: create_protection_service

    content: Create PlayerProtectionService with in-memory state tracking, expiration handling, and thread-safe operations
    status: pending

  - id: add_config

    content: Add spawn_protection_duration field to GameConfig with validation (1-300 seconds)
    status: pending

  - id: activate_on_login

    content: Integrate protection activation in select_character endpoint after successful character selection
    status: pending

  - id: activate_on_respawn

    content: Integrate protection activation in respawn_player and respawn_player_from_delirium methods
    status: pending

  - id: filter_targeting

    content: Filter protected players from target resolution results in _search_players_in_room
    status: pending

  - id: prevent_damage

    content: Add protection checks in combat_service.process_attack and player_service.damage_player to block damage
    status: pending

  - id: restrict_abilities

    content: Add protection checks in combat command handlers to block attack and combat abilities
    status: pending

  - id: client_notifications

    content: Send protection start/end events to protected player and room broadcasts for visibility
    status: pending

  - id: service_integration

    content: Initialize PlayerProtectionService in app lifespan, add to app state, and start background cleanup task
    status: pending

  - id: add_tests

    content: Create unit tests for protection service and integration tests for protection flow
    status: pending
---

# Player Protection System Impleme

ntation Plan

## Overview

This plan implements a spawn/respawn protection system that makes players immune to damage and targeting for a configurable period (default 10 seconds) after login or respawn. During protection:

- Players can move but cannot attack or use combat abilities
- Players cannot be targeted by other players or NPCs
- Protection status is visible to both the protected player and others
- Protection applies to both PvP and PvE

## Architecture Components

### 1. Protection State Management

**File**: `server/services/player_protection_service.py` (new)

- In-memory tracking of protected players with expiration timestamps
- Methods to:
- Start protection for a player (`start_protection(player_id, duration)`)
- Check if a player is protected (`is_protected(player_id) -> bool`)

- Get remaining protection time (`get_remaining_protection(player_id) -> float`)
- Clear protection (`clear_protection(player_id)`)

- Thread-safe implementation using locks/dict
- Background task to clean up expired protections

### 2. Configuration

**File**: `server/config/models.py`

- Add to `GameConfig` class:

  ```python
    spawn_protection_duration: int = Field(default=10, description="Spawn/respawn protection duration in seconds")
  ```

- Add validation: `1 <= value <= 300` (1 second to 5 minutes)

### 3. Protection Activation Points

#### 3a. Login Protection

**File**: `server/api/players.py`

- In `select_character()` endpoint, after successful character selection:
- Get protection service instance
- Call `start_protection(player_id, config.game.spawn_protection_duration)`
- Send protection start message to player

#### 3b. Respawn Protection

**File**: `server/services/player_respawn_service.py`

- In `respawn_player()` method, after respawn completes:

Get protection service from app state or dependency injection

- Call `start_protection(player_id, duration)`
- Add protection info to `PlayerRespawnedEvent`
- In `respawn_player_from_delirium()`, do the same

**File**: `server/realtime/player_event_handlers_respawn.py`

- In `handle_player_respawned()`, extract protection info from event and send to client

### 4. Targeting Filtering

**File**: `server/services/target_resolution_service.py`

- In `_search_players_in_room()` method:
- After getting player matches, filter out protected players
- Check `protection_service.is_protected(player_id)` before adding to matches
- Protected players are not included in target results

### 5. Damage Prevention

**File**: `server/services/combat_service.py`

- In `process_attack()` method, before applying damage:
- Check if target is protected: `protection_service.is_protected(target_id)`

- If protected, return early with message: "Target is protected and cannot be damaged"
- Log the blocked attack attempt

**File**: `server/game/player_service.py`

- In `damage_player()` method:
- Check protection status before applying damage
- Return error if player is protected

### 6. Ability Restrictions

**File**: `server/commands/combat.py`

- In `handle_attack_command()`:

Check if attacker is protected using protection service

- If protected, return: "You are protected and cannot attack"
- Similar checks for other combat commands

**File**: `server/command_handler_unified.py` or command routing

- Add pre-command check for combat-related commands:

Identify combat commands (attack, cast combat spells, etc.)

- Check protection status
- Block if protected (with appropriate message)

**Note**: Non-combat abilities (examine, talk, movement) should remain available during protection.

### 7. Visual Indicators

#### 7a. Client Notification (Protected Player)

**File**: `server/realtime/player_event_handlers_respawn.py` or similar

- When protection starts, send event to player:

  ```json
    {
      "event_type": "protection_started",
      "duration": 10,
      "message": "You are protected for 10 seconds"
    }
  ```

- When protection ends, send event:

  ```json
    {
      "event_type": "protection_ended",
      "message": "Your protection has expired"
    }
  ```

#### 7b. Visible to Others

**Option 1**: Modify player presence/room data

- Add `is_protected: bool` field to player data sent in room updates
- Client can display visual indicator (e.g., glow, shield icon)

**Option 2**: Send room broadcast

- When protection starts/ends, broadcast to room:

  ```json
    {
      "event_type": "player_protection_changed",
      "player_id": "...",
      "player_name": "...",
      "is_protected": true,
      "duration": 10
    }
  ```

### 8. Service Integration

**File**: `server/main.py` or lifespan management

- Initialize `PlayerProtectionService` as a singleton
- Add to app state for dependency injection

- Start background cleanup task for expired protections
- Ensure cleanup runs periodically (e.g., every 5 seconds)

### 9. Testing Requirements

Unit tests for `PlayerProtectionService`:

- Protection start/end
- Expiration handling
- Thread safety
- Integration tests:
- Protection on login
- Protection on respawn
- Targeting blocked during protection
- Damage blocked during protection

- Ability restrictions during protection
- Protection expiration

## Implementation Order

1. Create `PlayerProtectionService` with basic functionality
2. Add configuration to `GameConfig`
3. Integrate protection activation on login

4. Integrate protection activation on respawn
5. Add targeting filtering
6. Add damage prevention
7. Add ability restrictions
8. Add client notifications
9. Add tests

## Key Design Decisions

**In-memory storage**: Protection state is ephemeral and doesn't need persistence. If server restarts, protection is lost, which is acceptable.

**Thread-safe**: Use asyncio locks or thread-safe dict for concurrent access

**Background cleanup**: Periodic task removes expired entries to prevent memory leaks

**Separation of concerns**: Protection service is a standalone service that can be queried by other systems

**Configurable duration**: Allows server admins to adjust protection time via environment variable `GAME_SPAWN_PROTECTION_DURATION`

## Files to Create/Modify

### New Files

`server/services/player_protection_service.py`

### Modified Files

`server/config/models.py` - Add config field

- `server/api/players.py` - Activate on login
- `server/services/player_respawn_service.py` - Activate on respawn

- `server/services/target_resolution_service.py` - Filter protected players
- `server/services/combat_service.py` - Block damage

- `server/game/player_service.py` - Block damage in direct damage method
- `server/commands/combat.py` - Block combat commands
- `server/realtime/player_event_handlers_respawn.py` - Send protection events

- `server/main.py` or lifespan - Initialize service

## Edge Cases

Protection expires mid-combat: Damage is blocked until expiration

- Player disconnects during protection: Protection state is cleared (in-memory)
- Server restart during protection: Protection is lost (acceptable)

- Multiple respawns in quick succession: Each respawn resets protection timer
