# Container Loot Helpers

> 82 nodes · cohesion 0.05

## Key Concepts

- **ContainerService** (75 connections) — `server/services/container_service.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **UUID** (21 connections) — `server/services/container_service.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **test_container_helpers_loot.py** (19 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Any** (17 connections) — `server/services/container_service.py`
- **.transfer_from_container()** (14 connections) — `server/services/container_service.py`
- **ContainerComponent** (12 connections) — `server/services/container_service.py`
- **InventoryStack** (10 connections) — `server/services/container_service.py`
- **._validate_container_access()** (10 connections) — `server/services/container_service.py`
- **_filter_container_data()** (10 connections) — `server/services/container_service.py`
- **.loot_all()** (9 connections) — `server/services/container_service.py`
- **.open_container()** (9 connections) — `server/services/container_service.py`
- **.transfer_to_container()** (9 connections) — `server/services/container_service.py`
- **._persist_and_audit_transfer_from_container()** (8 connections) — `server/services/container_service.py`
- **.unlock_container()** (8 connections) — `server/services/container_service.py`
- **._add_item_to_player_inventory()** (7 connections) — `server/services/container_service.py`
- **.lock_container()** (7 connections) — `server/services/container_service.py`
- **._remove_item_from_container()** (7 connections) — `server/services/container_service.py`
- **._verify_container_open()** (7 connections) — `server/services/container_service.py`
- **_get_enum_value()** (7 connections) — `server/services/container_service.py`
- **.test_transfer_all_items_from_container_capacity_error()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_partial_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_transfer_error()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **._audit_log_container_close()** (6 connections) — `server/services/container_service.py`
- *... and 57 more nodes in this community*

## Relationships

- [[Container API Endpoints]] (28 shared connections)
- [[Inventory Service Helpers]] (28 shared connections)
- [[Container Exception Handlers]] (18 shared connections)
- [[Loot All Endpoint]] (16 shared connections)
- [[NPC Admin API]] (14 shared connections)
- [[Game Service Bundle]] (7 shared connections)
- [[API Test Fixtures]] (3 shared connections)
- [[Container Component Capacity]] (2 shared connections)
- [[Database Manager Tests]] (2 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 406 (88%)
- INFERRED: 56 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
