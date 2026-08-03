# NPC Combat

> 564 nodes

## Key Concepts

- **AsyncPersistenceLayer** (184 connections) — `server/async_persistence.py`
- **CombatService** (181 connections) — `server/services/combat_service.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **TargetResolutionResult** (42 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (40 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **TargetType** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **movement_service.py** (28 connections) — `server/game/movement_service.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **player_respawn.py** (25 connections) — `server/api/player_respawn.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (22 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 539 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (67 shared connections)
- [spell game magic](spell_game_magic.md) (66 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (50 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (49 shared connections)
- [target resolution service](target_resolution_service.md) (27 shared connections)
- [schemas invite user](schemas_invite_user.md) (24 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (23 shared connections)
- [command factories exploration](command_factories_exploration.md) (23 shared connections)
- [Item Instances](Item_Instances.md) (19 shared connections)
- [combat commands handler](combat_commands_handler.md) (17 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (17 shared connections)
- [Error Conversion](Error_Conversion.md) (16 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/container/bundles/combat.py`
- `server/game/magic/spell_targeting.py`
- `server/game/movement_service.py`
- `server/game/profession_service.py`
- `server/realtime/connection_manager.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 2418 (90%)
- INFERRED: 278 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*