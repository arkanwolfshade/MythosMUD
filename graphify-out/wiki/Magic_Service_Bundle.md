# Magic Service Bundle

> 279 nodes

## Key Concepts

- **TargetMatch** (121 connections) — `server/schemas/shared/target_resolution.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (12 connections) — `server/schemas/shared/target_metadata.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_as_app_with_state()** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- *... and 254 more nodes in this community*

## Relationships

- [Player Respawn Service](Player_Respawn_Service.md) (38 shared connections)
- [Game Client Container](Game_Client_Container.md) (21 shared connections)
- [Container Open Events](Container_Open_Events.md) (21 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (15 shared connections)
- [Player Event Handler Tests](Player_Event_Handler_Tests.md) (14 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (14 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (11 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (9 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (9 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (7 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (7 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (7 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 1088 (90%)
- INFERRED: 127 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*