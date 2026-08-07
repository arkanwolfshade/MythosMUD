# Item Instances

> 159 nodes

## Key Concepts

- **CombatParticipant** (193 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (61 connections) — `server/services/combat_turn_processor.py`
- **combat.py** (56 connections) — `server/models/combat.py`
- **test_combat_turn_processor.py** (49 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (29 connections) — `server/models/combat.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
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
- **.is_dead()** (5 connections) — `server/models/combat.py`
- **.get_alive_participants()** (5 connections) — `server/models/combat.py`
- *... and 134 more nodes in this community*

## Relationships

- [command factories exploration](command_factories_exploration.md) (76 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (24 shared connections)
- [services service phantom](services_service_phantom.md) (22 shared connections)
- [subject admin controller](subject_admin_controller.md) (17 shared connections)
- [persistence container extended](persistence_container_extended.md) (16 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (13 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (13 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (12 shared connections)
- [commands position system](commands_position_system.md) (9 shared connections)
- [message nats handler](message_nats_handler.md) (9 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (8 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (6 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_turn_processor.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 856 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*