# .get_instance

> 66 nodes

## Key Concepts

- **.get_instance()** (35 connections) — `server/container/main.py`
- **test_application_container.py** (29 connections) — `server/tests/unit/test_application_container.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container_creates_new_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_dict()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_empty_string()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_invalid()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_list()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_decode_json_column_none()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_project_root()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_service()** (3 connections) — `server/tests/unit/test_application_container.py`
- *... and 41 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (33 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [NPCStartupService](NPCStartupService.md) (3 shared connections)
- [UserManager](UserManager.md) (3 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (3 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (2 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (2 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [NATSError](NATSError.md) (2 shared connections)
- [HealthService](HealthService.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/game.py`
- `server/container/main.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 169 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*