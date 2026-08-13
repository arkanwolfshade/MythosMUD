# .transfer_from_container

> 53 nodes

## Key Concepts

- **.transfer_from_container()** (16 connections) — `server/services/container_service.py`
- **UUID** (16 connections)
- **Any** (13 connections)
- **._validate_container_access()** (11 connections) — `server/services/container_service.py`
- **.open_container()** (10 connections) — `server/services/container_service.py`
- **.transfer_to_container()** (10 connections) — `server/services/container_service.py`
- **_filter_container_data()** (10 connections) — `server/services/container_service.py`
- **.loot_all()** (9 connections) — `server/services/container_service.py`
- **.is_admin()** (9 connections) — `server/services/user_manager.py`
- **.lock_container()** (8 connections) — `server/services/container_service.py`
- **._persist_and_audit_transfer_from_container()** (8 connections) — `server/services/container_service.py`
- **.unlock_container()** (8 connections) — `server/services/container_service.py`
- **ContainerComponent** (8 connections)
- **._add_item_to_player_inventory()** (7 connections) — `server/services/container_service.py`
- **._can_unlock_container()** (7 connections) — `server/services/container_service.py`
- **._remove_item_from_container()** (7 connections) — `server/services/container_service.py`
- **._verify_container_open()** (7 connections) — `server/services/container_service.py`
- **_get_enum_value()** (7 connections) — `server/services/container_service.py`
- **._audit_log_container_close()** (6 connections) — `server/services/container_service.py`
- **.close_container()** (6 connections) — `server/services/container_service.py`
- **._validate_proximity()** (6 connections) — `server/services/container_service.py`
- **InventoryStack** (6 connections)
- **._validate_container_close()** (5 connections) — `server/services/container_service.py`
- **._validate_corpse_grace_period()** (5 connections) — `server/services/container_service.py`
- **._validate_ownership()** (5 connections) — `server/services/container_service.py`
- *... and 28 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (27 shared connections)
- [log_and_raise](log_and_raise.md) (13 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (3 shared connections)
- [UserManager](UserManager.md) (3 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 141 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*