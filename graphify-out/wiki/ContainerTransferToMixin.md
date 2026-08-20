# ContainerTransferToMixin

> 22 nodes

## Key Concepts

- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **._execute_transfer_to_container()** (12 connections) — `server/services/container_service_transfer_to.py`
- **._require_container_component()** (10 connections) — `server/services/container_service_transfer_to.py`
- **.transfer_to_container()** (9 connections) — `server/services/container_service_transfer_to.py`
- **UUID** (9 connections)
- **._add_stack_to_container_or_raise()** (7 connections) — `server/services/container_service_transfer_to.py`
- **._audit_transfer_to_container()** (7 connections) — `server/services/container_service_transfer_to.py`
- **._require_container_has_capacity()** (7 connections) — `server/services/container_service_transfer_to.py`
- **._require_player_for_transfer()** (7 connections) — `server/services/container_service_transfer_to.py`
- **InventoryStack** (7 connections)
- **ContainerComponent** (5 connections)
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

- [ContainerServiceError](ContainerServiceError.md) (14 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (2 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/services/container_service_transfer_to.py`

## Audit Trail

- EXTRACTED: 61 (88%)
- INFERRED: 8 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*