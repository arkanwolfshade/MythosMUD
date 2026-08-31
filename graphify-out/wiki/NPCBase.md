# NPCBase

> 295 nodes

## Key Concepts

- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **test_behavior_engine.py** (55 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **NPCEventReactionSystem** (24 connections) — `server/npc/event_reaction_system.py`
- **aggressive_mob_npc.py** (19 connections) — `server/npc/aggressive_mob_npc.py`
- **passive_mob_npc.py** (18 connections) — `server/npc/passive_mob_npc.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **.event_bus()** (14 connections) — `server/realtime/connection_manager.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **shopkeeper_npc.py** (13 connections) — `server/npc/shopkeeper_npc.py`
- **Any** (12 connections)
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **CommunicationIntegrationProtocol** (8 connections) — `server/npc/npc_protocols.py`
- **_build_aggressive()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **._try_evaluators()** (7 connections) — `server/npc/behavior_engine.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **behavior_engine.py** (7 connections) — `server/npc/behavior_engine.py`
- **CombatIntegrationProtocol** (6 connections) — `server/npc/npc_protocols.py`
- **.evaluate_condition()** (6 connections) — `server/npc/behavior_engine.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- *... and 270 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (36 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (20 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [EventBus](EventBus.md) (15 shared connections)
- [test_event_reaction_speech.py](test_event_reaction_speech.py.md) (14 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (8 shared connections)
- [NPCDefinition](NPCDefinition.md) (7 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (6 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (6 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/npc/behavior_engine.py`
- `server/npc/behaviors.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_protocols.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_service.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/npc/test_behavior_engine.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 577 (94%)
- INFERRED: 39 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*