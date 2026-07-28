# Combat Command Handler

> 409 nodes · cohesion 0.01

## Key Concepts

- **AsyncPersistenceLayer** (183 connections) — `server/async_persistence.py`
- **PlayerCombatService** (76 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_async_persistence_delegates.py** (35 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_flee_command.py** (28 connections) — `server/tests/unit/commands/test_flee_command.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **ContainerCreateParams** (20 connections) — `server/persistence/container_create_params.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **UUID** (15 connections)
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **FleeHandlerDeps** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- *... and 384 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (62 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (45 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (25 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (22 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (18 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (17 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (15 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (14 shared connections)
- [End-to-End Validation](End-to-End_Validation.md) (13 shared connections)
- [Death Delirium UI Modals](Death_Delirium_UI_Modals.md) (13 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (11 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (9 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/persistence/container_create_params.py`
- `server/realtime/connection_manager.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/services/test_player_combat_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 1525 (89%)
- INFERRED: 194 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*