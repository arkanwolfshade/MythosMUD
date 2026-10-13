# Community 791

> 21 nodes

## Key Concepts

- **ContainerTransferToMixin** (17 connections) — `server/services/container_service_transfer_to.py`
- **._execute_transfer_to_container()** (12 connections) — `server/services/container_service_transfer_to.py`
- **._require_container_component()** (9 connections) — `server/services/container_service_transfer_to.py`
- **.transfer_to_container()** (9 connections) — `server/services/container_service_transfer_to.py`
- **UUID** (9 connections)
- **._audit_transfer_to_container()** (8 connections) — `server/services/container_service_transfer_to.py`
- **InventoryStack** (7 connections)
- **._add_stack_to_container_or_raise()** (6 connections) — `server/services/container_service_transfer_to.py`
- **._require_container_has_capacity()** (6 connections) — `server/services/container_service_transfer_to.py`
- **._require_player_for_transfer()** (6 connections) — `server/services/container_service_transfer_to.py`
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

- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (13 shared connections)
- [Community 94](Community_94.md) (5 shared connections)
- [Community 592](Community_592.md) (1 shared connections)
- [Community 297](Community_297.md) (1 shared connections)
- [Community 78](Community_78.md) (1 shared connections)

## Source Files

- `server/services/container_service_transfer_to.py`

## Audit Trail

- EXTRACTED: 58 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*