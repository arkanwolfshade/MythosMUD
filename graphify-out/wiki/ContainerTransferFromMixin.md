# ContainerTransferFromMixin

> 23 nodes

## Key Concepts

- **ContainerTransferFromMixin** (18 connections) — `server/services/container_service_transfer_from.py`
- **._execute_transfer_from_container()** (12 connections) — `server/services/container_service_transfer_from.py`
- **._finalize_loot_all()** (10 connections) — `server/services/container_service_transfer_from.py`
- **._persist_and_audit_transfer_from_container()** (9 connections) — `server/services/container_service_transfer_from.py`
- **UUID** (9 connections)
- **._add_item_to_player_inventory()** (8 connections) — `server/services/container_service_transfer_from.py`
- **._loot_items_until_full()** (8 connections) — `server/services/container_service_transfer_from.py`
- **InventoryStack** (8 connections)
- **.loot_all()** (7 connections) — `server/services/container_service_transfer_from.py`
- **._remove_item_from_container()** (7 connections) — `server/services/container_service_transfer_from.py`
- **.transfer_from_container()** (7 connections) — `server/services/container_service_transfer_from.py`
- **._prepare_transfer_item()** (4 connections) — `server/services/container_service_transfer_from.py`
- **Player** (4 connections)
- **Persist container changes and log audit trail.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Mutation-guarded body: remove stack, add to player, persist, audit.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Transfer items from container to player inventory.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Transfer each container stack until capacity error; returns updated state.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Reload container, audit loot-all, and build response payload.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Loot all eligible items from a container (requires open mutation token).** (1 connections) — `server/services/container_service_transfer_from.py`
- **Transfer items from containers and loot-all.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Prepare item for transfer, handling quantity and slot_type.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Remove item from container items list.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Add item to player inventory using InventoryService.** (1 connections) — `server/services/container_service_transfer_from.py`

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (16 shared connections)
- [ContainerComponent](ContainerComponent.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [ContainerService](ContainerService.md) (1 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/services/container_service_transfer_from.py`

## Audit Trail

- EXTRACTED: 69 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*