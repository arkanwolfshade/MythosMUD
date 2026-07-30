# NPCLifecycleManager

> 66 nodes

## Key Concepts

- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (5 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (4 connections) — `server/app/lifespan_startup.py`
- **Any** (4 connections)
- **_validate_npc_services_prerequisites()** (4 connections) — `server/app/lifespan_startup.py`
- **_start_npc_thread_manager_and_pending()** (4 connections) — `server/app/lifespan_startup.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (4 connections) — `server/app/lifespan_startup.py`
- **test_initialize_container_and_legacy_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_no_item_factory()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_async_registry()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_setup_connection_manager()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 41 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (20 shared connections)
- [test command parser](test_command_parser.md) (12 shared connections)
- [.shutdown()](shutdown%28%29.md) (7 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (4 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [get health status()](get_health_status%28%29.md) (3 shared connections)
- [message handler factory](message_handler_factory.md) (3 shared connections)
- [process dead players()](process_dead_players%28%29.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 291 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*