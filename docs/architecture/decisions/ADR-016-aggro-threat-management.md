# ADR-016: Aggro and Threat Management System

**Status:** Accepted
**Date:** 2026-02-26

## Context

MythosMUD combat needs predictable, group-friendly NPC targeting so that tanks can hold aggro, healers and DPS can contribute without constant target flicker, and players understand why a mob switched targets. Traditional Diku/ROM-style "round-robin" or random targeting does not support tank/healer roles or threat-based control. A threat (hate) system with stability thresholds and room-based scope was desired, with future support for kiting (pulling a mob from an adjacent room).

## Decision

Adopt a **room-based aggro and threat management system** with the following choices:

- **Combat space:** Strictly room-based. Everyone in the same room is "in the fight"; no sub-room positioning. Target selection and threat are evaluated per room.
- **Threat accumulators:** Damage, healing (e.g. 0.5x equivalent threat), utility (buffs/debuffs), and taunt. Stored per-mob in a sparse structure (e.g. hash map keyed by entity id).
- **Stability threshold:** A new target is chosen only when an entity has threat >= (current target threat) \* (1 + stability_margin), preventing flicker (exact margin TBD; see design doc).
- **Taunt:** Room-local only. Taunt is valid only when the taunter is in the same room as the mob. Taunt does not pull from an adjacent room.
- **Future kiting:** Pulling from one room away is done by attacking (or another pull action) from an adjacent room, which creates aggro and, when implemented, moves the NPC into the attacker's room. Taunt is not used for ranged pull.
- **Feedback:** One short, text-efficient room message when the mob switches targets (e.g. "The horror turns its gaze to Soandso.").
- **Integration with NPC static data:** At combat join, each NPC's `npc_type` and `behavior_config.aggression_level` (0-10) are carried on the combat participant. **passive_mob:** damage does not add threat (only taunt and healing add threat). **aggressive_mob** (and other types when in combat): damage, healing, and taunt add threat as normal. **aggression_level** scales the effective threat multiplier: 0 -> 0.5x, 10 -> 1.0x (formula: 0.5 + 0.05 * level). Missing values default to full threat. Other npc_types (e.g. shopkeeper) in combat are treated like aggressive_mob.

Detailed formulas, data structures, UpdateAggro() behaviour, and test scenarios are in the companion design doc.

## Alternatives Considered

1. **Coordinate or position-in-room** – Rejected for initial scope; room-based keeps implementation simple and matches "everyone in the room is in the fight."
2. **Taunt as ranged pull** – Rejected; taunt is room-local so that kiting is explicitly "attack (or pull) from next room," not taunt-from-afar.
3. **No stability threshold** – Rejected; immediate switch on any threat lead would cause target flicker and poor tank/healer experience.
4. **Full round-robin / random target** – Rejected; does not support tanking or threat-based control.

## Consequences

- **Positive:** Clear tank/healer/DPS roles; predictable aggro with minimal spam; design supports future kiting via attack-from-adjacent-room; sparse hate list scales to many players in room.
- **Negative:** Per-mob state (hate list, current target) must be maintained and tick-driven; stealth/aggro shedding behaviour must be defined (TBD in design doc).
- **Neutral:** Optional per-NPC target priority (healer/caster/weakest) can be added later without changing core model.

## Related ADRs

- ADR-001: Layered Architecture with Event-Driven Components (combat tick / events)
- (Future) Kiting / cross-room pull: to be detailed when that feature is implemented

## References

- [Aggro and Threat System Design](../aggro-threat-system.md) – Formulas, data structures, pseudocode, test scenarios
- [Aggro and Threat Implementation Plan](../aggro-threat-implementation-plan.md) – Implementation summary and key files
