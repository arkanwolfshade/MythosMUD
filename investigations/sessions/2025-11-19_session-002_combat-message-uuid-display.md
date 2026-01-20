# BUG INVESTIGATION REPORT: Combat Initiation Message Showing UUIDs Instead of Names

**Investigation Date**: 2025-11-19
**Investigator**: AI Assistant (GPT-4)
**Session ID**: 2025-11-19_session-002_combat-message-uuid-display
**Bug Type**: Client-Side Display Issue - Data Formatting

---

## Executive Summary

Combat initiation messages display participant UUIDs instead of player/NPC names in the turn order. The message currently shows: "Combat has begun! Turn order: 9bcee4bf-43dc-4860-885a-1be5356b5a24, d839d857-1601-45dc-ac16-0960e034a52e" instead of displaying human-readable names like "ArkanWolfshade, Ithaqua".

**Affected Component**: Client-side event processing in `GameTerminalWithPanels.tsx`

**Severity**: Medium - Functional issue that degrades user experience but does not break core functionality

---

## Detailed Findings

### 1. Bug Description

**User Report**: Combat initiation should print the attacker and target names, not IDs. The message shows:

```
"Combat has begun! Turn order: 9bcee4bf-43dc-4860-885a-1be5356b5a24, d839d857-1601-45dc-ac16-0960e034a52e"
```

**Expected Behavior**: The message should display participant names, e.g.:

```
"Combat has begun! Turn order: ArkanWolfshade, Ithaqua"
```

### 2. System State Investigation

#### 2.1 Client-Side Message Generation

**Location**: `client/src/components/GameTerminalWithPanels.tsx` line 1540

**Current Implementation**:

```1540:1540:client/src/components/GameTerminalWithPanels.tsx
const message = `Combat has begun! Turn order: ${turnOrder.join(', ')}`;
```

**Issue**: The `turnOrder` array contains UUID strings (e.g., `["9bcee4bf-...", "d839d857-..."]`) that are directly joined without converting to participant names.

#### 2.2 Event Data Structure

**Location**: `client/src/components/GameTerminalWithPanels.tsx` lines 1514-1518

**Event Data Received**:

```1514:1518:client/src/components/GameTerminalWithPanels.tsx
case 'combat_started': {
  console.log('🔍 DEBUG: combat_started event received!', event);
  const combatId = event.data.combat_id as string;
  const turnOrder = Array.isArray(event.data.turn_order) ? (event.data.turn_order as string[]) : [];
  const participants = event.data.participants as Record<string, CombatParticipant> | undefined;
```

**Available Data**:

- `turnOrder`: Array of UUID strings (e.g., `["9bcee4bf-...", "d839d857-..."]`)
- `participants`: Dictionary mapping UUID strings to participant objects containing names
  - Example structure: `{"9bcee4bf-...": {"name": "ArkanWolfshade", "hp": 100, "max_hp": 100}, ...}`

**Key Finding**: The `participants` dictionary is available but **not being used** to convert UUIDs to names when generating the message.

### 3. Server-Side Data Flow

#### 3.1 Combat Event Creation

**Location**: `server/services/combat_service.py` lines 204-211

**Event Creation**:

```204:211:server/services/combat_service.py
started_event = CombatStartedEvent(
    combat_id=combat.combat_id,
    room_id=room_id,
    participants={
        str(p.participant_id): {"name": p.name, "hp": p.current_hp, "max_hp": p.max_hp}
        for p in combat.participants.values()
    },
    turn_order=[str(pid) for pid in combat.turn_order],
)
```

**Analysis**:

- Server correctly creates `participants` dict with UUID strings as keys and participant data (including `name`) as values
- Server correctly creates `turn_order` as list of UUID strings
- Both data structures are sent to the client via NATS events

#### 3.2 Event Schema

**Location**: `server/events/combat_events.py` lines 16-23

**Schema Definition**:

