# server npc npc base npcbase

> 182 nodes

## Key Concepts

- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (66 connections) — `server/npc/spawning_service.py`
- **test_spawning_modules.py** (41 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **spawning_models.py** (13 connections) — `server/npc/spawning_models.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- *... and 157 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (56 shared connections)
- [moduletype](moduletype.md) (29 shared connections)
- [jsondict](jsondict.md) (24 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (22 shared connections)
- [server game mechanics](server_game_mechanics.md) (9 shared connections)
- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (8 shared connections)
- [server npc population control npcpopulationcontroller](server_npc_population_control_npcpopulationcontroller.md) (5 shared connections)
- [server events event types npcdied](server_events_event_types_npcdied.md) (4 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (2 shared connections)
- [server npc aggressive mob npc](server_npc_aggressive_mob_npc.md) (2 shared connections)
- [server npc passive mob npc](server_npc_passive_mob_npc.md) (2 shared connections)
- [server npc shopkeeper npc rationale](server_npc_shopkeeper_npc_rationale.md) (2 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 434 (88%)
- INFERRED: 58 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*