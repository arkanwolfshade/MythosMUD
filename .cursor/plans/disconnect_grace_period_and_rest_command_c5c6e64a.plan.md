---
name: Disconnect Grace Period and Rest Command
overview: Implement a 30-second grace period for disconnected players (zombie state with auto-attack), a new `/rest` command with 10-second countdown for clean disconnection, and instant rest functionality in inns/hotels/motels.
todos:
  - id: grace_period_tracker
    content: Create disconnect_grace_period.py module to manage 30-second grace period timers and zombie state
    status: completed
  - id: connection_manager_grace
    content: Add grace_period_players tracking to ConnectionManager
    status: completed
  - id: modify_disconnect_tracking
    content: Modify player_presence_tracker.py to start grace period instead of immediate removal
    status: completed
  - id: zombie_state_utils
    content: Add is_player_in_grace_period() utility method
    status: completed
  - id: combat_grace_autoattack
    content: Modify combat_turn_processor.py to allow auto-attack for grace period players
    status: completed
  - id: command_blocking_grace
    content: Block commands for grace period players (except auto-attack responses)
    status: completed
  - id: reconnect_cancel_grace
    content: Handle reconnection during grace period to cancel timer
    status: completed
  - id: rewrite_rest_command
    content: Rewrite rest_command.py for 10-second countdown disconnect functionality
    status: completed
  - id: rest_state_tracking
    content: Add resting_players tracking to ConnectionManager
    status: completed
  - id: rest_interrupt_handling
    content: Implement interrupt logic for combat, movement, and spellcasting
    status: completed
  - id: rest_position_setting
    content: Set character to sitting position when /rest starts
    status: completed
  - id: room_rest_location
    content: Add rest_location property to Room model
    status: completed
  - id: rest_location_logic
    content: Implement instant disconnect logic for rest locations when not in combat
    status: completed
  - id: update_room_json
    content: "Add rest_location: true to inn/hotel/motel room JSON files"
    status: completed
  - id: visual_indicator_implementation
    content: Implement (linkdead) visual indicator in room occupant lists and /look command output
    status: pending
---

# Disconnect Grace Period and Rest Command Implementation

## Overview

This plan implements three related features:

1. **30-second grace period** after **unintentional disconnect** (connection loss) where characters remain in-game in a "zombie" state
2. **New `/rest` command** with 10-second countdown for intentional clean disconnection (blocked during combat)
3. **Inn/hotel/motel support** for instant rest when not in combat

## Design Decisions

Based on industry comparison and requirements:

- **Grace Period Scope**: Only applies to **unintentional disconnects** (connection loss). Intentional disconnects via `/rest` or `/quit` have no grace period.
- **Auto-Attack During Grace Period**: Normal auto-attack behavior (includes weapons, but no special abilities/skills)
- **Rest During Combat**: `/rest` command is **blocked entirely during combat** (cannot be used to escape combat)
- **Visual Indicator**: Disconnected characters show "(linkdead)" in both room occupant lists and `/look` command output
- **Rest Location Regeneration**: Rest locations provide safe logout only (no automatic HP/MP regeneration)
- **Countdown Duration**: 10 seconds for `/rest` command countdown

## Architecture

### Disconnect Grace Period System

**New Components:**

- `server/realtime/disconnect_grace_period.py` - Manages grace period timers and zombie state
- Extend `ConnectionManager` to track grace period state
- Modify `player_presence_tracker.py` to delay actual removal

**Key Changes:**

- `ConnectionManager` will track `grace_period_players: dict[uuid.UUID, asyncio.Task]` to manage active grace periods
- `track_player_disconnected_impl()` will start grace period **only for unintentional disconnects** (connection loss)
- Intentional disconnects via `/rest` or `/quit` bypass grace period entirely
- Grace period cancels if player reconnects
- During grace period, player is in "zombie" state: can be attacked, can auto-attack (normal auto-attack with weapons, no special abilities), but cannot take other actions
- Disconnected characters show "(linkdead)" indicator in room lists and `/look` output

### Rest Command System

**Key Changes:**

- Replace existing `server/commands/rest_command.py` (currently for MP regeneration)
- New `/rest` command:
  - **Blocked entirely during combat** (cannot be used to escape combat)
  - Sets character to sitting position
  - Starts 10-second countdown
  - Interrupts on: movement, spellcasting, being attacked/targeted
  - Does NOT interrupt on: chat, look, inventory management
  - On completion: clean disconnect (no grace period for intentional disconnect)

**Rest State Tracking:**

- Add `resting_players: dict[uuid.UUID, asyncio.Task] `to `ConnectionManager`
- Track rest countdown state per player

### Room Rest Location Support

**Key Changes:**

- Add `rest_location: bool` property to `Room` model (loaded from room JSON data)
- Modify `/rest` command to check `room.rest_location`
- If in rest location and not in combat: instant disconnect (no countdown, no grace period)
- If in rest location but in combat: command is blocked (cannot use `/rest` during combat)
- Rest locations provide safe logout only (no automatic HP/MP regeneration)

## Implementation Details

### 1. Disconnect Grace Period

**Files to Modify:**

- `server/realtime/connection_manager.py` - Add grace period tracking
- `server/realtime/player_presence_tracker.py` - Delay removal, start grace period
- `server/realtime/disconnect_grace_period.py` - NEW: Grace period management
- `server/realtime/player_event_handlers_utils.py` - Add `is_player_in_grace_period()` method
- `server/services/combat_turn_processor.py` - Allow auto-attack for grace period players (normal auto-attack, no special abilities)
- `server/game/room_service.py` or room description handlers - Add "(linkdead)" indicator display
- `server/commands/look_command.py` - Add "(linkdead)" indicator in look output

