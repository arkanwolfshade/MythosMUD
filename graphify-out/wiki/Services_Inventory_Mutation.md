# Services Inventory Mutation

> 171 nodes · cohesion 0.02

## Key Concepts

- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **MutationDecision** (18 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_internal.py** (15 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_error_handling.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Lock** (9 connections)
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **InventoryServiceError** (9 connections) — `server/services/inventory_service.py`
- **test_inventory_mutation_guard_async.py** (9 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **._validate_and_clone_optional_fields()** (7 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **InnerContainer** (6 connections) — `server/services/inventory_service.py`
- **InventoryStackRequired** (6 connections) — `server/services/inventory_service.py`
- **.get_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- *... and 146 more nodes in this community*

## Relationships

- [Commands Inventory Item](Commands_Inventory_Item.md) (48 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (14 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (6 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (3 shared connections)
- [Lucidity Rescue Helpers](Lucidity_Rescue_Helpers.md) (2 shared connections)
- [Inventory Test Support](Inventory_Test_Support.md) (2 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (2 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (1 shared connections)
- [Middleware Metrics Collector](Middleware_Metrics_Collector.md) (1 shared connections)
- [Whisper Reply Command Tests](Whisper_Reply_Command_Tests.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 491 (87%)
- INFERRED: 71 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*