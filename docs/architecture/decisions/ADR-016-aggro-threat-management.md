# ADR-016: Aggro and Threat Management System

**Version 1.1.0** · MythosMUD · 2026-08-28

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-02-26
**Provenance:** Post-hoc — authored after the systems it describes. See [README §2](README.md).

## 2. Context

**[NOTE]**
MythosMUD combat needs predictable, group-friendly NPC targeting so that tanks can hold aggro, healers and DPS can contribute without constant target flicker, and players understand why a mob switched targets. Traditional Diku/ROM-style "round-robin" or random targeting does not support tank/healer roles or threat-based control. A threat (hate) system with stability thresholds and room-based scope was desired, with future support for kiting (pulling a mob from an adjacent room).

## 3. Decision

**[SPEC]**
Adopt a **room-based aggro and threat management system** with the following choices:

- **Combat space:** Strictly room-based. Everyone in the same room is "in the fight"; no sub-room positioning. Target selection and threat are evaluated per room.
- **Threat accumulators:** Damage, healing (e.g. 0.5x equivalent threat), utility (buffs/debuffs), and taunt. Stored per-mob in a sparse structure (e.g. hash map keyed by entity id).
- **Stability threshold:** A new target is chosen only when an entity has threat >= (current target threat) \* (1 + stability_margin), preventing flicker (exact margin TBD; see design doc).
- **Taunt:** Room-local only. Taunt is valid only when the taunter is in the same room as the mob. Taunt does not pull from an adjacent room.
- **Future kiting:** Pulling from one room away is done by attacking (or another pull action) from an adjacent room, which creates aggro and, when implemented, moves the NPC into the attacker's room. Taunt is not used for ranged pull.
- **Feedback:** One short, text-efficient room message when the mob switches targets (e.g. "The horror turns its gaze to Soandso.").
- **Integration with NPC static data:** At combat join, each NPC's `npc_type` and `behavior_config.aggression_level` (0-10) are carried on the combat participant. **passive_mob:** damage does not add threat (only taunt and healing add threat); passive mobs can still build threat against healers. **aggressive_mob** (and other types when in combat): damage, healing, and taunt add threat as normal. **aggression_level** scales the effective threat multiplier: 0 -> 0.5x, 10 -> 1.0x (formula: 0.5 + 0.05 \* level). Missing values default to full threat. Other npc_types (e.g. shopkeeper) in combat are treated like aggressive_mob. Sample aggressive mobs such as Cultist of the Yellow Sign, Deep One Hybrid, and Nightgaunt use explicit `aggression_level` values in their `behavior_config` so designers can tune their relative stickiness.

Detailed formulas, data structures, UpdateAggro() behaviour, and test scenarios are in the companion design doc.

## 4. Alternatives Considered

**[SPEC]**

1. **Coordinate or position-in-room** – Rejected for initial scope; room-based keeps implementation simple and matches "everyone in the room is in the fight."
2. **Taunt as ranged pull** – Rejected; taunt is room-local so that kiting is explicitly "attack (or pull) from next room," not taunt-from-afar.
3. **No stability threshold** – Rejected; immediate switch on any threat lead would cause target flicker and poor tank/healer experience.
4. **Full round-robin / random target** – Rejected; does not support tanking or threat-based control.

## 5. Consequences

**[SPEC]**

- **Positive:** Clear tank/healer/DPS roles; predictable aggro with minimal spam; design supports future kiting via attack-from-adjacent-room; sparse hate list scales to many players in room.
- **Negative:** Per-mob state (hate list, current target) must be maintained and tick-driven; stealth/aggro shedding behaviour must be defined (TBD in design doc).
- **Neutral:** Optional per-NPC target priority (healer/caster/weakest) can be added later without changing core model.

## 6. Related ADRs

**[SPEC]**

- ADR-001: Layered Architecture with Event-Driven Components (combat tick / events)
- (Future) Kiting / cross-room pull: to be detailed when that feature is implemented

## 7. References

**[SPEC]**

- [Aggro and Threat System Design](../aggro-threat-system.md) – Formulas, data structures, pseudocode, test scenarios
- [Aggro and Threat Implementation Plan](../../archive/aggro-threat-implementation-plan.md) – Implementation summary and key files

## 8. Addendum: Group combat and attention control (#833)

**[SPEC]**
This addendum records decisions made when the classic kit was completed and a Call of Cthulhu style attention layer was added. It refines, and does not replace, the decisions above.

- **Combat roster:** A combat is **N players against exactly one NPC**. A player who attacks an NPC already fighting in their room **joins** that combat; their first attack is queued for the next round. Joining a phantom (ADR-024 hallucination) encounter, another room's fight, or a second NPC is refused. Multi-NPC packs are deferred (#994).
- **Leaving and ending:** One player leaves with `remove_participant` (queued actions, hate-list entries, target links and tracking go with them) and the fight continues for the rest. The combat ends when no living NPC/phantom **or** no living player remains (mortally wounded players at 0 DP still count). A 1v1 behaves as before.
- **Player targets:** `CombatInstance.player_current_target` mirrors `npc_current_target`. Auto-attack uses it and never targets an ally. XP on an NPC's death is paid in full to every living player still in the fight.
- **Taunt is a roll and costs the round:** `taunt <npc>` queues a combat action (it replaces anything queued for that round, so there is no auto-attack). It resolves on the player's initiative slot as one d100 against the **higher of `intimidate` and `fighting`**: Hard or Extreme makes the taunter top with a doubled lead, Regular is the plain taunt, Failure changes nothing, and a Fumble (100, or 96-100 under skill 50) wipes the taunter from that NPC's hate list. Each result gets one room line. Taunt stays room-local and the taunter's room and the target are re-checked at resolution.
- **Utility threat:** A successful status-effect or stat-modify spell adds a flat `aggro_utility_threat` (default 5.0), scaled by the NPC's aggression level and the corruption gap like heal threat. It is **not** skipped for passive mobs. A debuff on an NPC draws only that NPC; a buff on the caster or an ally draws every NPC in the fight. Area and phantom targets add nothing.
- **Assist:** `assist <player>` (or a bare `assist` for the party leader) is **one-shot target resolution**: it finds the foe that player is fighting and goes through the ordinary attack path, which performs the join. The assister then fights on their own and does not follow later target switches.
- **Deferred (own issues):** Protect / draw-fire and the tank threat multiplier (#991), Fight Back threat (#992), NPC target bias and fixation (#993), packs (#994), adjacent-room pull (#995), threat inspection and the personal switch notice (#996), hate-list trim and flee interaction (#997), persistent auto-assist (#998).

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-28 | Record provenance (post-hoc authorship); fix broken implementation-plan link, now in `docs/archive/` (#721) |
| 1.2.0 | 2026-10-06 | Addendum: N-player combat, graded taunt, utility threat, assist (#833) |
