# container_service_transfer_to.py

> 89 nodes

## Key Concepts

- **container_service_transfer_to.py** (33 connections) — `server/services/container_service_transfer_to.py`
- **container_service_transfer_from.py** (26 connections) — `server/services/container_service_transfer_from.py`
- **container_service_helpers.py** (23 connections) — `server/services/container_service_helpers.py`
- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **ContainerSessionMixin** (18 connections) — `server/services/container_service_session.py`
- **ContainerTransferFromMixin** (18 connections) — `server/services/container_service_transfer_from.py`
- **filter_container_data()** (14 connections) — `server/services/container_service_helpers.py`
- **as_object_dict()** (12 connections) — `server/services/container_service_helpers.py`
- **._execute_transfer_from_container()** (12 connections) — `server/services/container_service_transfer_from.py`
- **._execute_transfer_to_container()** (12 connections) — `server/services/container_service_transfer_to.py`
- **get_enum_value()** (11 connections) — `server/services/container_service_helpers.py`
- **._finalize_loot_all()** (10 connections) — `server/services/container_service_transfer_from.py`
- **._require_container_component()** (10 connections) — `server/services/container_service_transfer_to.py`
- **UUID** (10 connections)
- **player_inventory_for_response()** (9 connections) — `server/services/container_service_helpers.py`
- **.open_container()** (9 connections) — `server/services/container_service_session.py`
- **._persist_and_audit_transfer_from_container()** (9 connections) — `server/services/container_service_transfer_from.py`
- **.transfer_to_container()** (9 connections) — `server/services/container_service_transfer_to.py`
- **UUID** (9 connections)
- **UUID** (9 connections)
- **items_json_for_persist()** (8 connections) — `server/services/container_service_helpers.py`
- **._raise_if_cannot_open_locks()** (8 connections) — `server/services/container_service_session.py`
- **._add_item_to_player_inventory()** (8 connections) — `server/services/container_service_transfer_from.py`
- **._loot_items_until_full()** (8 connections) — `server/services/container_service_transfer_from.py`
- **InventoryStack** (8 connections)
- *... and 64 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (27 shared connections)
- [ContainerComponent](ContainerComponent.md) (24 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (16 shared connections)
- [log_and_raise](log_and_raise.md) (16 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (3 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (2 shared connections)
- [audit_logger.py](audit_logger.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/services/container_service_helpers.py`
- `server/services/container_service_session.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 271 (90%)
- INFERRED: 29 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*