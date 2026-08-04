# command factories exploration

> 178 nodes

## Key Concepts

- **CombatInstance** (186 connections) — `server/models/combat.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **test_combat_flee_handler.py** (33 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (20 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_npc_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **.is_dead()** (5 connections) — `server/models/combat.py`
- **.get_alive_participants()** (5 connections) — `server/models/combat.py`
- **_get_target_stats_for_damage()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- *... and 153 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (73 shared connections)
- [models npc rationale](models_npc_rationale.md) (33 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (33 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (25 shared connections)
- [services combat sync](services_combat_sync.md) (10 shared connections)
- [nats services service](nats_services_service.md) (9 shared connections)
- [combat flee commands](combat_flee_commands.md) (8 shared connections)
- [combat commands handler](combat_commands_handler.md) (8 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (6 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (4 shared connections)
- [container helpers loot](container_helpers_loot.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 789 (96%)
- INFERRED: 31 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*