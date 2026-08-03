# Realtime Subscribers

> 490 nodes

## Key Concepts

- **EventBus** (159 connections) — `server/events/event_bus.py`
- **event_types.py** (86 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (85 connections) — `server/events/event_types.py`
- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **NPCLifecycleManager** (78 connections) — `server/npc/lifecycle_manager.py`
- **BaseEvent** (75 connections) — `server/events/event_types.py`
- **NPCSpawningService** (67 connections) — `server/npc/spawning_service.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **PlayerLeftRoom** (57 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (56 connections) — `server/events/event_types.py`
- **NPCLeftRoom** (52 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **event_bus.py** (31 connections) — `server/events/event_bus.py`
- **room.py** (30 connections) — `server/models/room.py`
- **event_reaction_system.py** (29 connections) — `server/npc/event_reaction_system.py`
- **NPCEventReactionSystem** (27 connections) — `server/npc/event_reaction_system.py`
- **combat_integration.py** (26 connections) — `server/npc/combat_integration.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- *... and 465 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (138 shared connections)
- [command parser rationale](command_parser_rationale.md) (64 shared connections)
- [NATS Messaging](NATS_Messaging.md) (60 shared connections)
- [NPC Combat](NPC_Combat.md) (49 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (28 shared connections)
- [item models rationale](item_models_rationale.md) (28 shared connections)
- [services nats service](services_nats_service.md) (21 shared connections)
- [npc event handlers](npc_event_handlers.md) (21 shared connections)
- [combat services rationale](combat_services_rationale.md) (20 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (18 shared connections)
- [Error Conversion](Error_Conversion.md) (15 shared connections)
- [player realtime event](player_realtime_event.md) (14 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/game/follow_service.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/npc_protocols.py`
- `server/npc/passive_mob_npc.py`

## Audit Trail

- EXTRACTED: 2636 (88%)
- INFERRED: 345 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*