---
name: Login Grace Period Implementation
overview: Implement a 10-second login grace period system that provides immunity to damage and negative effects, prevents combat initiation, and makes hostile NPCs ignore players during initial login. The grace period applies only to new logins (through /select-character), not to reconnections after network disconnects.
todos:
  - id: create_login_grace_period_module
    content: Create server/realtime/login_grace_period.py with start/cancel/check functions
    status: completed
  - id: add_connection_manager_tracking
    content: Add login_grace_period_players dict to ConnectionManager.__init__
    status: in_progress
  - id: start_grace_period_after_motd
    content: Start grace period after MOTD dismissal (not during initial connection setup)
    status: pending
  - id: create_grace_period_start_handler
    content: Create WebSocket message handler or API endpoint to start grace period when MOTD dismissed
    status: pending
  - id: remove_combat_on_login
    content: Remove player from combat state if in combat when logging in
    status: pending
  - id: block_combat_commands
    content: Block combat commands (attack, etc.) during grace period in combat.py
    status: pending
  - id: prevent_combat_initiation
    content: Prevent combat.start_combat() if either participant is in grace period
    status: pending
  - id: block_damage_application
    content: Block damage application in combat_attack_handler.py and combat_integration.py
    status: pending
  - id: block_negative_effects
    content: Block negative status effects in spell_effects.py and game_tick_processing.py
    status: pending
  - id: prevent_npc_targeting
    content: Prevent NPCs from targeting players in grace period in aggressive_mob_npc.py
    status: pending
  - id: prevent_npc_attacks
    content: Prevent NPC attacks on players in grace period in npc_combat_integration_service.py
    status: pending
  - id: add_visual_indicator_warded
    content: Add "(warded)" visual indicator to player names in room lists, look commands, and occupant updates (similar to linkdead)
    status: pending
  - id: add_grace_period_to_game_state
    content: Include grace period status and remaining time in game state sent to client
    status: pending
  - id: add_grace_period_countdown_function
    content: Add get_login_grace_period_remaining() function to calculate remaining time
    status: pending
  - id: create_client_countdown_banner
    content: Create LoginGracePeriodBanner component to display countdown to player
    status: pending
  - id: integrate_countdown_in_game_client
    content: Integrate grace period countdown banner into GameClientV2Container
    status: pending
  - id: add_grace_period_countdown_function
    content: Add get_login_grace_period_remaining() function to calculate remaining time
    status: pending
  - id: create_client_countdown_banner
    content: Create LoginGracePeriodBanner component to display countdown to player
    status: pending
  - id: integrate_countdown_in_game_client
    content: Integrate grace period countdown banner into GameClientV2Container
    status: pending
  - id: write_unit_tests
    content: Write unit tests for login grace period functions (must achieve 70%+ coverage)
    status: completed
  - id: write_integration_tests
    content: Write integration tests for full login grace period flow
    status: completed
  - id: verify_test_coverage
    content: Verify all new code meets 70% minimum test coverage requirement
    status: pending
---

# Login Grace Period Implementation Plan

## Overview

Implement a 10-second grace period system that activates when a player logs in through the `/select-character` endpoint. During this period:

- Players are immune to all damage and negative status effects
- Players cannot initiate combat
- Hostile NPCs/mobs ignore players
- Players can move freely
- Players are removed from combat if they're in combat state on login

## Architecture

### New Module: `server/realtime/login_grace_period.py`

Similar to the existing `disconnect_grace_period.py`, create a new module to manage login grace periods:

- `start_login_grace_period(player_id, manager)` - Start 10-second grace period
- `cancel_login_grace_period(player_id, manager)` - Cancel grace period early (if needed)
- `is_player_in_login_grace_period(player_id, manager)` - Check if player is in grace period

### Connection Manager Updates

Add to `ConnectionManager`:

- `login_grace_period_players: dict[uuid.UUID, asyncio.Task]` - Track active grace periods

### Login Detection and Grace Period Start Timing

**Key Insight**: New logins go through `/select-character` → `handle_new_game_session_impl` → WebSocket connection → `handle_new_connection_setup` → MOTD screen → Player clicks "Enter the Realm" → Grace period starts

**CRITICAL**: Grace period should start AFTER MOTD dismissal, not during initial connection setup.

**Implementation**:

1. In `handle_new_game_session_impl` (called during `/select-character`), mark that this player should receive a login grace period (store flag/timestamp)
2. In `handle_new_connection_setup`, do NOT start grace period - only mark player as eligible
3. When player dismisses MOTD (`handleMotdContinue` in client), send message to server to start grace period
4. Server validates player is eligible and starts grace period
5. Use `is_new_connection` flag from `track_player_connected_impl` to distinguish new logins from reconnections

