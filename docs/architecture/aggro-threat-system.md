# Aggro and Threat System Design

**Version 1.1.0** · MythosMUD · 2026-08-28

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
This document specifies the aggro and threat management system for MythosMUD combat. It implements the decisions in [ADR-016](decisions/ADR-016-aggro-threat-management.md).

## 2. Scope and Assumptions

**[SPEC]**

- **Room-based combat:** Everyone in the same room is in the fight; no sub-room positioning.
- **Taunt is room-local:** Taunt only affects targets in the same room as the mob.
- **Future kiting:** Pull from one room away is done by attacking (or pull action) from an adjacent room; the NPC may move to the attacker's room. Taunt does not pull from range.

## 3. Threat Accumulators

**[SPEC]**

| Source  | Formula / behaviour                                                                                                                             |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Damage  | threat += damage_dealt \* damage_threat_multiplier (default 1.0; tanks may use > 1.0).                                                          |
| Healing | threat += heal_amount \* healing_threat_factor (e.g. 0.5) applied to the mob's hate list for the healer (and/or healing target as appropriate). |
| Utility | threat += `aggro_utility_threat` (default 5.0) per successful buff/debuff, x aggression x corruption scale; not skipped for passive_mob (#833). |
| Taunt   | A queued action that rolls d100 vs max(intimidate, fighting): top + margin (x2 on Hard/Extreme), nothing on failure, wiped on fumble. Valid only if taunter.room_id == mob.room_id (#833). |
| Protect | A queued action that rolls d100 vs fighting. On success the protector gains `aggro_protect_threat_share` (0.5) of the ally's threat on each mob, soaks the mob's hits aimed at the ally while cover lasts (each adds damage threat), and earns `aggro_guarding_threat_multiplier` (1.5) on damage threat (#991). |

All values are per-mob: one hate list per mob (or per combat instance).

## 4. Target Priority and Stability

**[SPEC]**

- **Stability (primary):** Current target keeps aggro unless some entity has threat >= current_target_threat \* (1 + stability_margin).
- **Default stability margin:** 0.10 (10%). A new target is chosen only when their threat is at least 10% above the current target's threat.
- **When no current target or tie:** Apply optional priority rules per NPC type (e.g. healer priority, caster priority, weakest HP%); in room-based combat "closest" is anyone in room; fallback to highest threat or deterministic tie-break.
- **Stealth (aggro shedding):** When a player enters stealth, that player is removed from the mob's hate list (or their threat is set to 0). The mob immediately re-evaluates target; no gradual decay while stealthed.

## 5. Data Structure: Hate List

**[SPEC]**

- **Recommendation:** Hash map (dict) keyed by entity id (player or NPC), value = threat (and optional metadata: last_damage_tick, is_healer_flag).
- **Why:** O(1) update by entity; only entities with nonzero threat are stored (sparse). Target resolution = one pass over the map to find max threat and apply stability rule.
- **Lifecycle:** Create when mob gains first aggro; optional decay or trim (e.g. drop entities with 0 threat after 30s, or cap top N) to bound size in large rooms.

## 6. UpdateAggro() (per combat tick, per mob)

**[NOTE]**
Pseudocode:

```
UpdateAggro(mob, room):
  hate_list = get_or_create_hate_list(mob)
  current_target = mob.current_target

  for each event in combat_tick_events (damage, heal, taunt, stealth, etc.):
    if event is stealth: remove entity from hate_list (or set threat to 0); then continue to target resolution
    apply threat delta to hate_list[entity] (add or set for taunt)
    ensure entity is in same room as mob for taunt; else ignore taunt

  candidate = entity with highest threat in hate_list
  if candidate is None:
    clear current_target; return

  if current_target is None:
    set_target(mob, candidate); emit_switch_message(room, candidate); return

  threshold = current_target.threat * (1 + stability_margin)
  if candidate != current_target and candidate.threat >= threshold (or taunt_override):
    set_target(mob, candidate)
    emit_switch_message(room, candidate)   // one short line to room

  optional: decay or trim hate_list (e.g. drop zero-threat entries after 30s)
```

## 7. Scaling (1 vs many in room)

**[SPEC]**

- Store only entities with nonzero threat (sparse hate list).
- Target resolution: find max threat, compare to current target with stability rule; no full sort of all room occupants.
- On target switch: broadcast one short message to the room (e.g. "The horror turns its gaze to Soandso.").

## 8. Test Scenarios

**[SPEC]**

| Scenario             | Expected behaviour                                                                                                                                        |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Healer overpull      | Tank has threat lead; healer does one big heal. Healer's threat crosses threshold (e.g. 110% of tank) -> mob switches to healer; one message; no flicker. |
| Tank swap            | Tank A taunts (room-local), gets top. Tank B taunts, gets top. Mob switches to B.                                                                         |
| 40 in room           | Only 5 ever deal damage/heal; hate list has 5 entries; target resolution O(5); one broadcast on switch.                                                   |
| Taunt from next room | Taunt has no effect; mob does not move. (Kiting uses attack/pull from adjacent room, not taunt.)                                                          |
| Support pull         | Tank holds the mob; a support caster applies debuffs (no damage) until their threat is 110% of the tank's -> mob switches to them (#833).                  |
| Taunt fumble         | The tank holding aggro fumbles: their hate entry is wiped, the next in line becomes the target, one line announces it (#833).                             |
| Join and assist      | A second player attacks (or assists) in the fight's room and joins it; a player already fighting another foe is refused (#833).                          |
| Tank covers healer   | A healer holds the mob; the tank protects them. The mob's hits land on the tank, whose threat grows 1.5x per hit until the mob turns on the tank (#991).  |

## 9. Feedback (low-latency, text-efficient)

**[SPEC]**

- On target switch: emit **one** short line to the room (e.g. "The horror turns its gaze to Soandso.").
- No per-player spam; no repeated "X is now the target" for every occupant. Optionally, the new target can receive a one-line personal notice (e.g. "The horror is now focusing on you.").

## 10. Decisions (locked)

**[SPEC]**
The following were decided and are fixed for implementation:

- **Default stability margin:** 0.10 (10%).
- **Stealth / aggro shedding:** Option A (wipe). Stealth removes the player from the mob's hate list (or sets threat to 0); no decay-over-time while stealthed.
- **Group combat (#833):** N players vs one NPC per combat; taunt is a graded, round-costing roll; utility threat is flat and spreads by target; `assist` is one-shot. Full rationale: ADR-016 section 8.
- **Protect (#991):** a queued Fighting roll; success redirects the mob's hits from the covered ally to the protector for this round and the next, shares threat, and applies the guarding multiplier. No fumble case. Full rationale: ADR-016 section 9.

## 11. References

**[SPEC]**

- ADR-016: Aggro and Threat Management System
- [Aggro and Threat Implementation Plan](../archive/aggro-threat-implementation-plan.md) – implementation summary and key files
- Context and comparison (Diku/ROM vs LPMud, modern MUDs, social aggro): see discussion that led to this design.

## 12. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-28 | Fix broken implementation-plan link, now in `docs/archive/` (#722) |
| 1.2.0 | 2026-10-06 | Utility threat, graded taunt, join/assist rows and decisions (#833) |