```16:23:server/events/combat_events.py
@dataclass
class CombatStartedEvent(BaseEvent):
    """Event fired when combat begins."""

    combat_id: UUID
    room_id: str
    participants: dict[str, Any]  # participant info
    turn_order: list[str]
```

**Analysis**: Schema correctly defines both `participants` (dict) and `turn_order` (list of strings/UUIDs). Server implementation matches schema.

#### 3.3 Event Publishing

**Location**: `server/services/combat_event_publisher.py` lines 154-160

**Event Data Packaging**:

```154:160:server/services/combat_event_publisher.py
event_data = {
    "combat_id": combat_id,
    "room_id": room_id,
    "participants": event.participants,
    "turn_order": event.turn_order,
    "timestamp": event.timestamp.isoformat(),
}
```

**Analysis**: Server correctly packages both `participants` and `turn_order` in the event data sent to clients via NATS.

### 4. Root Cause Analysis

#### 4.1 Primary Cause

**Root Cause**: Client-side message generation directly joins UUID strings from `turnOrder` array without converting them to participant names using the available `participants` dictionary.

**Technical Details**:

1. Server sends correct data structure:

   - `turn_order`: `["9bcee4bf-...", "d839d857-..."]`
   - `participants`: `{"9bcee4bf-...": {"name": "ArkanWolfshade", ...}, "d839d857-...": {"name": "Ithaqua", ...}}`

2. Client correctly extracts both data structures (lines 1517-1518)

3. Client fails to use `participants` dict to convert UUIDs to names when generating message (line 1540)

#### 4.2 Missing Logic

The client has access to:

- `turnOrder`: Array of UUID strings representing turn order
- `participants`: Dictionary mapping UUID strings to participant objects with `name` property

But the message generation code does not:

- Map each UUID in `turnOrder` to the corresponding participant name from `participants` dict
- Handle cases where participant might not be found (graceful fallback)
- Use the available `name` property from participant objects

#### 4.3 Code Pattern Evidence

**Evidence from Similar Code**: The client code already has a helper function `isPlayerCombatParticipant` (line 164) that demonstrates understanding of how to use the `participants` dict, showing the pattern is known but not applied to message generation.

### 5. System Impact Assessment

#### 5.1 User Experience Impact

**Severity**: Medium

**Impact**:

**Readability**: UUIDs are not human-readable, making it difficult for players to understand turn order

**Immersion**: Breaks game immersion by exposing technical identifiers

**Usability**: Players cannot easily identify which combatant acts next

**Affected Users**: All players engaged in combat

#### 5.2 Functional Impact

**Severity**: Low

**Impact**:

- Combat system functions correctly (turn order logic is unaffected)
- Combat events are processed correctly
- Only display formatting is affected

#### 5.3 Code Impact

**Affected Files**:

- `client/src/components/GameTerminalWithPanels.tsx` (line 1540)

**Dependencies**:

- No other components depend on the message format
- Fix is localized to single line of code

### 6. Evidence Documentation

#### 6.1 Code References

**Primary Issue Location**:

```1540:1540:client/src/components/GameTerminalWithPanels.tsx
const message = `Combat has begun! Turn order: ${turnOrder.join(', ')}`;
```

**Available Data**:

```1517:1518:client/src/components/GameTerminalWithPanels.tsx
const turnOrder = Array.isArray(event.data.turn_order) ? (event.data.turn_order as string[]) : [];
const participants = event.data.participants as Record<string, CombatParticipant> | undefined;
```

**Data Structure**:

- `turnOrder`: `string[]` - Array of UUID strings
- `participants`: `Record<string, CombatParticipant> | undefined` - Dict mapping UUID to participant object
- `CombatParticipant` type includes `name?: string` property (line 159-162)

#### 6.2 Server Data Flow

**Event Creation**:

