# Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)

> 21 nodes · cohesion 0.20

## Key Concepts

- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **._execute_transfer_to_container()** (12 connections) — `server/services/container_service_transfer_to.py`
- **._require_container_component()** (10 connections) — `server/services/container_service_transfer_to.py`
- **.transfer_to_container()** (9 connections) — `server/services/container_service_transfer_to.py`
- **UUID** (9 connections)
- **._audit_transfer_to_container()** (8 connections) — `server/services/container_service_transfer_to.py`
- **._add_stack_to_container_or_raise()** (7 connections) — `server/services/container_service_transfer_to.py`
- **._require_container_has_capacity()** (7 connections) — `server/services/container_service_transfer_to.py`
- **._require_player_for_transfer()** (7 connections) — `server/services/container_service_transfer_to.py`
- **InventoryStack** (7 connections)
- **._log_container_data_before_validation()** (4 connections) — `server/services/container_service_transfer_to.py`
- **Player** (3 connections)
- **Best-effort audit log for transfer-to-container (must not fail the transfer).** (1 connections) — `server/services/container_service_transfer_to.py`
- **Add a stack via InventoryService; map capacity failures to…** (1 connections) — `server/services/container_service_transfer_to.py`
- **Load player or raise ValidationError for transfer ops.** (1 connections) — `server/services/container_service_transfer_to.py`
- **Load and validate container component for transfer-to.** (1 connections) — `server/services/container_service_transfer_to.py`
- **Mutation-guarded body: add stack, persist, audit, return response.** (1 connections) — `server/services/container_service_transfer_to.py`
- **Transfer items from player inventory to container.** (1 connections) — `server/services/container_service_transfer_to.py`
- **Transfer items into containers.** (1 connections) — `server/services/container_service_transfer_to.py`
- **Debug shape of container_data from persistence before Pydantic validate.** (1 connections) — `server/services/container_service_transfer_to.py`
- **Raise ContainerCapacityError when the container has no free slots.** (1 connections) — `server/services/container_service_transfer_to.py`

## Relationships

- [test_command_factories.py](test_command_factories.py.md) (9 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (6 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (5 shared connections)
- [endpoints.py](endpoints.py.md) (4 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (2 shared connections)
- [test_metadata.py](test_metadata.py.md) (1 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (1 shared connections)

## Source Files

- `server/services/container_service_transfer_to.py`

## Audit Trail

- EXTRACTED: 62 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*