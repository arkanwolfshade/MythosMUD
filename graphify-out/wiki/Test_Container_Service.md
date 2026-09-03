# Test Container Service

> 168 nodes

## Key Concepts

- **ContainerService** (90 connections) — `server/services/container_service.py`
- **test_container_service.py** (73 connections) — `server/tests/unit/services/test_container_service.py`
- **InventoryMutationGuard** (33 connections) — `server/services/inventory_mutation_guard.py`
- **asyncio** (27 connections)
- **_container_data()** (25 connections) — `server/tests/unit/services/test_container_service.py`
- **_stack()** (21 connections) — `server/tests/unit/services/test_container_service.py`
- **inventory_mutation_guard.py** (21 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (18 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **MutationDecision** (17 connections) — `server/services/inventory_mutation_guard.py`
- **_container()** (15 connections) — `server/tests/unit/services/test_container_service.py`
- **_open_from_fixture()** (11 connections) — `server/tests/unit/services/test_container_service.py`
- **test_inventory_mutation_guard_error_handling.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_inventory_mutation_guard_sync.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **.acquire()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **_allow_all_mutations()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_capacity_exceeded()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_item_not_found()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_mutation_guard_suppressed()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_reraises_unexpected_error()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_success()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **Lock** (7 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **test_loot_all_stops_on_capacity_error()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 143 more nodes in this community*

## Relationships

- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (24 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (17 shared connections)
- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (14 shared connections)
- [Container Service Helpers](Container_Service_Helpers.md) (13 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (6 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Performance Monitor](Performance_Monitor.md) (5 shared connections)
- [Test Inventory Mutation Guard Async](Test_Inventory_Mutation_Guard_Async.md) (3 shared connections)
- [Test Inventory Mutation Guard Internal](Test_Inventory_Mutation_Guard_Internal.md) (3 shared connections)
- [Test Inventory Service](Test_Inventory_Service.md) (3 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (3 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (2 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 363 (79%)
- INFERRED: 95 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*