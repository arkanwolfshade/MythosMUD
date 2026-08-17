# EventBus

> 156 nodes

## Key Concepts

- **EventBus** (153 connections) — `server/events/event_bus.py`
- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **Any** (10 connections)
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **._stop_processing()** (7 connections) — `server/events/event_bus.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **._create_async_subscriber_tasks()** (6 connections) — `server/events/event_bus.py`
- **._ensure_async_processing()** (6 connections) — `server/events/event_bus.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **._process_sync_subscribers()** (5 connections) — `server/events/event_bus.py`
- **._separate_subscribers()** (5 connections) — `server/events/event_bus.py`
- **.unsubscribe()** (5 connections) — `server/events/event_bus.py`
- **._wait_for_async_subscribers()** (5 connections) — `server/events/event_bus.py`
- **._check_spawn_requirements_for_room()** (5 connections) — `server/npc/spawning_service.py`
- **.get_spawn_statistics()** (5 connections) — `server/npc/spawning_service.py`
- **test_spawning_service_npc_room_event_handlers()** (5 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **NPCSpawnRequest** (5 connections)
- *... and 131 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (41 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (21 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (20 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (18 shared connections)
- [NPCDefinition](NPCDefinition.md) (10 shared connections)
- [npc_base.py](npc_base.py.md) (8 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [test_party_flow.py](test_party_flow.py.md) (4 shared connections)
- [NPCBase](NPCBase.md) (4 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (3 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/npc/event_reaction_system.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 369 (83%)
- INFERRED: 78 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*