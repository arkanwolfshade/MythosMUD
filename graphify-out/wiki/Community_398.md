# Community 398

> 44 nodes

## Key Concepts

- **test_n_player_combat.py** (41 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **_combat()** (26 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **_p()** (26 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **join_existing_combat()** (14 connections) — `server/services/combat_service_start.py`
- **_service_for()** (12 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **remove_participant()** (10 connections) — `server/services/combat_service_end.py`
- **_select_player_target()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **asyncio** (9 connections)
- **_xp_recipients()** (8 connections) — `server/services/combat_service_attack.py`
- **remove_entity_from_aggro()** (7 connections) — `server/services/aggro_threat.py`
- **test_join_existing_combat_adds_player_and_rebuilds_initiative()** (7 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_join_existing_combat_refuses_a_player_already_fighting_elsewhere()** (7 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_join_existing_combat_refuses_another_room()** (7 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_join_existing_combat_refuses_phantom_encounters()** (7 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_remove_participant_ends_combat_when_no_other_player_remains()** (7 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **_data()** (6 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_queue_attack_records_player_target_but_not_npc_target()** (6 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_remove_participant_does_not_count_a_dead_player_as_remaining()** (6 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_remove_participant_drops_only_the_leaver_when_others_remain()** (6 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_remove_participant_ignores_unknown_participant_and_combat()** (6 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_auto_attack_never_picks_an_ally()** (4 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_auto_attack_player_versus_player_keeps_legacy_pick()** (4 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_auto_attack_prefers_the_tracked_target_and_skips_a_dead_one()** (4 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_clear_aggro_for_combat_also_clears_player_targets()** (4 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **test_combat_ends_when_npc_dies_even_with_two_players_left()** (4 connections) — `server/tests/unit/services/test_n_player_combat.py`
- *... and 19 more nodes in this community*

## Relationships

- [Combat Attack Execution](Combat_Attack_Execution.md) (27 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (7 shared connections)
- [Combat Participants](Combat_Participants.md) (5 shared connections)
- [Community 52](Community_52.md) (3 shared connections)
- [Community 226](Community_226.md) (1 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (1 shared connections)
- [Community 758](Community_758.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_n_player_combat.py`

## Audit Trail

- EXTRACTED: 163 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*