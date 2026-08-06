# Exception Containers

> 518 nodes

## Key Concepts

- **ContainerComponent** (110 connections) — `server/models/container.py`
- **RateLimitError** (76 connections) — `server/exceptions.py`
- **LootAllRequest** (62 connections) — `server/api/container_models.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **container_helpers.py** (42 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (42 connections) — `server/tests/unit/api/test_container_helpers.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **ContainerSourceType** (29 connections) — `server/models/container.py`
- **test_containers.py** (26 connections) — `server/tests/unit/api/test_containers.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **test_container_helpers_loot.py** (22 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **OpenContainerRequest** (17 connections) — `server/api/container_models.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- *... and 493 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (118 shared connections)
- [task registry app](task_registry_app.md) (69 shared connections)
- [alias storage commands](alias_storage_commands.md) (60 shared connections)
- [player requests schemas](player_requests_schemas.md) (45 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (24 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (18 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (14 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (12 shared connections)
- [message handler factory](message_handler_factory.md) (12 shared connections)
- [Game Terminal UI](Game_Terminal_UI.md) (12 shared connections)
- [Error Conversion](Error_Conversion.md) (10 shared connections)
- [command handler unified](command_handler_unified.md) (7 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/exceptions.py`
- `server/models/container.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 2007 (84%)
- INFERRED: 392 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*