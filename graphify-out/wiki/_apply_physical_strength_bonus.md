# _apply_physical_strength_bonus

> 8 nodes

## Key Concepts

- **_apply_physical_strength_bonus()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_strength_modifier_from_attacker_stats()** (4 connections) — `server/services/combat_turn_participant_actions.py`
- **test_apply_physical_strength_bonus_adds_for_physical_only()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_strength_modifier_from_attacker_stats_defaults()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Parse strength from attacker stats dict; default 50 when missing or invalid.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Add CoC-style strength bonus for physical attacks (same formula as NPC combat…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Strength modifier defaults to 50; digit strings coerce for bonus math.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Physical damage adds strength bonus above 50; other damage types do not.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Relationships

- [CombatInstance](CombatInstance.md) (4 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*