# server api container helpers get

> 123 nodes

## Key Concepts

- **ContainerService** (79 connections) — `server/services/container_service.py`
- **test_container_service.py** (61 connections) — `server/tests/unit/services/test_container_service.py`
- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **ContainerLockState** (42 connections) — `server/models/container.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **asyncio** (18 connections)
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (15 connections) — `server/services/inventory_mutation_guard.py`
- **asyncio** (14 connections)
- **_stack()** (12 connections) — `server/tests/unit/services/test_container_service.py`
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestHandleContainerServiceErrorEdgeCases** (8 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestHandleContainerServiceError** (8 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_transfer_all_items_from_container_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_empty_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_item_without_quantity()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_multiple_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_partial_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_container()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_inventory()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 98 more nodes in this community*

## Relationships

- [server models container containercomponent](server_models_container_containercomponent.md) (57 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (34 shared connections)
- [server api container endpoints loot](server_api_container_endpoints_loot.md) (24 shared connections)
- [server services container service](server_services_container_service.md) (22 shared connections)
- [server api container events](server_api_container_events.md) (14 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (9 shared connections)
- [server services inventory mutation guard](server_services_inventory_mutation_guard.md) (7 shared connections)
- [server api players](server_api_players.md) (6 shared connections)
- [dependsparam](dependsparam.md) (4 shared connections)
- [server services environmental container loader](server_services_environmental_container_loader.md) (3 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (3 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (3 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 354 (75%)
- INFERRED: 119 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*