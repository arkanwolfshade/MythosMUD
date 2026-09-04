# MUD Disconnect Grace Period & Rest Command: Industry Comparison

## Executive Summary

After researching common MUD practices, our plan aligns well with industry standards but has several gaps and differences worth discussing. This document highlights areas where we may want to adjust our implementation.

---

## 1. Disconnect Grace Period Duration

### Industry Practices

**Lineage II**: 15 seconds of auto-attack (no skills)

**Ragnarök MUD**: 30 minutes before moving to storage room

**Various MUDs**: 30 seconds (common standard)
- **Some MUDs**: No grace period, immediate removal

### Our Plan

**30 seconds** grace period

### Gap Analysis

✅ **Our duration is standard** - 30 seconds is a common choice and aligns with many MUD implementations.

**Consideration**: Some MUDs use longer periods (30 minutes) but those are typically for idle/idle-disconnect handling, not immediate disconnection. Our 30-second window is appropriate for connection loss scenarios.

---

## 2. Auto-Attack During Grace Period

### Industry Practices

**Lineage II**: Auto-attack continues for 15 seconds, but **no special skills/abilities**

**Many MUDs**: Character becomes completely inactive (no auto-attack)

**Some MUDs**: Character continues full combat behavior
- **CircleMUD**: Linkdead players remain vulnerable but inactive

### Our Plan

**Normal auto-attack** (same as connected player)

- Only basic attacks, no special abilities

### Gap Analysis

⚠️ **Potential Gap**: We should clarify if auto-attack includes:

- Basic unarmed attacks only? ✅ (Our plan)
- Weapon-based attacks? ❓ (Not specified)
- Combat skills/abilities? ❌ (Should be excluded)

**Recommendation**: Explicitly limit grace period auto-attack to basic unarmed attacks only, matching Lineage II's approach. This prevents disconnected players from using powerful abilities.

---

## 3. Grace Period Visibility & Messaging

### Industry Practices

**Many MUDs**: Display "linkdead" or "disconnected" status to other players

**Some MUDs**: Character appears normal but doesn't respond

**Ragnarök**: Character may be moved to storage room after extended period

### Our Plan

Character remains visible and in room

- No explicit mention of "zombie" or "linkdead" status to other players

### Gap Analysis

❓ **Gap**: Should other players see that the character is disconnected?

**Options to Consider**:

1. **Visual indicator**: Show "(linkdead)" or "(disconnected)" in room descriptions
2. **No indicator**: Keep current plan (character appears normal)
3. **Status command**: `/who` or `/look` shows disconnect status

**Recommendation**: Add a subtle indicator (e.g., character appears "dazed" or "unresponsive") so other players understand why the character isn't responding to chat/commands.

---

## 4. Rest/Quit Command During Combat

### Industry Practices

**Many MUDs**: **Cannot quit during combat** (blocked entirely)

**Aardwolf**: Cannot quit while affected by certain combat conditions

**Some MUDs**: Quit allowed but with penalties (drop items, lose XP)
- **7 Degrees of Freedom**: Quit drops all equipment and money

### Our Plan

`/rest` command **allowed during combat** but requires 10-second countdown

- Can be interrupted by combat actions

### Gap Analysis

⚠️ **Significant Difference**: Most MUDs **completely block** quit/rest during combat.

**Our approach is more permissive**. We should decide:

1. **Block `/rest` entirely during combat** (more traditional)
2. **Allow `/rest` but with longer countdown** (e.g., 30 seconds instead of 10)
3. **Keep current plan** (10-second countdown, interruptible)

**Recommendation**: Consider blocking `/rest` entirely during combat, or at least requiring combat to end first. This prevents combat evasion while still allowing safe logout.

---

## 5. Rest Command Countdown Duration

### Industry Practices

**Minecraft HCF**: 30-second logout countdown

**Various MUDs**: 10-30 seconds

**Some MUDs**: Immediate logout in safe zones, countdown elsewhere

### Our Plan

**10 seconds** countdown for `/rest`

### Gap Analysis

✅ **Our duration is reasonable** - 10 seconds is on the shorter end but acceptable.

**Consideration**: Some MUDs use longer countdowns (30 seconds) to give more time for interruption. Our 10-second window is faster but may feel rushed.

---

## 6. Rest Location (Inn/Hotel) Behavior

### Industry Practices

**Many MUDs**: Safe zones allow immediate logout

**Some MUDs**: Rest locations provide faster HP/MP regeneration

**Abandoned Realms**: Sleeping in safe locations is safer than elsewhere

### Our Plan

**Instant disconnect** in rest locations when not in combat

