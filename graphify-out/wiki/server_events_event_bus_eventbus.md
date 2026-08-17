# server events event bus eventbus

> 235 nodes

## Key Concepts

- **EventBus** (149 connections) — `server/events/event_bus.py`
- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **Any** (10 connections)
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **_build_aggressive()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **._stop_processing()** (7 connections) — `server/events/event_bus.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **._create_async_subscriber_tasks()** (6 connections) — `server/events/event_bus.py`
- *... and 210 more nodes in this community*

## Relationships

- [server events event bus](server_events_event_bus.md) (36 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (27 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (26 shared connections)
- [draft7validator](draft7validator.md) (23 shared connections)
- [moduletype](moduletype.md) (15 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (14 shared connections)
- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (11 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (8 shared connections)
- [server npc population control npcpopulationcontroller](server_npc_population_control_npcpopulationcontroller.md) (7 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (7 shared connections)
- [server models npc npcdefinition is](server_models_npc_npcdefinition_is.md) (6 shared connections)
- [server tests unit events test](server_tests_unit_events_test.md) (5 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/npc/behaviors.py`
- `server/npc/npc_base.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 575 (84%)
- INFERRED: 109 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*