## Implementation Details

### 1. Login Grace Period Module (`server/realtime/login_grace_period.py`)

```python
LOGIN_GRACE_PERIOD_DURATION = 10.0  # 10 seconds

async def start_login_grace_period(player_id: uuid.UUID, manager: Any) -> None:
    """Start login grace period for a player."""
    # Similar pattern to disconnect_grace_period.py
    # Create async task that waits 10 seconds then removes player from tracking

def is_player_in_login_grace_period(player_id: uuid.UUID, manager: Any) -> bool:
    """Check if player is in login grace period."""
    # Check if player_id in manager.login_grace_period_players
```

### 2. Connection Manager Initialization

Update `ConnectionManager.__init__` in `server/realtime/connection_manager.py`:

- Add `self.login_grace_period_players: dict[uuid.UUID, asyncio.Task] = {}`

### 3. Start Grace Period After MOTD Dismissal

**CRITICAL**: Grace period should NOT start during initial connection setup. It should start only after the player clicks through the MOTD screen to enter the game.

**Location**: `client/src/App.tsx`

In `handleMotdContinue` (around line 444):

- After setting `setShowMotd(false)` and before rendering game client
- Send WebSocket message or API call to server to start login grace period
- Message type: `start_login_grace_period` or similar
- Include `player_id` in the message

**Location**: `server/realtime/websocket_handler.py` or `server/api/real_time.py`

Handle grace period start request:

- Create new WebSocket message handler or API endpoint: `handle_start_login_grace_period`
- Validate player is connected and authenticated
- Check if player should receive grace period (new login, not reconnection)
- Call `start_login_grace_period(player_id, manager)`
- Remove player from combat if they're in combat state
- Return confirmation to client

**Alternative Approach** (if WebSocket message handling is complex):

- Create API endpoint: `POST /api/players/{player_id}/start-login-grace-period`
- Call this endpoint from `handleMotdContinue` in client
- Server validates and starts grace period

**Location**: `server/realtime/player_connection_setup.py`

**CHANGE**: Do NOT start grace period in `handle_new_connection_setup`. Instead:

- Only mark that player is eligible for grace period (store flag or timestamp)
- Actual grace period start happens when MOTD is dismissed

### 4. Combat Prevention

**Location**: `server/commands/combat.py`

In `handle_attack_command`:

- Check `is_player_in_login_grace_period()` before processing attack
- Return error message if in grace period

**Location**: `server/services/combat_service.py`

In `start_combat`:

- Check if attacker or target is in login grace period
- Prevent combat initiation if either participant is in grace period

### 5. Damage Prevention

**Location**: `server/services/combat_attack_handler.py`

In `_apply_damage`:

- Check if target is in login grace period
- Skip damage application if in grace period (return 0 damage)

**Location**: `server/services/combat_service.py`

In `process_attack`:

- Check if target is in login grace period before applying damage

**Location**: `server/npc/combat_integration.py`

In `_apply_player_combat_effects`:

- Check if target is in login grace period
- Skip damage application if in grace period

### 6. Status Effect Prevention

**Location**: `server/game/magic/spell_effects.py`

In `_process_status_effect`:

- Check if target is in login grace period
- Skip negative status effects if in grace period
- Allow positive effects (healing, buffs) to proceed

**Location**: `server/app/game_tick_processing.py`

In `_process_player_status_effects`:

- Check if player is in login grace period
- Skip processing negative effects if in grace period

### 7. NPC Targeting Prevention

**Location**: `server/npc/aggressive_mob_npc.py`

In `hunt_target` and `attack_target`:

- Check if target is in login grace period
- Skip targeting if target is in grace period

**Location**: `server/services/npc_combat_integration_service.py`

In `handle_player_attack_on_npc`:

- Check if player is in login grace period
- Prevent attack if player is in grace period

**Location**: NPC behavior engine (where NPCs select targets):

- Filter out players in login grace period from target lists

### 8. Combat State Cleanup on Login

**Location**: `server/realtime/player_connection_setup.py`

In `handle_new_connection_setup`:

- Check if player is in combat
- If in combat, end combat gracefully (use `CombatService.end_combat`)
- Log the cleanup action

### 9. Visual Indicator (Similar to Linkdead)

**REQUIRED**: Add "(warded)" indicator to player names when they are in login grace period, similar to how "(linkdead)" is shown for disconnect grace period.

**Location**: `server/realtime/integration/game_state_provider.py`

In `_filter_other_players` (around line 218):

