# _weapon_damage_from_equipped_player

> 13 nodes

## Key Concepts

- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_apply_physical_strength_bonus()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_strength_modifier_from_attacker_stats()** (4 connections) — `server/services/combat_turn_participant_actions.py`
- **_attacker_stats_dict_from_full_player()** (3 connections) — `server/services/combat_turn_participant_actions.py`
- **test_apply_physical_strength_bonus_adds_for_physical_only()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_strength_modifier_from_attacker_stats_defaults()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **PrototypeRegistry** (2 connections)
- **Parse strength from attacker stats dict; default 50 when missing or invalid.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Add CoC-style strength bonus for physical attacks (same formula as NPC combat…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Normalize full_player.get_stats() to a dict for damage math.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Resolve rolled damage and type from main-hand weapon, or unarmed fallback.** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Strength modifier defaults to 50; digit strings coerce for bonus math.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Physical damage adds strength bonus above 50; other damage types do not.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (10 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 23 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*