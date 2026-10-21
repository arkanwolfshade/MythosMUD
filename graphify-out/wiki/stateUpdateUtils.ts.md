# stateUpdateUtils.ts

> 47 nodes · cohesion 0.12

## Key Concepts

- **test_n_player_combat.py** (41 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **_combat()** (26 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **_p()** (26 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **combat_service_end.py** (16 connections) — `server/services/combat_service_end.py`
- **_service_for()** (12 connections) — `server/tests/unit/services/test_n_player_combat.py`
- **remove_participant()** (10 connections) — `server/services/combat_service_end.py`
- **_select_player_target()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **asyncio** (9 connections)
- **_xp_recipients()** (8 connections) — `server/services/combat_service_attack.py`
- **end_combat()** (8 connections) — `server/services/combat_service_end.py`
- **clear_aggro_for_combat()** (7 connections) — `server/services/aggro_threat.py`
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
- *... and 22 more nodes in this community*

## Relationships

- [test_player_combat_service.py](test_player_combat_service.py.md) (15 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (15 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (10 shared connections)
- [DatabaseManager](DatabaseManager.md) (5 shared connections)
- [Room](Room.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [useThemeContext.ts](useThemeContext.ts.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_n_player_combat.py`

## Audit Trail

- EXTRACTED: 176 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*