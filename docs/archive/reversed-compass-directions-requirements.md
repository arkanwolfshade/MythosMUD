# Reversed Compass Directions Implementation Requirements

**Status**: Pending Implementation (Client-Side Display Feature)

**Last Updated**: 2026-01-02

**Related Documentation**: `docs/lucidity-system.md` (Section 5.1)

---

## Overview

Reversed compass directions are a hallucination effect for Deranged tier players. When a player's lucidity tier is "deranged", all compass directions displayed to them are reversed (north appears as south, east appears as west, etc.).

**Key Point**: This is a **visual hallucination only**. Movement commands remain unchanged - if a player types "go north", the server processes "north" correctly, but the client displays it as "south" in the UI.

---

## Specification Requirements

From `docs/lucidity-system.md` Section 5.1:

| Tier         | Hallucination Frequency   | Event Palette                     |
| ------------ | ------------------------- | --------------------------------- |
| **Deranged** | 45% chance per 20 seconds | ...reversed compass directions... |

**Key Points**:

- Active when player's lucidity tier is "deranged"
- Continuous effect (not a one-time event)
- Visual display only - does not affect movement logic
- All compass directions are reversed (north ↔ south, east ↔ west, etc.)

---

## Functional Requirements

### FR-1: Direction Reversal Logic

**FR-1.1: Primary Directions**

- north ↔ south
- east ↔ west

**FR-1.2: Compound Directions**

- northeast ↔ southwest
- northwest ↔ southeast

**FR-1.3: Vertical Directions**

- up ↔ down (reversed)
- in ↔ out (reversed, if applicable)

**FR-1.4: Unknown Directions**

- Any direction not in the standard set should pass through unchanged (defensive)

### FR-2: Activation Condition

**FR-2.1: Tier-Based Activation**

- Active when `lucidityStatus.tier === 'deranged'`
- Inactive for all other tiers (lucid, uneasy, fractured, catatonic)
- Should update immediately when tier changes (no delay)

### FR-3: Display Locations

**FR-3.1: Room Exit Display**

- RoomInfoPanel (exits list)
- LocationPanel (exits display)
- RoomExits component (exits display)
- RoomDetailsPanel (exits list)
- Any other UI components showing room exits

**FR-3.2: Command Echoes**

- When player types "go north", if displayed back to player, show as "south"
- Command history may show reversed directions (optional - can be original or reversed)

**FR-3.3: Look Commands**

- Direction look commands ("look north") may show reversed direction in output (optional)

### FR-4: Movement Logic (Unchanged)

**FR-4.1: Server-Side Processing**

- Movement commands use original directions (not reversed)
- Player types "go north" → server processes "north" → player moves north correctly
- Server-side logic is unaffected by visual reversal

---

## Implementation Approach

### Client-Side Implementation (Primary)

**Location**: `client/src/utils/directionUtils.ts` (new file)

Create a utility module with:

```typescript
// Direction reversal map for Deranged tier
const DIRECTION_REVERSAL_MAP: Record<string, string> = {
  north: 'south',
  south: 'north',
  east: 'west',
  west: 'east',
  northeast: 'southwest',
  southwest: 'northeast',
  northwest: 'southeast',
  southeast: 'northwest',
  up: 'down',
  down: 'up',
  in: 'out',
  out: 'in',
};

/**
 * Reverse a direction if player is in Deranged tier.
 *
 * @param direction - Original direction (e.g., "north")
 * @param tier - Current lucidity tier
 * @returns Reversed direction if tier is "deranged", original otherwise
 */
export function getDisplayDirection(direction: string, tier: string): string {
  if (tier !== 'deranged') {
    return direction;
  }
  return DIRECTION_REVERSAL_MAP[direction.toLowerCase()] || direction;
}

/**
 * Reverse multiple directions for display.
 *
 * @param directions - Array of directions or object keys (directions)
 * @param tier - Current lucidity tier
 * @returns Reversed directions if tier is "deranged", original otherwise
 */
export function reverseDirectionsForDisplay(directions: string[] | Record<string, any>, tier: string): string[] {
  if (tier !== 'deranged') {
    return Array.isArray(directions) ? directions : Object.keys(directions);
  }

  const dirs = Array.isArray(directions) ? directions : Object.keys(directions);
  return dirs.map(dir => DIRECTION_REVERSAL_MAP[dir.toLowerCase()] || dir);
}
```

