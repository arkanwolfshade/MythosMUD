# NPCCombatIntegrationService

> 185 nodes

## Key Concepts

- **NPCCombatIntegrationService** (86 connections) — `server/services/npc_combat_integration_service.py`
- **PlayerCombatService** (77 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **player_combat_service.py** (32 connections) — `server/services/player_combat_service.py`
- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **UUID** (15 connections)
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **CombatCommandHandlerExtras** (9 connections) — `server/commands/combat_handler.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **NPCCombatIntegrationReadApi** (7 connections) — `server/services/player_combat_service_support.py`
- **.validate_combat_command()** (7 connections) — `server/validators/combat_validator.py`
- **combat_validator.py** (7 connections) — `server/validators/combat_validator.py`
- **EventBusPublish** (6 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (6 connections) — `server/services/player_combat_service_support.py`
- **._get_persistence_from_app()** (6 connections) — `server/commands/combat_handler.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **handler()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (5 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (5 connections) — `server/services/player_combat_service_support.py`
- *... and 160 more nodes in this community*

## Relationships

- [test_npc_combat_integration_service.py](test_npc_combat_integration_service.py.md) (35 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (32 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (18 shared connections)
- [CombatService](CombatService.md) (16 shared connections)
- [combat_loader.py](combat_loader.py.md) (13 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [PlayerService](PlayerService.md) (11 shared connections)
- [NPCDefinition](NPCDefinition.md) (9 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (8 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/services/combat_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 426 (80%)
- INFERRED: 105 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*