**10-second countdown** if in combat (even in rest location)

### Gap Analysis

✅ **Our approach aligns well** with common practices.

**Potential Enhancement**: Some MUDs also provide HP/MP regeneration bonuses in rest locations. We're replacing the MP regeneration `/rest` command, so we might want to consider:

- Automatic slow regeneration while in rest locations?
- Or keep rest locations purely for safe logout?

---

## 7. Reconnection During Grace Period

### Industry Practices

**Most MUDs**: Reconnection cancels any disconnect handling

**Some MUDs**: Reconnection restores full control immediately

**Rare**: Reconnection doesn't cancel (player must wait out timer)

### Our Plan

**Reconnection cancels grace period immediately**

### Gap Analysis

✅ **Our approach is standard** - matches common practice.

---

## 8. Grace Period After Intentional Disconnect

### Industry Practices

**Most MUDs**: Grace period only applies to **unintentional** disconnects (connection loss)

**Some MUDs**: Grace period applies to all disconnects

**Distinction**: `/quit` vs. connection loss handled differently

### Our Plan

Grace period applies to **all disconnects** (intentional and unintentional)

### Gap Analysis

⚠️ **Potential Gap**: Should we distinguish between:

1. **Intentional disconnect** (player uses `/quit` or `/rest`) → No grace period?
2. **Unintentional disconnect** (connection loss) → 30-second grace period?

**Current Plan**: Grace period applies to all disconnects.

**Recommendation**: Consider **skipping grace period** for intentional disconnects (via `/rest` or `/quit`), as the player has already chosen to leave. Only apply grace period to unexpected connection losses.

---

## 9. Command Blocking During Grace Period

### Industry Practices

**Most MUDs**: Linkdead players cannot execute any commands

**Some MUDs**: Linkdead players can only auto-attack (no other actions)

**Rare**: Linkdead players retain full command access

### Our Plan

**Zombie state**: Cannot move, use commands, or take other actions

**Only auto-attacks** when attacked

### Gap Analysis

✅ **Our approach is standard** - matches common practice.

---

## 10. Grace Period Persistence

### Industry Practices

**Most MUDs**: Grace period is in-memory only (no persistence)

**Some MUDs**: Server restart loses grace period state

**Rare**: Grace period persists across server restarts

### Our Plan

**In-memory only** (no persistence)

### Gap Analysis

✅ **Our approach is standard** - matches common practice.

---

## 11. Missing Features from Other MUDs

### Features We're NOT Implementing (but exist elsewhere)

1. **Extended Idle Handling**:

   - Some MUDs move linkdead players to storage rooms after 30+ minutes
   - We only handle immediate disconnects (30 seconds)

2. **Combat Penalties for Disconnect**:

   - Some MUDs drop items or lose XP on disconnect during combat
   - We only apply grace period (no penalties)

3. **Visual Status Indicators**:

   - Some MUDs show "(linkdead)" in room descriptions
   - We don't plan to show disconnect status to other players

4. **Rest Location Regeneration**:

   - Some MUDs provide HP/MP regeneration in rest locations
   - We're removing MP regeneration from `/rest` command

---

## Recommendations Summary

### High Priority Decisions

1. **Auto-Attack Limitation**: Explicitly limit grace period auto-attack to basic unarmed attacks only (no weapons, no skills)

2. **Rest During Combat**: Consider blocking `/rest` entirely during combat, or requiring combat to end first

3. **Grace Period for Intentional Disconnects**: Consider skipping grace period for intentional disconnects (`/rest`, `/quit`), only applying it to connection losses

4. **Visual Indicator**: Consider adding subtle visual indicator (e.g., "dazed" or "unresponsive") so other players know the character is disconnected

### Medium Priority Enhancements

1. **Rest Location Regeneration**: Consider if rest locations should provide automatic slow HP/MP regeneration (separate from `/rest` command)

2. **Countdown Duration**: Consider if 10 seconds is sufficient or if 15-30 seconds would be better

### Low Priority (Future Considerations)

1. **Extended Idle Handling**: Consider 30+ minute idle-disconnect handling (separate from immediate disconnect grace period)

2. **Combat Disconnect Penalties**: Consider if disconnecting during combat should have penalties (beyond grace period vulnerability)

---

## Questions for Discussion

1. Should grace period auto-attack be limited to basic unarmed attacks only?
2. Should `/rest` be blocked entirely during combat?
3. Should grace period only apply to unintentional disconnects (connection loss), not intentional ones?
4. Should other players see a visual indicator that a character is disconnected?
5. Should rest locations provide automatic HP/MP regeneration in addition to safe logout?
