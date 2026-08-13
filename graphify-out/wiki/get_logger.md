# get_logger

> 1078 nodes

## Key Concepts

- **get_logger()** (509 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (484 connections) — `server/structured_logging/enhanced_logging_config.py`
- **CombatService** (181 connections) — `server/services/combat_service.py`
- **CombatParticipant** (167 connections) — `server/models/combat.py`
- **AsyncPersistenceLayer** (163 connections) — `server/async_persistence.py`
- **ConnectionManager** (162 connections) — `server/realtime/connection_manager.py`
- **CombatInstance** (155 connections) — `server/models/combat.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **async_persistence.py** (74 connections) — `server/async_persistence.py`
- **NATSError** (60 connections) — `server/services/nats_exceptions.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **models/combat.py** (50 connections) — `server/models/combat.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **TargetResolutionResult** (37 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **CombatParticipantData** (36 connections) — `server/services/combat_types.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **movement_service.py** (34 connections) — `server/game/movement_service.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- *... and 1053 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (200 shared connections)
- [PlayerService](PlayerService.md) (158 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (113 shared connections)
- [DatabaseError](DatabaseError.md) (95 shared connections)
- [event_types.py](event_types.py.md) (94 shared connections)
- [Player](Player.md) (68 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (62 shared connections)
- [UUID](UUID.md) (56 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (52 shared connections)
- [AliasStorage](AliasStorage.md) (44 shared connections)
- [CombatTurnProcessor](CombatTurnProcessor.md) (43 shared connections)
- [TauntCommandHandler](TauntCommandHandler.md) (32 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `server/api/base.py`
- `server/api/containers.py`
- `server/app/lifespan_startup.py`
- `server/app/task_registry.py`
- `server/async_persistence.py`
- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/caching/cache_service.py`
- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/commands/combat_taunt.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/go_command.py`
- `server/config/__init__.py`
- `server/config/models/cors.py`
- `server/constants/spawn_defaults.py`

## Audit Trail

- EXTRACTED: 4524 (95%)
- INFERRED: 239 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*