# .validate target()

> 94 nodes

## Key Concepts

- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_queued_actions()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_clear_queued_actions()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_clear_queued_actions_specific_round()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_get_default_damage_from_config()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_get_default_damage_fallback_on_error()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_player_positive_dp()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_player_zero_dp()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_player_negative_dp_above_threshold()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_player_negative_dp_at_threshold()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_player_negative_dp_below_threshold()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_player_inactive()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_npc_positive_dp()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_npc_zero_dp()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_npc_negative_dp()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_alive_npc_inactive()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_dead_player_positive_dp()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_dead_player_at_zero()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_dead_player_at_negative_10()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_mortally_wounded_player_at_zero()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_is_mortally_wounded_player_npc_always_false()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_apply_damage_player_reduces_dp()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_apply_damage_player_mortally_wounded()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_apply_damage_player_dies()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_participant_apply_damage_player_caps_at_negative_10()** (3 connections) — `server/tests/unit/models/test_combat.py`
- *... and 69 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (54 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (4 shared connections)

## Source Files

- `server/tests/unit/models/test_combat.py`

## Audit Trail

- EXTRACTED: 244 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*