# CombatService

> 1036 nodes · cohesion 0.00

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **NATSError** (98 connections) — `server/services/nats_exceptions.py`
- **NPCCombatIntegrationService** (89 connections) — `server/services/npc_combat_integration_service.py`
- **NATSService** (71 connections) — `server/services/nats_service.py`
- **NATSSubjectManager** (56 connections) — `server/services/nats_subject_manager/manager.py`
- **combat.py** (50 connections) — `server/models/combat.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **magic_service.py** (39 connections) — `server/game/magic/magic_service.py`
- **NPCCombatUUIDMapping** (39 connections) — `server/services/npc_combat_uuid_mapping.py`
- **CombatParticipantData** (38 connections) — `server/services/combat_types.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **NATSPublishError** (31 connections) — `server/services/nats_exceptions.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **nats_exceptions.py** (30 connections) — `server/services/nats_exceptions.py`
- **NPCCombatLucidity** (30 connections) — `server/services/npc_combat_lucidity.py`
- **NPCCombatDataProvider** (29 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **CombatEventPublisher** (27 connections) — `server/services/combat_event_publisher.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- *... and 1011 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (185 shared connections)
- [get_logger](get_logger.md) (128 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (45 shared connections)
- [TargetMatch](TargetMatch.md) (41 shared connections)
- [test_npc_combat_integration_service.py](test_npc_combat_integration_service.py.md) (41 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (32 shared connections)
- [SpellRegistry](SpellRegistry.md) (25 shared connections)
- [TauntCommandHandler](TauntCommandHandler.md) (24 shared connections)
- [ConnectionManager](ConnectionManager.md) (20 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (19 shared connections)
- [spell_effects_heal.py](spell_effects_heal.py.md) (17 shared connections)
- [exceptions.py](exceptions.py.md) (16 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/lifespan_startup.py`
- `server/commands/combat_taunt.py`
- `server/config/__init__.py`
- `server/container/bundles/combat.py`
- `server/events/combat_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_targeting.py`
- `server/game/mechanics.py`
- `server/infrastructure/nats_broker.py`
- `server/models/combat.py`
- `server/realtime/message_formatters.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`

## Audit Trail

- EXTRACTED: 4389 (92%)
- INFERRED: 405 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*