**Grace Period Behavior:**

- **Only applies to unintentional disconnects** (connection loss)
- Player remains in room, visible to others
- Shows "(linkdead)" indicator in room occupant lists and `/look` command output
- Can be targeted and attacked
- Auto-attacks when attacked (normal auto-attack with weapons, no special abilities/skills)
- Cannot move, use commands, or take other actions
- Reconnection cancels grace period immediately
- After 30 seconds: normal disconnect cleanup

### 2. Rest Command

**Files to Modify:**

- `server/commands/rest_command.py` - Complete rewrite (block during combat, instant disconnect in rest locations)
- `server/realtime/connection_manager.py` - Add rest state tracking
- `server/commands/command_service.py` - Ensure `/rest` is registered (already is)
- `server/commands/combat.py` - Check rest state before allowing combat (rest interrupts combat)
- `server/game/movement_service.py` - Check rest state before allowing movement (rest interrupts movement)
- `server/commands/magic_commands.py` - Check rest state before allowing spellcasting (rest interrupts spellcasting)

**Rest Command Logic:**

```python
async def handle_rest_command(...):
    # Check if in combat -> block command entirely
    # Check if in rest location and not in combat -> instant disconnect (no grace period)
    # Otherwise: set position to sitting, start 10-second countdown
    # Track rest task in ConnectionManager
    # On interrupt: cancel task, return to normal
    # On completion: clean disconnect (no grace period for intentional disconnect)
```

**Combat Restriction:**

- `/rest` command is **blocked entirely during combat**
- Player must end combat before using `/rest`

**Interrupt Conditions:**

- Movement commands (`/go`, `/north`, etc.)
- Spellcasting commands (`/cast`, etc.)
- Being attacked or targeted in combat
- Any action that would normally interrupt rest

**Non-Interrupt Actions:**

- Chat commands (`/say`, `/local`, `/whisper`, etc.)
- Look commands (`/look`, `/examine`, etc.)
- Inventory commands (`/inventory`, `/equip`, `/drop`, etc.)
- Status commands (`/status`, `/whoami`, etc.)

### 3. Room Rest Location

**Files to Modify:**

- `server/models/room.py` - Add `rest_location` property
- Room JSON data files - Add `rest_location: true` flag to inn/hotel/motel rooms
- `server/commands/rest_command.py` - Check `room.rest_location`

**Room Property:**

```python
self.rest_location: bool = room_data.get("rest_location", False)
```

## Data Flow

### Disconnect Grace Period Flow

```
Unintentional Disconnect Detected (connection loss)
  ↓
Start Grace Period (30s timer)
  ↓
Player in Zombie State (shows "(linkdead)")
  ├─ Can be attacked → Auto-attacks back (normal auto-attack, no special abilities)
  ├─ Cannot move/command
  └─ Reconnect? → Cancel grace period immediately
  ↓
30s elapsed → Normal disconnect cleanup
```

**Note**: Intentional disconnects via `/rest` or `/quit` bypass grace period entirely.

### Rest Command Flow

```
/rest command
  ↓
In combat?
  ├─ Yes → Command blocked ("Cannot rest during combat")
  └─ No → In rest location?
         ├─ Yes → Instant disconnect (no grace period)
         └─ No → Set sitting, start 10s countdown
                ├─ Interrupted? → Cancel, return to normal
                └─ Completed? → Clean disconnect (no grace period)
```

## Testing Considerations

**Unit Tests:**

- Grace period timer expiration (unintentional disconnects only)
- Grace period cancellation on reconnect
- Grace period NOT applied to intentional disconnects
- Rest command blocked during combat
- Rest command countdown
- Rest command interruption scenarios
- Rest location instant disconnect
- Zombie state auto-attack behavior (normal auto-attack, no special abilities)
- Visual indicator "(linkdead)" display in room lists and /look

**Integration Tests:**

- Unintentional disconnect during combat → grace period applies
- Rest command in combat → command blocked
- Rest command in rest location → instant disconnect (no grace period)
- Multiple interrupts during rest countdown
- Visual indicator "(linkdead)" visible to other players

## Migration Notes

- Existing `/rest` command (MP regeneration) will be replaced
- Room JSON files need `rest_location` property added for inns/hotels/motels
- No database schema changes required
- Grace period is in-memory only (no persistence needed)

## Files Summary

**New Files:**

- `server/realtime/disconnect_grace_period.py`

**Modified Files:**

- `server/realtime/connection_manager.py`
- `server/realtime/player_presence_tracker.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/commands/rest_command.py`
- `server/models/room.py`
- `server/services/combat_turn_processor.py`
- `server/commands/combat.py`
- `server/game/movement_service.py`
- `server/commands/magic_commands.py`
- `server/game/room_service.py` or room description handlers (for "(linkdead)" indicator)
- `server/commands/look_command.py` (for "(linkdead)" indicator in look output)
- Room JSON data files (for rest locations)

**Test Files:**

- `server/tests/unit/realtime/test_disconnect_grace_period.py` (NEW)
- `server/tests/unit/commands/test_rest_command.py` (MODIFY)
- `server/tests/integration/test_rest_and_grace_period.py` (NEW)
- `server/tests/unit/realtime/test_visual_indicator.py` (NEW - for "(linkdead)" display)
