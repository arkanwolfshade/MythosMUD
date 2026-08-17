# server models combat combataction

> 213 nodes

## Key Concepts

- **CombatParticipant** (184 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (61 connections) — `server/services/combat_turn_processor.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_turn_processor.py** (50 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (27 connections) — `server/models/combat.py`
- **asyncio** (27 connections)
- **._execute_spell_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (7 connections) — `server/services/combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (7 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_participant_action_valid_queued_attack()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_attack_action()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_spell_without_magic_service()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_app()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **_unarmed_fallback_player_target_pair()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._apply_spell_effects()** (5 connections) — `server/services/combat_turn_processor.py`
- *... and 188 more nodes in this community*

## Relationships

- [server models combat combatinstance](server_models_combat_combatinstance.md) (50 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (37 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (26 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (16 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (7 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (6 shared connections)
- [server services combat event handler](server_services_combat_event_handler.md) (6 shared connections)
- [server models combat combatresult](server_models_combat_combatresult.md) (3 shared connections)
- [server services combat initialization](server_services_combat_initialization.md) (2 shared connections)
- [server commands combat flee](server_commands_combat_flee.md) (2 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (2 shared connections)
- [server game magic spell registry](server_game_magic_spell_registry.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 527 (94%)
- INFERRED: 36 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*