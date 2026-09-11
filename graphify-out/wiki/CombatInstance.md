# CombatInstance

> 171 nodes

## Key Concepts

- **CombatInstance** (190 connections) — `server/models/combat.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **test_combat_flee_handler.py** (33 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (24 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (20 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (15 connections)
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **._create_corpse_on_death()** (10 connections) — `server/services/combat_death_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **.handle_target_state_changes()** (6 connections) — `server/services/combat_death_handler.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **_execute_npc_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **test_execute_voluntary_flee_free_hits_error_logged()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_missing_participant_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_move_fails_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 146 more nodes in this community*

## Relationships

- [combat_service.py](combat_service.py.md) (68 shared connections)
- [CombatParticipant](CombatParticipant.md) (52 shared connections)
- [CombatService](CombatService.md) (34 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (20 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (18 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (7 shared connections)
- [_weapon_damage_from_equipped_player](_weapon_damage_from_equipped_player.md) (7 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (5 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (4 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 541 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*