**Integration Points**:

1. **RoomInfoPanel.tsx** - Reverse directions when displaying exits
2. **LocationPanel.tsx** - Reverse directions in exits display
3. **RoomExits component** - Reverse directions in exit labels
4. **RoomDetailsPanel.tsx** - Reverse directions in exits list

**Example Integration**:

```typescript
// In RoomInfoPanel.tsx or similar
import { getDisplayDirection } from '@/utils/directionUtils';

// Get lucidity tier from context/store
const lucidityTier = lucidityStatus?.tier || 'lucid';

// When rendering exits:
{Object.entries(room.exits)
  .filter(([_, destination]) => destination !== null)
  .map(([direction, _]) => getDisplayDirection(direction, lucidityTier))
  .map(direction => direction.charAt(0).toUpperCase() + direction.slice(1))
  .join(', ')}
```

### Server-Side Considerations

**No server-side changes required** for basic implementation. The server already:

- Sends lucidity tier information to client via `lucidity_change` events
- Processes movement commands correctly using original directions
- Room data includes exits with original direction keys

**Optional Enhancement**: If command echoes should show reversed directions, the server could check the player's tier before echoing movement commands. This is optional and not required for initial implementation.

---

## Testing Considerations

### Unit Tests

1. **Direction Reversal Logic**
   - Test all primary directions (north, south, east, west)
   - Test compound directions (northeast, southwest, etc.)
   - Test vertical directions (up, down)
   - Test unknown directions (pass through unchanged)
   - Test case insensitivity
   - Test inactive tier (returns original direction)

2. **Integration Tests**
   - Test direction reversal in RoomInfoPanel
   - Test direction reversal in LocationPanel
   - Test that movement commands still work correctly (server processes original direction)

### Manual Testing

1. Set player to Deranged tier (LCD < -50)
2. Enter a room with multiple exits
3. Verify directions are reversed in UI
4. Type "go north" - verify player moves north (correct direction) but UI shows "south"
5. Change tier to non-Deranged - verify directions return to normal

---

## Related Files

### Client-Side

- `client/src/utils/directionUtils.ts` - **NEW FILE** - Direction reversal utility
- `client/src/components/RoomInfoPanel.tsx` - Room exits display (needs integration)
- `client/src/components/ui/RoomInfo.tsx` - RoomExits component (needs integration)
- `client/src/components/ui-v2/panels/LocationPanel.tsx` - Exits display (needs integration)
- `client/src/components/map/RoomDetailsPanel.tsx` - Exits list (needs integration)
- `client/src/contexts/GameTerminalContext.tsx` - Lucidity status context
- `client/src/stores/gameStore.ts` - Game state store (lucidity tier access)

### Server-Side

- No changes required (tier information already sent to client)

---

## Implementation Status

### ✅ Completed

- Requirements documentation

### ❌ Not Yet Implemented

- Client-side direction reversal utility
- Integration into UI components showing exits
- Unit tests
- Manual testing

---

## Notes

- This is a **client-side only** feature - no server-side changes required
- Movement logic remains unchanged - players still move in the correct direction
- The reversal is purely visual/perceptual (hallucination effect)
- Should activate/deactivate immediately when tier changes
- Consider adding a visual indicator (e.g., color change, icon) to suggest directions are unreliable (optional enhancement)

---

## References

- `docs/lucidity-system.md` - Section 5.1 (Hallucination & Phantom Event Tables)
- `server/services/lucidity_event_dispatcher.py` - Lucidity change events
- `client/src/utils/lucidityEventUtils.ts` - Lucidity status handling
