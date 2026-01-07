# Investigation Report: Delirium Respawn Bug

**Session ID**: 2025-12-07_session_001_delirium-respawn-bug
**Date**: 2025-12-07
**Investigator**: AI Agent (GPT-4)
**Bug Report**: When a player reaches -10 lucidity, they should be taken to a
respawn screen (different from the death respawn screen) and after
acknowledging their delirium, they should respawn in the Sanitarium with 10
lucidity.

## Executive Summary

**Root Cause Identified**: The delirium respawn feature is completely missing
from the codebase. There is no logic to:

1. Check for lucidity <= -10 threshold
2. Display a delirium-specific respawn screen
3. Move player to Sanitarium when lucidity hits -10
4. Set lucidity to 10 after delirium respawn acknowledgment

**Impact**:

- Players with lucidity <= -10 do not receive any special handling
- No delirium respawn screen exists (only death respawn screen exists)
- Players cannot respawn from delirium state in Sanitarium
- Missing critical game mechanic for lucidity management

**Status**: Root cause identified - feature is completely missing.
Comprehensive remediation prompt generated.

## Detailed Findings

### Phase 1: Bug Report Analysis

**Expected Behavior**:

- When player's lucidity reaches -10, they should:
  1. See a delirium respawn screen (different from death respawn screen)
  2. After acknowledging delirium, respawn in Sanitarium
  3. Have lucidity set to 10 after respawn

**Actual Behavior**:

- No special handling occurs when lucidity reaches -10
- Players remain in their current state with negative lucidity
- No delirium respawn screen is shown
- No automatic respawn to Sanitarium occurs

### Phase 2: System State Investigation

#### Lucidity Storage and Range

**Location**: `server/models/lucidity.py`

**Findings**:

- Lucidity is stored in `player_lucidity` table with `current_lcd` field
- Range: -100 to 100 (database constraint: `CHECK (current_lcd BETWEEN -100
  AND 100)`)
- Current tier system: `lucid` (>=70), `uneasy` (>=40), `fractured` (>=20),
  `deranged` (>=1), `catatonic` (<=0)

**Code Reference**:

```29:29:server/models/lucidity.py
        CheckConstraint("current_lcd BETWEEN -100 AND 100", name="ck_player_lucidity_range"),
```

```45:55:server/services/lucidity_service.py
def resolve_tier(lucidity_value: int) -> Tier:
    """Derive tier label based on LCD thresholds."""
    if lucidity_value >= 70:
        return "lucid"
    if lucidity_value >= 40:
        return "uneasy"
    if lucidity_value >= 20:
        return "fractured"
    if lucidity_value >= 1:
        return "deranged"
    return "catatonic"
```

#### Current Lucidity Threshold Checks

**Location**: `server/services/lucidity_service.py`

**Findings**:

- **-100 Threshold Check EXISTS**: Line 306 checks for `new_lcd <= -100` and
  triggers "sanitarium failover"
- **-10 Threshold Check MISSING**: No check exists for lucidity <= -10 to
  trigger delirium respawn

**Code Reference**:

```306:319:server/services/lucidity_service.py
        if new_lcd <= -100 and previous_lcd > -100 and self._catatonia_observer:
            logger.error(
                "Sanitarium failover triggered",
                player_id=player_id,
                previous_lcd=previous_lcd,
                lcd=new_lcd,
            )
            self._catatonia_observer.on_sanitarium_failover(player_id=player_id, current_lcd=new_lcd)
            await send_rescue_update_event(
                player_id=str(player_id),
                status="sanitarium",
                current_lcd=new_lcd,
                message="Orderlies whisk you to Arkham Sanitarium for observation.",
            )
```

**Analysis**: The system only checks for -100 threshold (extreme delirium),
but not for -10 threshold (delirium respawn trigger).

### Phase 3: Code Analysis

#### Respawn Screen Components

