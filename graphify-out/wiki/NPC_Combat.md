# NPC Combat

> 526 nodes

## Key Concepts

- **AsyncPersistenceLayer** (184 connections) — `server/async_persistence.py`
- **CombatService** (181 connections) — `server/services/combat_service.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **NPCCombatIntegrationService** (89 connections) — `server/services/npc_combat_integration_service.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **NPCCombatUUIDMapping** (39 connections) — `server/services/npc_combat_uuid_mapping.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCCombatLucidity** (30 connections) — `server/services/npc_combat_lucidity.py`
- **NPCCombatDataProvider** (29 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **CombatEventPublisher** (27 connections) — `server/services/combat_event_publisher.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- *... and 501 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (133 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (51 shared connections)
- [command inventory factories](command_inventory_factories.md) (43 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (42 shared connections)
- [Spell Validation](Spell_Validation.md) (41 shared connections)
- [target resolution service](target_resolution_service.md) (39 shared connections)
- [command models admin](command_models_admin.md) (33 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (32 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (30 shared connections)
- [models npc rationale](models_npc_rationale.md) (28 shared connections)
- [player service game](player_service_game.md) (27 shared connections)
- [Database Config](Database_Config.md) (24 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/async_persistence.py`
- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/container/bundles/combat.py`
- `server/events/combat_events.py`
- `server/game/magic/spell_targeting.py`
- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`
- `server/realtime/connection_manager.py`
- `server/services/active_lucidity_service.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`

## Audit Trail

- EXTRACTED: 2477 (89%)
- INFERRED: 314 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*