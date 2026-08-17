# server app lifespan startup

> 87 nodes

## Key Concepts

- **lifespan_startup.py** (64 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (41 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (8 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **_start_npc_thread_manager_and_pending()** (4 connections) — `server/app/lifespan_startup.py`
- **test_get_item_prototype_count_non_iterable()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_get_item_prototype_entries_async_failure()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_get_item_prototype_entries_missing_all_method()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_get_item_prototype_entries_none_registry()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 62 more nodes in this community*

## Relationships

- [server container bundles chat](server_container_bundles_chat.md) (11 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server app lifespan](server_app_lifespan.md) (7 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (7 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (4 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (4 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (3 shared connections)
- [holidayresolver](holidayresolver.md) (3 shared connections)
- [server services npc startup service](server_services_npc_startup_service.md) (3 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (3 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (3 shared connections)
- [server game chat service chatservice](server_game_chat_service_chatservice.md) (2 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 244 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*