# PlayerCombatService

> 251 nodes

## Key Concepts

- **PlayerCombatService** (77 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **CombatBundle** (24 connections) — `server/container/bundles/combat.py`
- **asyncio** (22 connections)
- **player_death_service.py** (20 connections) — `server/services/player_death_service.py`
- **_NpcWithLife** (16 connections) — `server/commands/combat_handler.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **bundles/combat.py** (13 connections) — `server/container/bundles/combat.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **PlayerLifecycleServices** (8 connections) — `server/services/combat_service_types.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **.initialize()** (7 connections) — `server/container/bundles/combat.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- *... and 226 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (30 shared connections)
- [CombatService](CombatService.md) (19 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (19 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (14 shared connections)
- [combat_loader.py](combat_loader.py.md) (13 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (11 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [EventBus](EventBus.md) (10 shared connections)
- [combat_service.py](combat_service.py.md) (9 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/container/bundles/combat.py`
- `server/models/npc.py`
- `server/services/combat_service.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/player_combat_service.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/services/test_player_combat_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 561 (86%)
- INFERRED: 88 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*