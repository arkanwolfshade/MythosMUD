# Aggro and Threat System Design

This document specifies the aggro and threat management system for MythosMUD combat. It implements the decisions in [ADR-016](decisions/ADR-016-aggro-threat-management.md).

## 1. Scope and Assumptions

- **Room-based combat:** Everyone in the same room is in the fight; no sub-room positioning.
- **Taunt is room-local:** Taunt only affects targets in the same room as the mob.
- **Future kiting:** Pull from one room away is done by attacking (or pull action) from an adjacent room; the NPC may move to the attacker's room. Taunt does not pull from range.

## 2. Threat Accumulators

| Source  | Formula / behaviour                                                                                                                             |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Damage  | threat += damage_dealt \* damage_threat_multiplier (default 1.0; tanks may use > 1.0).                                                          |
| Healing | threat += heal_amount \* healing_threat_factor (e.g. 0.5) applied to the mob's hate list for the healer (and/or healing target as appropriate). |
| Utility | threat += flat or small per-application value for buffs/debuffs so support can pull if they over-apply.                                         |
| Taunt   | Set taunter's threat to current_top_threat + margin (or "become top for N seconds"). Valid only if taunter.room_id == mob.room_id.              |

All values are per-mob: one hate list per mob (or per combat instance).

## 3. Target Priority and Stability

- **Stability (primary):** Current target keeps aggro unless some entity has threat >= current_target_threat \* (1 + stability_margin).
- **Default stability margin:** 0.10 (10%). A new target is chosen only when their threat is at least 10% above the current target's threat.
- **When no current target or tie:** Apply optional priority rules per NPC type (e.g. healer priority, caster priority, weakest HP%); in room-based combat "closest" is anyone in room; fallback to highest threat or deterministic tie-break.
- **Stealth (aggro shedding):** When a player enters stealth, that player is removed from the mob's hate list (or their threat is set to 0). The mob immediately re-evaluates target; no gradual decay while stealthed.

## 4. Data Structure: Hate List

- **Recommendation:** Hash map (dict) keyed by entity id (player or NPC), value = threat (and optional metadata: last_damage_tick, is_healer_flag).
- **Why:** O(1) update by entity; only entities with nonzero threat are stored (sparse). Target resolution = one pass over the map to find max threat and apply stability rule.
- **Lifecycle:** Create when mob gains first aggro; optional decay or trim (e.g. drop entities with 0 threat after 30s, or cap top N) to bound size in large rooms.

## 5. UpdateAggro() (per combat tick, per mob)

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

## 6. Scaling (1 vs many in room)

- Store only entities with nonzero threat (sparse hate list).
- Target resolution: find max threat, compare to current target with stability rule; no full sort of all room occupants.
- On target switch: broadcast one short message to the room (e.g. "The horror turns its gaze to Soandso.").

## 7. Test Scenarios

| Scenario             | Expected behaviour                                                                                                                                        |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Healer overpull      | Tank has threat lead; healer does one big heal. Healer's threat crosses threshold (e.g. 110% of tank) -> mob switches to healer; one message; no flicker. |
| Tank swap            | Tank A taunts (room-local), gets top. Tank B taunts, gets top. Mob switches to B.                                                                         |
| 40 in room           | Only 5 ever deal damage/heal; hate list has 5 entries; target resolution O(5); one broadcast on switch.                                                   |
| Taunt from next room | Taunt has no effect; mob does not move. (Kiting uses attack/pull from adjacent room, not taunt.)                                                          |

## 8. Feedback (low-latency, text-efficient)

- On target switch: emit **one** short line to the room (e.g. "The horror turns its gaze to Soandso.").
- No per-player spam; no repeated "X is now the target" for every occupant. Optionally, the new target can receive a one-line personal notice (e.g. "The horror is now focusing on you.").

## 9. Decisions (locked)

The following were decided and are fixed for implementation:

- **Default stability margin:** 0.10 (10%).
- **Stealth / aggro shedding:** Option A (wipe). Stealth removes the player from the mob's hate list (or sets threat to 0); no decay-over-time while stealthed.

## 10. References

- ADR-016: Aggro and Threat Management System
- [Aggro and Threat Implementation Plan](aggro-threat-implementation-plan.md) – implementation summary and key files
- Context and comparison (Diku/ROM vs LPMud, modern MUDs, social aggro): see discussion that led to this design.