**Location**: `client/src/components/DeathInterstitial.tsx`

**Findings**:

- **Death Respawn Screen EXISTS**: `DeathInterstitial` component handles death
  respawn
- **Delirium Respawn Screen MISSING**: No `DeliriumInterstitial` component
  exists

**Code Reference**:

```4:58:client/src/components/DeathInterstitial.tsx
interface DeathInterstitialProps {
  isVisible: boolean;
  deathLocation: string;
  onRespawn: () => void;
  isRespawning?: boolean;
}

export const DeathInterstitial: React.FC<DeathInterstitialProps> = ({
  isVisible,
  deathLocation,
  onRespawn,
  isRespawning = false,
}) => {
  if (!isVisible) {
    return null;
  }

  return (
    <div className="death-interstitial-overlay">
      <div className="death-interstitial-container">
        <div className="death-interstitial-content">
          <h1 className="death-title">THE THRESHOLD CROSSED</h1>

          <div className="death-narrative">
            <p>
              The darkness consumes you utterly, and for a timeless moment,
              you drift through the spaces between worlds. Whispers in
              languages older than humanity echo around you, speaking of
              things mortal minds were never meant to comprehend.
            </p>

            <p>
              But the threads binding you to the waking world are not yet severed. The sanitarium calls you back from
              the threshold of oblivion...
            </p>
          </div>

          <div className="death-location">
            <p className="death-location-label">You perished at:</p>
            <p className="death-location-name">{deathLocation || 'Unknown Location'}</p>
          </div>

          <button className="respawn-button" onClick={onRespawn} disabled={isRespawning}>
            {isRespawning ? 'Returning to the mortal realm...' : 'Rejoin the earthly plane'}
          </button>

          {isRespawning && (
            <div className="respawn-loading">
              <p>The veil between worlds parts...</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
```

**Analysis**: Only death respawn screen exists. No delirium-specific screen component.

#### Client-Side Death Detection

**Location**: `client/src/components/ui-v2/GameClientV2Container.tsx`

**Findings**:

- **Death Detection EXISTS**: Lines 1260-1287 check for HP <= -10 to show
  death screen
- **Delirium Detection MISSING**: No check for lucidity <= -10 to show
  delirium screen

**Code Reference**:

```1260:1287:client/src/components/ui-v2/GameClientV2Container.tsx
  // Check if player is dead based on HP or room location
  useEffect(() => {
    const player = gameState.player;
    if (!player) return;

    const currentHp = player.stats?.current_health ?? 0;
    const roomId = gameState.room?.id;
    const isInLimbo = roomId === 'limbo_death_void_limbo_death_void';

    // Player is dead if HP <= -10 or in limbo
    if (currentHp <= -10 || isInLimbo) {
      if (!isDead) {
        setIsDead(true);
        logger.info('GameClientV2Container', 'Player detected as dead', {
          currentHp,
          roomId,
          isInLimbo,
        });
      }
    } else if (isDead && currentHp > -10 && !isInLimbo) {
      // Player is no longer dead
      setIsDead(false);
      logger.info('GameClientV2Container', 'Player detected as alive', {
        currentHp,
        roomId,
      });
    }
  }, [gameState.player, gameState.room, isDead]);
```

**Analysis**: Client checks for death state (HP <= -10) but does not check
for delirium state (lucidity <= -10).

#### Respawn Service

**Location**: `server/services/player_respawn_service.py`

**Findings**:

- **Death Respawn EXISTS**: `respawn_player()` method handles death respawn
- **Delirium Respawn MISSING**: No method exists for delirium respawn
- **Default Respawn Room**: `DEFAULT_RESPAWN_ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"`

**Code Reference**:

```21:22:server/services/player_respawn_service.py
# Default respawn location (Arkham Sanitarium foyer)
DEFAULT_RESPAWN_ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"
```

