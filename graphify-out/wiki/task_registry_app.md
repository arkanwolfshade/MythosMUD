# task registry app

> 329 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **InventoryService** (40 connections) — `server/services/inventory_service.py`
- **InventoryMutationGuard** (39 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (38 connections) — `server/services/inventory_service.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **container_service_transfer_to.py** (33 connections) — `server/services/container_service_transfer_to.py`
- **inventory_service.py** (33 connections) — `server/services/inventory_service.py`
- **ContainerAccessDeniedError** (31 connections) — `server/services/container_service_helpers.py`
- **container.py** (30 connections) — `server/models/container.py`
- **container_service_session.py** (28 connections) — `server/services/container_service_session.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **container_service_transfer_from.py** (26 connections) — `server/services/container_service_transfer_from.py`
- **InventoryCapacityError** (26 connections) — `server/services/inventory_service.py`
- **container_service_helpers.py** (23 connections) — `server/services/container_service_helpers.py`
- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **MutationDecision** (19 connections) — `server/services/inventory_mutation_guard.py`
- **container_helpers_inventory_display.py** (18 connections) — `server/commands/container_helpers_inventory_display.py`
- **ContainerSessionMixin** (18 connections) — `server/services/container_service_session.py`
- **ContainerTransferFromMixin** (18 connections) — `server/services/container_service_transfer_from.py`
- **ContainerLockState** (17 connections) — `server/models/container.py`
- **container_service_access.py** (17 connections) — `server/services/container_service_access.py`
- **ContainerAccessMixin** (17 connections) — `server/services/container_service_access.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- *... and 304 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (69 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (66 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (46 shared connections)
- [player cache rationale](player_cache_rationale.md) (37 shared connections)
- [Error Conversion](Error_Conversion.md) (30 shared connections)
- [alias storage commands](alias_storage_commands.md) (20 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (17 shared connections)
- [event connection helpers](event_connection_helpers.md) (14 shared connections)
- [tick game processing](tick_game_processing.md) (13 shared connections)
- [container inventory display](container_inventory_display.md) (10 shared connections)
- [add used user](add_used_user.md) (10 shared connections)
- [Game Terminal UI](Game_Terminal_UI.md) (6 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_display.py`
- `server/models/container.py`
- `server/services/container_service_access.py`
- `server/services/container_service_helpers.py`
- `server/services/container_service_lock.py`
- `server/services/container_service_session.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- `server/tests/unit/services/test_inventory_service.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 1424 (88%)
- INFERRED: 188 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*