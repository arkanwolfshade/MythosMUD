# Logging Correct Patterns

> 82 nodes

## Key Concepts

- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_validate_taunt_context()** (13 connections) — `server/commands/combat_taunt.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **__init__.py** (12 connections) — `server/schemas/shared/__init__.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **_validate_taunt_target()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_success()** (7 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **Any** (6 connections)
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **UUID** (6 connections)
- **_validate_taunt_target_name()** (6 connections) — `server/commands/combat_taunt.py`
- **.handle_npc_attack_on_player()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **_RoomWithIdOnly** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **test_validate_taunt_target_not_npc()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_dead()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_no_combat_service()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- *... and 57 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (23 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (17 shared connections)
- [Client Event Store](Client_Event_Store.md) (12 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (9 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (7 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (7 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (5 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (4 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (4 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (3 shared connections)
- [Config Cors](Config_Cors.md) (3 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (3 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 340 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*