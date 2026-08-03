# container events rationale

> 159 nodes

## Key Concepts

- **ContainerSourceType** (27 connections) — `server/models/container.py`
- **container.py** (25 connections) — `server/models/container.py`
- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **ContainerLockState** (14 connections) — `server/models/container.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **Any** (8 connections)
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **TestEmitContainerOpenedEventsEdgeCases** (8 connections) — `server/tests/unit/api/test_container_events.py`
- **.create_corpse()** (7 connections) — `server/models/container.py`
- **.create_environment()** (6 connections) — `server/models/container.py`
- **.create_equipment()** (6 connections) — `server/models/container.py`
- *... and 134 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (58 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (18 shared connections)
- [command inventory factories](command_inventory_factories.md) (9 shared connections)
- [task registry app](task_registry_app.md) (9 shared connections)
- [Exception Containers](Exception_Containers.md) (5 shared connections)
- [Database Config](Database_Config.md) (5 shared connections)
- [tick game processing](tick_game_processing.md) (4 shared connections)
- [world models rationale](world_models_rationale.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (2 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (2 shared connections)
- [alias storage commands](alias_storage_commands.md) (2 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/models/container.py`
- `server/services/container_websocket_events.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 587 (95%)
- INFERRED: 28 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*