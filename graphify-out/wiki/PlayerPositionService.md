# PlayerPositionService

> 110 nodes · cohesion 0.04

## Key Concepts

- **combat_handler.py** (54 connections) — `server/commands/combat_handler.py`
- **combat_assist.py** (38 connections) — `server/commands/combat_assist.py`
- **test_combat_protect.py** (38 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **target_resolution_service.py** (29 connections) — `server/services/target_resolution_service.py`
- **_protect()** (27 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **AssistCommandHandler** (26 connections) — `server/commands/combat_assist.py`
- **combat_protect.py** (22 connections) — `server/commands/combat_protect.py`
- **AppWithState** (21 connections) — `server/commands/combat_app_protocols.py`
- **asyncio** (18 connections)
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **run_handle_protect_command()** (15 connections) — `server/commands/combat_protect.py`
- **TargetMetadata** (15 connections) — `server/schemas/shared/target_metadata.py`
- **_match()** (15 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **run_handle_assist_command()** (14 connections) — `server/commands/combat_assist.py`
- **_fight()** (13 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **load_assister()** (11 connections) — `server/commands/combat_assist.py`
- **find_ally_fight()** (10 connections) — `server/commands/combat_assist.py`
- **combat_app_protocols.py** (8 connections) — `server/commands/combat_app_protocols.py`
- **UUID** (8 connections)
- **_resolve_assisted()** (8 connections) — `server/commands/combat_assist.py`
- **_join_if_needed()** (8 connections) — `server/commands/combat_protect.py`
- **_find_assisted_foe()** (7 connections) — `server/commands/combat_assist.py`
- **resolve_named_player()** (7 connections) — `server/commands/combat_assist.py`
- **assisted_name_from_command()** (6 connections) — `server/commands/combat_assist.py`
- **_foe_of()** (6 connections) — `server/commands/combat_assist.py`
- *... and 85 more nodes in this community*

## Relationships

- [InventorySchemaValidationError](InventorySchemaValidationError.md) (36 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (15 shared connections)
- [command_parser.py](command_parser.py.md) (15 shared connections)
- [RoomService](RoomService.md) (12 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (11 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (10 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (9 shared connections)
- [DatabaseManager](DatabaseManager.md) (9 shared connections)
- [npcs/catalog_dml.py](npcs-catalog_dml.py.md) (6 shared connections)
- [TestNPCCombatLifecycle](TestNPCCombatLifecycle.md) (6 shared connections)
- [Room](Room.md) (6 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (5 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_assist.py`
- `server/commands/combat_attack.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_protect.py`
- `server/schemas/shared/target_metadata.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_protect.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 382 (91%)
- INFERRED: 36 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*