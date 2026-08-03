# Item Instances

> 196 nodes

## Key Concepts

- **CombatParticipant** (193 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (61 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (49 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (29 connections) — `server/models/combat.py`
- **._execute_spell_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (8 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **_unarmed_fallback_player_target_pair()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **.process_game_tick()** (5 connections) — `server/services/combat_turn_processor.py`
- **Any** (5 connections)
- **._apply_spell_effects()** (5 connections) — `server/services/combat_turn_processor.py`
- **._handle_flee_skip_action()** (5 connections) — `server/services/combat_turn_processor.py`
- **._process_npc_turn()** (5 connections) — `server/services/combat_turn_processor.py`
- **._process_player_turn()** (5 connections) — `server/services/combat_turn_processor.py`
- **test_combat_instance_queue_action()** (5 connections) — `server/tests/unit/models/test_combat.py`
- *... and 171 more nodes in this community*

## Relationships

- [combat commands handler](combat_commands_handler.md) (50 shared connections)
- [command factories exploration](command_factories_exploration.md) (46 shared connections)
- [NPC Combat](NPC_Combat.md) (19 shared connections)
- [services combat sync](services_combat_sync.md) (12 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (10 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (8 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (8 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [movement monitor game](movement_monitor_game.md) (5 shared connections)
- [spell game magic](spell_game_magic.md) (4 shared connections)
- [admin shutdown commands](admin_shutdown_commands.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_turn_processor.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 810 (99%)
- INFERRED: 9 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*