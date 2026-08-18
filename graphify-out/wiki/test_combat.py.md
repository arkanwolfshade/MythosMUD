# test_combat.py

> 106 nodes

## Key Concepts

- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **test_combat_instance_clear_queued_actions()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_clear_queued_actions_specific_round()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_alive_participants()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_alive_participants_empty()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_current_turn_participant_with_valid_turn()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_participants_by_initiative()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_queued_actions()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_is_combat_over_when_active()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_advance_turn()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_advance_turn_always_increments_round()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_advance_turn_increments_round()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_default_values()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_current_turn_participant_missing_participant()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_current_turn_participant_no_turn_order()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_current_turn_participant_turn_out_of_range()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_is_combat_over_when_ended()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_is_combat_over_when_timeout()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_update_activity()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_apply_damage_npc_caps_at_zero()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_apply_damage_npc_dies_at_zero()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_apply_damage_npc_reduces_dp()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_apply_damage_player_caps_at_negative_10()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_apply_damage_player_dies()** (3 connections) — `server/tests/unit/models/test_combat.py`
- *... and 81 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (42 shared connections)
- [CombatInstance](CombatInstance.md) (19 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/tests/unit/models/test_combat.py`

## Audit Trail

- EXTRACTED: 169 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*