- Check if player is in login grace period using `is_player_in_login_grace_period()`
- Append "(warded)" to player name if in grace period
- Note: Check for both linkdead and warded, show both if applicable (though they shouldn't overlap)

**Location**: `server/realtime/player_occupant_processor.py`

In `process_player_occupant` (around line 101):

- Check if player is in login grace period
- Append "(warded)" to player name if in grace period
- Similar pattern to linkdead indicator

**Location**: `server/commands/look_room.py`

In `_format_player_look_display` (around line 97):

- Check if player is in login grace period
- Append "(warded)" to player name in look command output

**Location**: `server/commands/look_player.py`

In look player command (around line 132):

- Check if target player is in login grace period
- Append "(warded)" to player name in look output

**Location**: `server/realtime/websocket_room_updates.py`

In room update handlers (around line 40):

- Check if player is in login grace period
- Append "(warded)" to player name in room occupant updates

### 10. Client Updates

**REQUIRED**: The connecting player must see a countdown timer showing when their immunity/warding will end.

**Location**: `server/realtime/integration/game_state_provider.py`

In `_send_initial_game_state`:

- Include `login_grace_period_active: bool` and `login_grace_period_remaining: float` (seconds remaining) in game state
- Calculate remaining time: `LOGIN_GRACE_PERIOD_DURATION - elapsed_time_since_start`
- Send updates periodically (or on each game state update) to keep countdown accurate

**Location**: `server/realtime/login_grace_period.py`

In `start_login_grace_period`:

- Store start timestamp for each player's grace period
- Provide function to get remaining time: `get_login_grace_period_remaining(player_id, manager) -> float`

**Location**: Client-side - `client/src/components/ui-v2/GameClientV2Container.tsx` or similar

Add grace period countdown display:

- Create state to track grace period status: `loginGracePeriodRemaining: number | null`
- Listen for grace period updates in game state events
- Display countdown banner/indicator similar to other status banners (like IncapacitatedBanner)
- Show countdown in format: "Warded: X.Xs remaining" or "Immune: X.Xs remaining"
- Update countdown every second (or on game state updates)
- Hide when grace period expires or reaches 0

**Location**: Client-side - Create new component (optional but recommended)

Create `client/src/components/ui-v2/LoginGracePeriodBanner.tsx`:

- Similar to `IncapacitatedBanner.tsx` or `RescueStatusBanner.tsx`
- Display countdown timer with Mythos-themed styling
- Show warning/warded icon
- Auto-hide when grace period expires
- **CRITICAL**: Position prominently but non-intrusively - must NOT interfere with command input or movement commands
- Position at top of screen or near status panels (away from command input area)
- Use absolute/fixed positioning that doesn't block input fields
- Ensure banner is visually distinct but doesn't capture focus or block keyboard input
- Banner should be informational only - player must be able to type movement commands normally
- Follow same pattern as `IncapacitatedBanner.tsx` which displays above game content without blocking input

## Testing Strategy

**CRITICAL REQUIREMENT**: All new code must meet the **70% minimum test coverage target**. Test coverage will be verified using the project's coverage tools before considering the implementation complete.

### Unit Tests

1. `server/tests/unit/realtime/test_login_grace_period.py`

   - Test grace period start/cancel/check functions
   - Test grace period expiration
   - Test grace period task cancellation
   - Test concurrent grace periods for multiple players
   - **Target Coverage**: 90%+ for login_grace_period.py module

2. `server/tests/unit/commands/test_combat_grace_period.py`

   - Test combat commands blocked during grace period
   - Test error messages returned
   - Test all combat command paths with grace period checks
   - **Target Coverage**: 70%+ for modified combat command code paths

3. `server/tests/unit/services/test_damage_grace_period.py`

   - Test damage blocked during grace period
   - Test status effects blocked during grace period
   - Test positive effects allowed during grace period
   - Test all damage application paths with grace period checks
   - **Target Coverage**: 70%+ for modified damage/effect code paths

4. `server/tests/unit/npc/test_npc_grace_period.py` (if needed)

   - Test NPC targeting prevention during grace period
   - Test NPC attack prevention during grace period
   - **Target Coverage**: 70%+ for modified NPC code paths

5. `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

   - Test "(warded)" indicator added to player names in room lists
   - Test "(warded)" indicator in look command output
   - Test "(warded)" indicator in occupant updates
   - Test indicator removed when grace period expires
   - Test indicator not shown for reconnections
   - **Target Coverage**: 70%+ for visual indicator code paths

### Integration Tests

1. `server/tests/integration/test_login_grace_period_flow.py`

   - Test full login flow with grace period
   - Test grace period starts AFTER MOTD dismissal (not during connection setup)
   - Test grace period doesn't start if MOTD is not dismissed
   - Test grace period doesn't apply to reconnections
   - Test combat cleanup when grace period starts
   - Test NPCs ignore players during grace period
   - Test grace period expiration and cleanup
   - Test multiple players with grace periods simultaneously
   - Test grace period remaining time calculation accuracy
   - **Target Coverage**: All critical integration paths covered

2. Client-side tests (if test framework available):

   - Test LoginGracePeriodBanner component renders correctly
   - Test countdown updates correctly
   - Test banner hides when grace period expires
   - Test banner doesn't show for reconnections

### Coverage Verification

- Run coverage analysis after implementation: `make test` (or equivalent coverage command)
- Verify all new files meet 70% minimum coverage
- Verify modified files maintain or improve existing coverage
- Address any coverage gaps before marking implementation complete

## Files to Modify

### New Files

- `server/realtime/login_grace_period.py` - Grace period management
- `server/tests/unit/realtime/test_login_grace_period.py` - Unit tests
- `server/tests/integration/test_login_grace_period_flow.py` - Integration tests

### Modified Files

**Server-side:**

- `server/realtime/connection_manager.py` - Add `login_grace_period_players` tracking
- `server/realtime/player_connection_setup.py` - Start grace period on login, remove from combat
- `server/commands/combat.py` - Block combat commands during grace period
- `server/services/combat_service.py` - Prevent combat initiation during grace period
- `server/services/combat_attack_handler.py` - Block damage during grace period
- `server/npc/combat_integration.py` - Block NPC damage during grace period
- `server/game/magic/spell_effects.py` - Block negative effects during grace period
- `server/app/game_tick_processing.py` - Skip negative effect processing during grace period
- `server/npc/aggressive_mob_npc.py` - Skip targeting players in grace period
- `server/services/npc_combat_integration_service.py` - Prevent NPC attacks during grace period
- `server/realtime/integration/game_state_provider.py` - Add "(warded)" indicator and include grace period status + remaining time in game state
- `server/realtime/player_occupant_processor.py` - Add "(warded)" indicator to player names
- `server/commands/look_room.py` - Add "(warded)" indicator in look command output
- `server/commands/look_player.py` - Add "(warded)" indicator when looking at a player
- `server/realtime/websocket_room_updates.py` - Add "(warded)" indicator in room occupant updates

**Client-side:**

- `client/src/components/ui-v2/GameClientV2Container.tsx` - Add grace period state tracking and integrate countdown banner
- `client/src/components/ui-v2/GameClientV2.tsx` - Pass grace period state to child components if needed

## Edge Cases

1. **Player reconnects during grace period**: Grace period should continue (reconnection doesn't cancel it)
2. **Player logs in while in combat**: Remove from combat when grace period starts (after MOTD dismissal)
3. **Multiple logins in quick succession**: Each new login starts a new grace period (cancels previous)
4. **Grace period expires during combat attempt**: Combat should be blocked until grace period expires
5. **NPC already targeting player**: NPC should stop targeting when player enters grace period
6. **Visual indicator display**: "(warded)" should appear in all places where player names are shown (room lists, look commands, occupant updates)
7. **Visual indicator removal**: "(warded)" should be removed when grace period expires
8. **Multiple indicators**: If a player somehow has both linkdead and warded (shouldn't happen), both indicators should be shown
9. **Countdown banner non-interference**: Countdown banner must NOT block or interfere with command input, movement commands, or keyboard input - player must be able to type and move normally
10. **Banner positioning**: Banner should be positioned away from command input area (top of screen or status panel area), using absolute/fixed positioning that doesn't block input fields
11. **Countdown accuracy**: Countdown timer should update smoothly and accurately reflect remaining time
12. **Countdown expiration**: Countdown banner should automatically hide when grace period expires
13. **MOTD dismissal required**: Grace period should NOT start until player clicks through MOTD - if player disconnects before dismissing MOTD, no grace period should be active
14. **MOTD skip scenarios**: If MOTD is skipped or not shown, grace period should still start (handle edge case where MOTD might be bypassed)

## Notes

- Grace period duration is hardcoded to 10 seconds (can be made configurable later)
- Grace period is separate from disconnect grace period (they use different tracking dictionaries)
- Movement is explicitly allowed during grace period (no changes needed to movement commands)
- Positive effects (healing, buffs) are allowed during grace period
- **CRITICAL**: Grace period starts AFTER MOTD dismissal, not during initial connection setup - this ensures players have time to read MOTD before grace period begins

## Test Coverage Requirements

**MANDATORY**: All new code must achieve **70% minimum test coverage**. This includes:

- All new modules (`login_grace_period.py`)
- All modified functions/methods that include grace period checks
- All error handling paths
- All edge cases identified in the Edge Cases section

Coverage will be verified using the project's standard coverage tools before the implementation is considered complete. Any coverage gaps must be addressed with additional tests.
