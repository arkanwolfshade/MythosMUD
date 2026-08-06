# Item Instances

> 218 nodes

## Key Concepts

- **CombatParticipant** (193 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (61 connections) — `server/services/combat_turn_processor.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_turn_processor.py** (49 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (29 connections) — `server/models/combat.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **._execute_spell_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (8 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
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
- *... and 193 more nodes in this community*

## Relationships

- [command factories exploration](command_factories_exploration.md) (55 shared connections)
- [models npc rationale](models_npc_rationale.md) (30 shared connections)
- [EdgeCreationModal map STANDARD](EdgeCreationModal_map_STANDARD.md) (19 shared connections)
- [subject admin controller](subject_admin_controller.md) (17 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (17 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (10 shared connections)
- [tick game processing](tick_game_processing.md) (9 shared connections)
- [room renderer functions](room_renderer_functions.md) (7 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (6 shared connections)
- [tools generate invite](tools_generate_invite.md) (3 shared connections)
- [player look commands](player_look_commands.md) (3 shared connections)
- [combat flee commands](combat_flee_commands.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 935 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*