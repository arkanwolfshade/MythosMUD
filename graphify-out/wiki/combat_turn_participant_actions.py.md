# combat_turn_participant_actions.py

> 71 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_npc_attack_damage()** (14 connections) — `server/game/npcs/attack_damage.py`
- **attack_damage.py** (12 connections) — `server/game/npcs/attack_damage.py`
- **test_attack_damage.py** (12 connections) — `server/tests/unit/game/npcs/test_attack_damage.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_combat_container_services()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_npc_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **armor_points_from_base_stats()** (6 connections) — `server/game/npcs/attack_damage.py`
- **_damage_from_attack()** (6 connections) — `server/game/npcs/attack_damage.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_apply_physical_strength_bonus()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_target_stats_for_damage()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_player_target()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_npc_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_player_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_skip_for_casting()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **test_resolve_npc_target_broadcasts_when_aggro_switches()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_uses_aggro_current_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_strength_modifier_from_attacker_stats()** (4 connections) — `server/services/combat_turn_participant_actions.py`
- *... and 46 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (21 shared connections)
- [CombatParticipant](CombatParticipant.md) (20 shared connections)
- [CombatInstance](CombatInstance.md) (8 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (7 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (5 shared connections)
- [NATSError](NATSError.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (3 shared connections)
- [damage_expr_to_min_max](damage_expr_to_min_max.md) (3 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [AppConfig](AppConfig.md) (3 shared connections)

## Source Files

- `server/game/npcs/attack_damage.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/game/npcs/test_attack_damage.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 179 (91%)
- INFERRED: 17 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*