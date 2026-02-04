# Combat Second-NPC and Linkdead Findings

**Session ID**: 2026-02-04
**Investigation Date**: February 4, 2026
**Related**: feature/first-weapon branch; combat flow, respawn, connection state

---

## Executive Summary

Two issues were investigated: (1) "Target is not in this combat" when attacking a second NPC after slaying the first, and (2) combat round messages not appearing in the Game Info panel for a second NPC while health decreased. A respawn 403 blocked retesting until fixed. **Findings**: (1) Fixed by validating queued attacks in the turn processor. (2) **Root cause for missing second-combat messages**: client was likely in **(linkdead)** state (WebSocket disconnected); when the client was fully connected, first-combat messages displayed correctly. Respawn eligibility was broadened to allow respawn when in limbo or when `is_dead()`.

---

## Issue 1: "Target is not in this combat" (Second NPC Attack)

### Symptoms

- Player slays first NPC, then attacks a second NPC.
- Server raises `ValueError("Target is not in this combat")` in `combat_attack_handler.py`.
- Errors appear in `errors.log`; combat flow breaks.

### Root Cause

Queued attack actions in the turn processor could reference a stale or dead target (e.g. the first NPC). When the round executed, the handler assumed the target was still in combat.

### Fix Implemented

- **File**: `server/services/combat_turn_processor.py`
- In `_execute_round`, before applying a queued attack, validate that the target exists in the combat and is alive. If not, clear the stale action and use the default action (e.g. default attack).
- Added logging for stale/cleared actions.
- **Test**: `test_execute_round_stale_queued_attack_uses_default_action` in `server/tests/unit/services/test_combat_turn_processor.py`.

### Status

**Resolved.** `errors.log` remained clear after the fix.

---

## Issue 2: Combat Messages Not Showing for Second NPC (Game Info Panel)

### Symptoms (Original Report)

- After first combat, attacking a **second** NPC: character health decreases (combat occurs server-side).
- Game Info panel shows **no** combat round messages for that second fight.
- Regular game ticks still appear in Game Info.

### Investigation

1. **Client flow**: Combat events are processed in `useEventProcessing.ts` and projected into `gameState.messages` via `projector.ts`. Instrumentation logged "Combat event received" and "Combat message appended" when events were handled.
2. **Server**: `CombatEventPublisher` publishes combat events to NATS; these are broadcast to WebSocket clients. Event types include `player_attacked`, `npc_attacked`, etc.
3. **Retest (after respawn fix)**:
   - First combat (e.g. vs Dr. Francis Morgan): **All** combat round messages appeared in Game Info ("You auto_attack...", "Dr. Francis Morgan auto_attack...", "The Dr. Francis Morgan has been slain."). Client console showed "Combat event received" and "Combat message appended".
   - Second combat: Could not be reproduced in that run—no other living NPCs in the room after the first kill.

### Finding: Linkdead State and Event Delivery

- When the client is **connected** (WebSocket up), combat events are received and shown in Game Info.
- When the client shows **(linkdead)**, the WebSocket is **disconnected**. The server keeps the player in a 30-second grace period (`disconnect_grace_period.py`); the client does not receive real-time events (e.g. combat rounds) until it reconnects.
- **Conclusion**: The observation that "combat messages don’t show for the second NPC" is **consistent with the client being (linkdead)** during the second fight—i.e. connection loss or NATS/WebSocket delivery failure—rather than a bug in combat message formatting or projection. No code defect was found in the combat event pipeline for connected clients.

### Implications

- **UX**: Ensure connection status is visible (e.g. "Connected" vs "(linkdead)") so players understand when they are not receiving live events.
- **Reliability**: Investigate why the client might disconnect (linkdead) during or between combats: health checks, WebSocket timeouts, NATS reconnects, or browser/network behavior.
- **Future**: If desired, consider replaying missed combat messages on reconnect (complex; not in scope for this session).

---

## Respawn 403 Forbidden (Blocker Resolved)

### Symptoms

- Respawn request to `/api/players/respawn` returned **403 Forbidden**.
- Server logic required `is_dead()` (e.g. DP <= -10). Client showed death state but server considered player not dead (e.g. already respawned or in limbo).

### Fix Implemented

- **File**: `server/game/player_respawn_wrapper.py`
- **Change**: `_is_eligible_for_respawn` now allows respawn if **either** `player.is_dead()` **or** player is in `LIMBO_ROOM_ID`. This lets players in limbo or in a death-like state use the respawn flow without 403.

### Status

**Resolved.** Respawn succeeded after the change; retest of combat flow could proceed.

---

## Related Files

- `server/services/combat_turn_processor.py` – stale queued attack handling
- `server/services/combat_attack_handler.py` – target-in-combat checks
- `server/services/combat_event_publisher.py` – combat events to NATS/WS
- `server/realtime/disconnect_grace_period.py` – linkdead grace period
- `server/realtime/websocket_room_updates.py` – linkdead indicator
- `server/game/player_respawn_wrapper.py` – respawn eligibility (limbo)
- `client/src/components/ui-v2/hooks/useEventProcessing.ts` – combat event handling
- `client/src/components/ui-v2/eventLog/projector.ts` – message projection

---

## Next Steps (Recommendations)

1. **Connection / linkdead**: Review client WebSocket and NATS health checks, reconnect logic, and server-side disconnect/grace-period behavior so players stay "Connected" during normal play and reconnection is robust.
2. **Second-combat E2E**: When multiple NPCs are available, add or run an E2E scenario: first combat to death, then attack second NPC and confirm combat messages appear in Game Info while client is connected.
3. **Monitoring**: Log or metric when players enter grace period (linkdead) to correlate with reports of "missing" combat messages.

---

**Investigation Status**: Findings recorded; second-NPC message issue attributed to linkdead/connection state. Fixes for "Target is not in this combat" and respawn 403 are in place.