```136:178:server/services/player_respawn_service.py
    async def respawn_player(self, player_id: uuid.UUID, session: AsyncSession) -> bool:
        """
        Respawn a dead player at their respawn location with full HP.

        This method:
        1. Restores player HP to their max_health (not hardcoded 100)
        2. Moves player from limbo to respawn room
        3. Publishes respawn event for UI updates

        Args:
            player_id: ID of the player to respawn
            session: Database session for player data access

        Returns:
            True if respawn was successful, False otherwise
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for respawn", player_id=player_id)
                return False

            # Get respawn room using async API
            respawn_room = await self.get_respawn_room(player_id, session)

            # Get current stats and restore HP to max health
            stats = player.get_stats()
            old_hp = stats.get("current_health", -10)
            max_hp = stats.get("max_health", 100)  # Default to 100 if max_health not found
            stats["current_health"] = max_hp  # Restore to max health, not hardcoded 100

            # BUGFIX: Restore posture to standing when player respawns
            # As documented in "Resurrection and Corporeal Restoration" - Dr. Armitage, 1930
            # Upon resurrection, the body is restored to full function including upright posture
            stats["position"] = PositionState.STANDING

            # Update player stats and location
            player.set_stats(stats)
            old_room = player.current_room_id
            player.current_room_id = respawn_room  # type: ignore[assignment]
```

**Analysis**: Respawn service only handles death respawn (HP restoration). No
delirium respawn logic exists (lucidity restoration to 10).

### Phase 4: Evidence Collection

#### Missing Components Summary

1. **Server-Side**:
   - No check for lucidity <= -10 in `LucidityService.apply_lucidity_adjustment()`
   - No delirium respawn method in `PlayerRespawnService`
   - No delirium respawn API endpoint
   - No delirium state tracking (similar to death state)

2. **Client-Side**:
   - No `DeliriumInterstitial` component
   - No delirium state detection in `GameClientV2Container`
   - No delirium respawn event handling
   - No delirium state management

3. **Database**:
   - No delirium-specific fields or tracking
   - Lucidity can go negative (down to -100) but no special handling at -10

#### Existing Similar Functionality

**Death Respawn System** (for reference):

- Server: `PlayerDeathService.handle_player_death()` moves player to limbo
- Server: `PlayerRespawnService.respawn_player()` handles respawn
- Client: `DeathInterstitial` component displays death screen
- Client: `GameClientV2Container` detects death state (HP <= -10)
- API: `/api/players/respawn` endpoint handles respawn request

**Analysis**: Death respawn system provides a template for delirium respawn implementation.

### Phase 5: Analysis and Reporting

## Root Cause Analysis

**PRIMARY ROOT CAUSE**: The delirium respawn feature was never implemented.
The codebase contains:

- Death respawn system (HP <= -10)
- Lucidity system with tier tracking
- Sanitarium failover at -100 lucidity
- But NO delirium respawn at -10 lucidity

**SECONDARY ISSUES**:

1. **Missing Threshold Check**: No code checks for lucidity <= -10 to trigger
   delirium respawn
2. **Missing UI Component**: No delirium-specific respawn screen exists
3. **Missing Server Logic**: No method to handle delirium respawn (move to
   Sanitarium, set lucidity to 10)
4. **Missing Client Detection**: Client doesn't detect delirium state
   (lucidity <= -10)
5. **Missing API Endpoint**: No API endpoint for delirium respawn
   acknowledgment

## System Impact Assessment

**Scope**:

- **Affected Systems**: Lucidity system, respawn system, client UI, game
  state management
- **Affected Players**: All players who reach -10 lucidity
- **Severity**: High - Missing critical game mechanic

**Impact**:

- Players cannot recover from delirium state through respawn
- No visual feedback when lucidity reaches -10
- Missing gameplay mechanic for lucidity management
- Inconsistent with death respawn system (which works correctly)

**Dependencies**:

- Requires changes to: `LucidityService`, `PlayerRespawnService`, client
  components, API endpoints
