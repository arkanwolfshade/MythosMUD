# Rest Command Flow

> 227 nodes

## Key Concepts

- **CombatParticipant** (168 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **combat.py** (50 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **CombatStatus** (11 connections) — `server/models/combat.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
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
- *... and 202 more nodes in this community*

## Relationships

- [Container Component Capacity](Container_Component_Capacity.md) (68 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (38 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (24 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (17 shared connections)
- [Health Check Models](Health_Check_Models.md) (15 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (13 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (11 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (9 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (4 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 939 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*