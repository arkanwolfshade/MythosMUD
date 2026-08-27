# test_who_commands.py

> 97 nodes

## Key Concepts

- **lifespan_startup.py** (49 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (42 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **FastAPI** (16 connections)
- **FastAPI** (15 connections)
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (9 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_combat_services()** (8 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (7 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **nats_is_connected()** (6 connections) — `server/app/lifespan_protocols.py`
- **_attach_combat_service()** (6 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **test_setup_connection_manager()** (6 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **_create_npc_services_on_app()** (5 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (5 connections) — `server/app/lifespan_startup.py`
- **_start_nats_message_handler()** (5 connections) — `server/app/lifespan_startup.py`
- **mock_app()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_chat_service()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 72 more nodes in this community*

## Relationships

- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (14 shared connections)
- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (7 shared connections)
- [ContainerComponent](ContainerComponent.md) (6 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (2 shared connections)
- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (2 shared connections)
- [3. REFACTOR Findings (935 findings)](3._REFACTOR_Findings_935_findings.md) (2 shared connections)
- [look_command.py](look_command.py.md) (2 shared connections)
- [Asynchronous Code Audit - December 3, 2025](Asynchronous_Code_Audit_-_December_3,_2025.md) (1 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 246 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*