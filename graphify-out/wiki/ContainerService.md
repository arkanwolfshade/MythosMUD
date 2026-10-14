# ContainerService

> 44 nodes

## Key Concepts

- **ContainerService** (98 connections) — `server/services/container_service.py`
- **test_container_service.py** (80 connections) — `server/tests/unit/services/test_container_service.py`
- **_container()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_bank_box()** (10 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_ownership_orphaned_bank_box_matches_nobody()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_can_unlock_container_admin()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_can_unlock_container_locked_without_key()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_can_unlock_container_with_key()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_remove_item_from_container_partial_quantity()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_container_access_bank_owner_opens_it_anywhere()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_container_access_success()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_corpse_grace_period_blocks_non_owner()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_corpse_grace_period_expired_allows_other_player()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_ownership_equipment_match()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_ownership_equipment_mismatch_raises()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_proximity_different_room_raises()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_proximity_same_room_passes()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **UUID** (4 connections)
- **service()** (3 connections) — `server/tests/unit/services/test_container_service.py`
- **test_close_container_audit_failure_still_closes()** (3 connections) — `server/tests/unit/services/test_container_service.py`
- **test_close_container_success()** (3 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_not_found()** (3 connections) — `server/tests/unit/services/test_container_service.py`
- **test_prepare_transfer_item_reduces_quantity()** (3 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_container_access_bank_is_closed_to_other_players_and_admins()** (3 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_ownership_bank_other_player_raises()** (3 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (63 shared connections)
- [ContainerComponent](ContainerComponent.md) (29 shared connections)
- [LootAllRequest](LootAllRequest.md) (13 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (9 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [MutationDecision](MutationDecision.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [InventoryService](InventoryService.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [TestGetContainerService](TestGetContainerService.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 141 (63%)
- INFERRED: 82 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*