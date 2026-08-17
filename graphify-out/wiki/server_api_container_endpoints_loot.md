# server api container endpoints loot

> 133 nodes

## Key Concepts

- **ContainerService** (79 connections) — `server/services/container_service.py`
- **test_container_service.py** (61 connections) — `server/tests/unit/services/test_container_service.py`
- **LootAllRequest** (58 connections) — `server/api/container_models.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **asyncio** (18 connections)
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **_container()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (15 connections) — `server/services/inventory_mutation_guard.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **asyncio** (14 connections)
- **_stack()** (12 connections) — `server/tests/unit/services/test_container_service.py`
- **test_container_endpoints_loot_register.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **asyncio** (7 connections)
- **register_loot_endpoints()** (6 connections) — `server/api/container_endpoints_loot.py`
- **.test_loot_all_items_emit_event_failure()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_loot_all_items_player_not_found()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_loot_all_items_validation_error()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **.test_transfer_all_items_from_container_empty_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_item_without_quantity()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_multiple_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 108 more nodes in this community*

## Relationships

- [abstractcontextmanager](abstractcontextmanager.md) (64 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (41 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (9 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (8 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (3 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (3 shared connections)
- [characterinfo](characterinfo.md) (3 shared connections)
- [server api container helpers handle](server_api_container_helpers_handle.md) (2 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (1 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 359 (79%)
- INFERRED: 98 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*