- Must integrate with existing respawn system
- Must follow same patterns as death respawn system

## Evidence Documentation

### Code References

1. **Lucidity Service** - Missing -10 check:
   - File: `server/services/lucidity_service.py`
   - Lines: 238-378 (apply_lucidity_adjustment method)
   - Issue: Only checks for -100 threshold, not -10

2. **Respawn Service** - Missing delirium respawn:
   - File: `server/services/player_respawn_service.py`
   - Lines: 136-178 (respawn_player method)
   - Issue: Only handles death respawn, not delirium respawn

3. **Client Container** - Missing delirium detection:
   - File: `client/src/components/ui-v2/GameClientV2Container.tsx`
   - Lines: 1260-1287 (death detection useEffect)
   - Issue: Only checks for death state, not delirium state

4. **Death Interstitial** - Only death screen exists:
   - File: `client/src/components/DeathInterstitial.tsx`
   - Lines: 4-58 (component definition)
   - Issue: No delirium-specific screen component

### Database Schema

- **Table**: `player_lucidity`
- **Field**: `current_lcd` (INTEGER, range: -100 to 100)
- **Constraint**: `CHECK (current_lcd BETWEEN -100 AND 100)`
- **Issue**: Schema supports negative lucidity but no special handling at
  -10

## Investigation Recommendations

**PRIORITY 1 - Critical**:

1. Implement delirium threshold check in
   `LucidityService.apply_lucidity_adjustment()`
2. Create `DeliriumInterstitial` component (similar to `DeathInterstitial`)
3. Add delirium respawn method to `PlayerRespawnService`
4. Add delirium state detection in `GameClientV2Container`

**PRIORITY 2 - High**:
5. Create delirium respawn API endpoint
6. Add delirium respawn event types
7. Integrate with existing respawn system
8. Add tests for delirium respawn flow

**PRIORITY 3 - Medium**:
9. Add delirium state tracking (similar to death state)
10. Update documentation for delirium respawn mechanic
11. Add logging for delirium respawn events

## Remediation Prompt

**For Cursor Chat**:

```text
Implement delirium respawn feature: When a player's lucidity reaches -10,
they should be taken to a delirium respawn screen (different from the death
respawn screen) and after acknowledging their delirium, they should respawn
in the Sanitarium with 10 lucidity.

REQUIREMENTS:
1. Server-Side:
   - Add lucidity <= -10 check in
     LucidityService.apply_lucidity_adjustment()
   - Create delirium respawn method in PlayerRespawnService (similar to
     respawn_player but sets lucidity to 10)
   - Add delirium respawn API endpoint (similar to /api/players/respawn)
   - Move player to Sanitarium
     (earth_arkhamcity_sanitarium_room_foyer_001) on delirium respawn
   - Set lucidity to 10 after delirium respawn acknowledgment

2. Client-Side:
   - Create DeliriumInterstitial component (similar to DeathInterstitial but
     with delirium-specific narrative)
   - Add delirium state detection in GameClientV2Container (check lucidity
     <= -10)
   - Add delirium respawn event handling
   - Integrate with existing respawn system

3. Integration:
   - Follow same patterns as death respawn system
   - Use existing respawn service infrastructure
   - Maintain consistency with death respawn UI/UX

4. Testing:
   - Add unit tests for delirium respawn logic
   - Add integration tests for delirium respawn flow
   - Test delirium screen display and respawn functionality

REFERENCE IMPLEMENTATION:
- Death respawn system: server/services/player_respawn_service.py,
  client/src/components/DeathInterstitial.tsx
- Lucidity service: server/services/lucidity_service.py (check -100
  threshold logic)
- Death detection: client/src/components/ui-v2/GameClientV2Container.tsx
  (lines 1260-1287)

```text

---

**Investigation Complete**: Root cause identified - feature is completely
missing. Comprehensive remediation prompt generated for implementation.
