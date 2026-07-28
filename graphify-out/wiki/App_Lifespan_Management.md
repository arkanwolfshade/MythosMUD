# App Lifespan Management

> 484 nodes · cohesion 0.01

## Key Concepts

- **CombatInstance** (167 connections) — `server/models/combat.py`
- **CombatParticipant** (166 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **CombatStatus** (11 connections) — `server/models/combat.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **combat_service_end.py** (11 connections) — `server/services/combat_service_end.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- *... and 459 more nodes in this community*

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (185 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (14 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (14 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (13 shared connections)
- [Cursor Plans Uvicorn](Cursor_Plans_Uvicorn.md) (11 shared connections)
- [Phantom Hostile Requirements](Phantom_Hostile_Requirements.md) (11 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (10 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (7 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (6 shared connections)
- [Test Value Distribution](Test_Value_Distribution.md) (5 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (5 shared connections)
- [Player Death Service Tests](Player_Death_Service_Tests.md) (3 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 1837 (97%)
- INFERRED: 58 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*