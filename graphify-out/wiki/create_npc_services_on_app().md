# create npc services on app()

> 44 nodes

## Key Concepts

- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (4 connections) — `server/app/lifespan_startup.py`
- **_start_npc_thread_manager_and_pending()** (4 connections) — `server/app/lifespan_startup.py`
- **test_initialize_container_and_legacy_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_no_item_factory()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_async_registry()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_setup_connection_manager()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_setup_connection_manager_no_manager()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_npc_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_combat_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_mythos_time_consumer()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_npc_startup_spawning()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_nats_and_combat_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_chat_service()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_magic_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **mock_app()** (2 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **mock_container()** (2 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **Test initialize_container_and_legacy_services() initializes container.** (2 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **Initialize container and set up container reference on app.state.      Services** (1 connections) — `server/app/lifespan_startup.py`
- *... and 19 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (14 shared connections)
- [lifespan](lifespan.md) (9 shared connections)
- [.shutdown()](shutdown%28%29.md) (7 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (4 shared connections)
- [get item prototype count()](get_item_prototype_count%28%29.md) (3 shared connections)
- [. repr ()](_repr_%28%29.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [. post init ()](_post_init_%28%29.md) (1 shared connections)
- [time commands](time_commands.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (1 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 158 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*