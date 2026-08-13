# ContainerService

> 55 nodes

## Key Concepts

- **ContainerService** (73 connections) — `server/services/container_service.py`
- **.transfer_from_container()** (16 connections) — `server/services/container_service.py`
- **UUID** (16 connections)
- **Any** (13 connections)
- **._validate_container_access()** (11 connections) — `server/services/container_service.py`
- **.open_container()** (10 connections) — `server/services/container_service.py`
- **.transfer_to_container()** (10 connections) — `server/services/container_service.py`
- **_filter_container_data()** (10 connections) — `server/services/container_service.py`
- **.loot_all()** (9 connections) — `server/services/container_service.py`
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
- *... and 30 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (29 shared connections)
- [ContainerComponent](ContainerComponent.md) (14 shared connections)
- [log_and_raise](log_and_raise.md) (13 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (9 shared connections)
- [UserManager](UserManager.md) (4 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (3 shared connections)
- [api/conftest.py](api-conftest.py.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`

## Audit Trail

- EXTRACTED: 163 (83%)
- INFERRED: 34 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*