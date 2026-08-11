# Rest Command Flow

> 559 nodes

## Key Concepts

- **CombatInstance** (169 connections) — `server/models/combat.py`
- **CombatParticipant** (168 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **UUID** (20 connections)
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **_validate_taunt_context()** (13 connections) — `server/commands/combat_taunt.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- *... and 534 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (123 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (73 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (26 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (15 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (14 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (10 shared connections)
- [Health Check Models](Health_Check_Models.md) (8 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (6 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (5 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (4 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (2 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 2313 (98%)
- INFERRED: 49 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*