# Player Effects API

> 56 nodes

## Key Concepts

- **ContainerService** (78 connections) — `server/services/container_service.py`
- **.transfer_from_container()** (18 connections) — `server/services/container_service.py`
- **UUID** (17 connections)
- **conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- **Any** (13 connections)
- **.transfer_to_container()** (13 connections) — `server/services/container_service.py`
- **.loot_all()** (11 connections) — `server/services/container_service.py`
- **_filter_container_data()** (10 connections) — `server/services/container_service.py`
- **._remove_item_from_container()** (8 connections) — `server/services/container_service.py`
- **._add_item_to_player_inventory()** (8 connections) — `server/services/container_service.py`
- **._persist_and_audit_transfer_from_container()** (8 connections) — `server/services/container_service.py`
- **_get_enum_value()** (7 connections) — `server/services/container_service.py`
- **._verify_container_open()** (7 connections) — `server/services/container_service.py`
- **._validate_container_close()** (6 connections) — `server/services/container_service.py`
- **._audit_log_container_close()** (6 connections) — `server/services/container_service.py`
- **.close_container()** (6 connections) — `server/services/container_service.py`
- **InventoryStack** (6 connections)
- **._remove_container_from_open_list()** (4 connections) — `server/services/container_service.py`
- **.get_container_token()** (4 connections) — `server/services/container_service.py`
- **._prepare_transfer_item()** (4 connections) — `server/services/container_service.py`
- **.test_get_container_service_with_persistence()** (4 connections) — `server/tests/unit/api/test_containers.py`
- **.test_get_container_service_from_request()** (4 connections) — `server/tests/unit/api/test_containers.py`
- **mock_container_service()** (3 connections) — `server/tests/unit/api/conftest.py`
- **mock_container()** (3 connections) — `server/tests/unit/api/conftest.py`
- **mock_container_service()** (3 connections) — `server/tests/unit/api/test_containers.py`
- *... and 31 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (50 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (18 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (13 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (9 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (6 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (4 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (3 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (2 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (1 shared connections)
- [Grace Period Blocking Tests](Grace_Period_Blocking_Tests.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 250 (83%)
- INFERRED: 51 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*