# .initialize()

> 390 nodes

## Key Concepts

- **EventBus** (123 connections) — `server/events/event_bus.py`
- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **NPCPopulationController** (58 connections) — `server/npc/population_control.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (44 connections) — `server/npc/spawning_service.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **AggressiveMobNPC** (32 connections) — `server/npc/aggressive_mob_npc.py`
- **PassiveMobNPC** (29 connections) — `server/npc/passive_mob_npc.py`
- **combat_integration.py** (25 connections) — `server/npc/combat_integration.py`
- **NPCEventReactionSystem** (25 connections) — `server/npc/event_reaction_system.py`
- **spawning_instance_factory.py** (24 connections) — `server/npc/spawning_instance_factory.py`
- **test_npc_combat_integration_class.py** (23 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **__init__.py** (22 connections) — `server/npc/__init__.py`
- **spawning_request_execution.py** (19 connections) — `server/npc/spawning_request_execution.py`
- **aggressive_mob_npc.py** (18 connections) — `server/npc/aggressive_mob_npc.py`
- **passive_mob_npc.py** (18 connections) — `server/npc/passive_mob_npc.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **ShopkeeperNPC** (17 connections) — `server/npc/shopkeeper_npc.py`
- **NPCSpawnStatistics** (16 connections) — `server/npc/spawning_service.py`
- **SimpleNPCDefinition** (15 connections) — `server/npc/spawning_models.py`
- **NPCSpawnResult** (14 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (13 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_models.py** (12 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (12 connections) — `server/npc/spawning_request_execution.py`
- *... and 365 more nodes in this community*

## Relationships

- [. repr ()](_repr_%28%29.md) (79 shared connections)
- [Any](Any.md) (70 shared connections)
- [main()](main%28%29.md) (40 shared connections)
- [. create async subscriber tasks()](_create_async_subscriber_tasks%28%29.md) (20 shared connections)
- [. init ()](_init_%28%29.md) (17 shared connections)
- [.initialize()](initialize%28%29.md) (16 shared connections)
- [.is required()](is_required%28%29.md) (16 shared connections)
- [Return stats\[key\] as int, or](Return_stats%5Bkey%5D_as_int%2C_or.md) (16 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (14 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (13 shared connections)
- [Schedule end combat if npc](Schedule_end_combat_if_npc.md) (13 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (11 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/event_bus.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_base.py`

## Audit Trail

- EXTRACTED: 1524 (91%)
- INFERRED: 143 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*