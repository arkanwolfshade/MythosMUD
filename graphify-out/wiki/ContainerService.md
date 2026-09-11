# ContainerService

> 75 nodes

## Key Concepts

- **ContainerService** (90 connections) — `server/services/container_service.py`
- **test_container_service.py** (72 connections) — `server/tests/unit/services/test_container_service.py`
- **asyncio** (27 connections)
- **_container_data()** (25 connections) — `server/tests/unit/services/test_container_service.py`
- **_stack()** (21 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (17 connections) — `server/services/inventory_mutation_guard.py`
- **_container()** (15 connections) — `server/tests/unit/services/test_container_service.py`
- **_open_from_fixture()** (11 connections) — `server/tests/unit/services/test_container_service.py`
- **_allow_all_mutations()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_capacity_exceeded()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_item_not_found()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_mutation_guard_suppressed()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_reraises_unexpected_error()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_success()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_stops_on_capacity_error()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_lock_container_updates_state()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_continues_past_other_errors()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_success()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_capacity_exceeded()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_non_dict_container_data()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 50 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (31 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (25 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (10 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [GameBundle](GameBundle.md) (3 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 214 (72%)
- INFERRED: 85 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*