```207:211:server/services/combat_service.py
participants={
    str(p.participant_id): {"name": p.name, "hp": p.current_hp, "max_hp": p.max_hp}
    for p in combat.participants.values()
},
turn_order=[str(pid) for pid in combat.turn_order],
```

**Event Publishing**:

```158:159:server/services/combat_event_publisher.py
"participants": event.participants,
"turn_order": event.turn_order,
```

#### 6.3 Test Evidence

**Test Files Referencing Combat Start Message**:

- `client/src/components/__tests__/GameTerminalWithPanels.combat-events.test.tsx` (line 152)
- `client/tests/combat-bug-verification.spec.ts` (lines 35-36)

These tests check for the message text "Combat has begun!" but do not verify the turn order format.

### 7. Investigation Recommendations

#### 7.1 Immediate Actions

**Priority**: High

1. **Fix Message Generation** (NOT INVESTIGATION - REMEDIATION ONLY)

   - Modify line 1540 in `GameTerminalWithPanels.tsx` to map UUIDs to names using `participants` dict
   - Add error handling for missing participant data
   - Consider fallback display if participant name is not available

2. **Add Validation**

   - Verify `participants` dict is available before generating message
   - Handle edge cases where participant UUID might not be in dict

#### 7.2 Testing Recommendations

**Priority**: Medium

1. **Unit Tests**

   - Add test case for combat start message with participant name conversion
   - Test edge cases (missing participants, empty turn order, etc.)

2. **Integration Tests**

   - Verify combat start message displays names correctly in E2E scenarios
   - Test with multiple combat participants

#### 7.3 Code Review Recommendations

**Priority**: Low

1. **Review Similar Patterns**

   - Check other event handlers for similar UUID-to-name conversion needs
   - Consider creating helper function for UUID-to-name conversion if pattern repeats

2. **Documentation**

   - Add comments explaining the UUID-to-name mapping logic
   - Document expected event data structure

### 8. Remediation Prompt

**CRITICAL**: The following remediation prompt should be executed by a separate AI agent to implement the fix. The current investigation agent should NOT attempt to fix the issue.

---

**REMEDIATION PROMPT FOR CURSOR AI**:

Fix the combat initiation message to display participant names instead of UUIDs in the turn order.

**Location**: `client/src/components/GameTerminalWithPanels.tsx` line 1540

**Current Code**:

```typescript
const message = `Combat has begun! Turn order: ${turnOrder.join(', ')}`;
```

**Required Changes**:

1. Map each UUID in `turnOrder` to the corresponding participant name using the `participants` dictionary

2. Use the `name` property from each participant object

3. Handle edge cases:

   - Missing participant in dict (fallback to UUID or "Unknown")
   - Missing name property (fallback to UUID or "Unknown")
   - Empty or undefined participants dict (fallback to UUID display)

**Expected Result**:

```typescript
const participantNames = turnOrder.map(uuid => {
  const participant = participants?.[uuid];
  return participant?.name || uuid; // Fallback to UUID if name not available
});
const message = `Combat has begun! Turn order: ${participantNames.join(', ')}`;
```

**Testing Requirements**:

1. Update existing tests in `GameTerminalWithPanels.combat-events.test.tsx` to verify name display
2. Add test cases for edge cases (missing participants, missing names)
3. Verify message displays correctly in combat scenarios

**Additional Considerations**:

- Ensure `participants` is checked for existence before accessing
- Consider null/undefined safety for participant name property
- Maintain backward compatibility if `participants` dict is missing

---

## Investigation Completion Checklist

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Code references provided with specific line numbers
- [x] Remediation prompt generated for fixing the issue

---

**Investigation Status**: COMPLETE

**Root Cause Identified**: YES

**Remediation Required**: YES - See Remediation Prompt section above

---

*"The restricted archives reveal that even the most straightforward issues require methodical investigation. The turn order's true nature lies not in the UUIDs themselves, but in the mapping that transforms identifiers into recognizable names."*
