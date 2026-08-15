# .get_instance

> 63 nodes

## Key Concepts

- **.get_instance()** (34 connections) — `server/container/main.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
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
- **test_application_container_get_service_invalid()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_service_not_initialized_service()** (3 connections) — `server/tests/unit/test_application_container.py`
- *... and 38 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (30 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [NPCStartupService](NPCStartupService.md) (3 shared connections)
- [UserManager](UserManager.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (2 shared connections)
- [HealthService](HealthService.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (1 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/main.py`
- `server/npc/npc_base.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 144 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*