# Community 592

> 29 nodes

## Key Concepts

- **ContainerTransferFromMixin** (20 connections) — `server/services/container_service_transfer_from.py`
- **._execute_transfer_from_container()** (12 connections) — `server/services/container_service_transfer_from.py`
- **._finalize_loot_all()** (11 connections) — `server/services/container_service_transfer_from.py`
- **._persist_and_audit_transfer_from_container()** (10 connections) — `server/services/container_service_transfer_from.py`
- **InventoryStack** (9 connections)
- **UUID** (9 connections)
- **._loot_items_until_full()** (8 connections) — `server/services/container_service_transfer_from.py`
- **.transfer_from_container()** (8 connections) — `server/services/container_service_transfer_from.py`
- **._add_item_to_player_inventory()** (7 connections) — `server/services/container_service_transfer_from.py`
- **._resolve_container_stack()** (7 connections) — `server/services/container_service_transfer_from.py`
- **.loot_all()** (6 connections) — `server/services/container_service_transfer_from.py`
- **._remove_item_from_container()** (6 connections) — `server/services/container_service_transfer_from.py`
- **._prepare_transfer_item()** (4 connections) — `server/services/container_service_transfer_from.py`
- **test_resolve_container_stack_expands_client_identifier()** (4 connections) — `server/tests/unit/api/test_container_endpoints_basic_weapon.py`
- **test_resolve_container_stack_keeps_caller_item_when_instance_absent()** (4 connections) — `server/tests/unit/api/test_container_endpoints_basic_weapon.py`
- **Player** (4 connections)
- **Persist container changes and log audit trail.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Mutation-guarded body: remove stack, add to player, persist, audit.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Replace a caller-supplied stack with the container's own copy of it. The GUI…** (1 connections) — `server/services/container_service_transfer_from.py`
- **Transfer items from container to player inventory.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Transfer each container stack until capacity error; returns updated state.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Reload container, audit loot-all, and build response payload.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Transfer items from containers and loot-all.** (1 connections) — `server/services/container_service_transfer_from.py`
- **Loot all eligible items from a container (requires open mutation token).** (1 connections) — `server/services/container_service_transfer_from.py`
- **Prepare item for transfer, handling quantity and slot_type.** (1 connections) — `server/services/container_service_transfer_from.py`
- *... and 4 more nodes in this community*

## Relationships

- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (16 shared connections)
- [Community 94](Community_94.md) (6 shared connections)
- [Container API Models](Container_API_Models.md) (3 shared connections)
- [Community 178](Community_178.md) (1 shared connections)
- [Community 791](Community_791.md) (1 shared connections)
- [Community 78](Community_78.md) (1 shared connections)

## Source Files

- `server/services/container_service_transfer_from.py`
- `server/tests/unit/api/test_container_endpoints_basic_weapon.py`

## Audit Trail

- EXTRACTED: 80 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*