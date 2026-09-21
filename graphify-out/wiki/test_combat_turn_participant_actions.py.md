# test_combat_turn_participant_actions.py

> 19 nodes

## Key Concepts

- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_broadcasts_when_aggro_switches()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_uses_aggro_current_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_select_npc_target_prefers_mortally_wounded_player_over_skipping()** (4 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_apply_physical_strength_bonus_adds_for_physical_only()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_strength_modifier_from_attacker_stats_defaults()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **asyncio** (3 connections)
- **UUID** (2 connections)
- **MonkeyPatch** (1 connections)
- **Select target for NPC attack. Prefers participants that are not dead (includes…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Unit tests for combat_turn_participant_actions (aggro-aware NPC targeting and…** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Strength modifier defaults to 50; digit strings coerce for bonus math.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Physical damage adds strength bonus above 50; other damage types do not.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Happy path: living NPC resolves target and combat_service.process_attack runs.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **Player at 0 DP is not is_dead; NPC turn must still select them (ADR-016 / auto…** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **When get_npc_current_target resolves an id, that participant is returned if…** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **update_aggro may signal a switch; combat service broadcasts room narrative.** (1 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [CombatParticipant](CombatParticipant.md) (6 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*