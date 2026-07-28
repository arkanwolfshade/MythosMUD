# NPC Combat Lifecycle

> 1036 nodes · cohesion 0.00

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **NATSError** (101 connections) — `server/services/nats_exceptions.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
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
- **nats_exceptions.py** (33 connections) — `server/services/nats_exceptions.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **NPCCombatLucidity** (30 connections) — `server/services/npc_combat_lucidity.py`
- **NPCCombatDataProvider** (29 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **CombatEventPublisher** (27 connections) — `server/services/combat_event_publisher.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- *... and 1011 more nodes in this community*

## Relationships

- [App Lifespan Management](App_Lifespan_Management.md) (185 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (128 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (45 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (45 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (41 shared connections)
- [Community 2205](Community_2205.md) (32 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (25 shared connections)
- [Cursor Plans Uvicorn](Cursor_Plans_Uvicorn.md) (24 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (19 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (19 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (17 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (16 shared connections)

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

- EXTRACTED: 4397 (92%)
- INFERRED: 405 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*