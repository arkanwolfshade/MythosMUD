# rescue_commands.py

> 105 nodes · cohesion 0.04

## Key Concepts

- **lifespan_startup.py** (66 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (42 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **FastAPI** (16 connections)
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (15 connections)
- **test_combat_skill_wiring.py** (14 connections) — `server/tests/unit/container/test_combat_skill_wiring.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **_attach_combat_service()** (11 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (9 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (6 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **test_setup_connection_manager()** (6 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **nats_is_connected()** (5 connections) — `server/app/lifespan_protocols.py`
- **_log_npc_startup_errors()** (5 connections) — `server/app/lifespan_startup.py`
- **_start_nats_message_handler()** (5 connections) — `server/app/lifespan_startup.py`
- *... and 80 more nodes in this community*

## Relationships

- [test_message_handlers.py](test_message_handlers.py.md) (18 shared connections)
- [CombatInstance](CombatInstance.md) (10 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (8 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (7 shared connections)
- [Room](Room.md) (5 shared connections)
- [SpellLearningService](SpellLearningService.md) (4 shared connections)
- [RoomLoader](RoomLoader.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [player.ts](player.ts.md) (3 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [Communities (11 total, 0 thin omitted)](Communities_11_total,_0_thin_omitted.md) (3 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/container/test_combat_skill_wiring.py`

## Audit Trail

- EXTRACTED: 299 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*