# Community 144

> 83 nodes

## Key Concepts

- **LootAllRequest** (59 connections) — `server/api/container_models.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (31 connections) — `server/api/container_endpoints_loot.py`
- **test_container_helpers_loot.py** (22 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **asyncio** (14 connections)
- **TestGetContainerAndPlayerForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **apply_rate_limiting_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_transfer_all_items_from_container_capacity_error()** (7 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **asyncio** (7 connections)
- **_build_loot_all_response()** (6 connections) — `server/api/container_endpoints_loot.py`
- **register_loot_endpoints()** (6 connections) — `server/api/container_endpoints_loot.py`
- **.test_loot_all_items_emit_event_failure()** (6 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **.test_transfer_all_items_from_container_empty_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_item_without_quantity()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_multiple_items()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_partial_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_container()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_result_missing_inventory()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_transfer_all_items_from_container_success()** (6 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- *... and 58 more nodes in this community*

## Relationships

- [User Manager & Character Info](User_Manager_&_Character_Info.md) (28 shared connections)
- [Community 31](Community_31.md) (28 shared connections)
- [Community 67](Community_67.md) (18 shared connections)
- [Community 64](Community_64.md) (17 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (14 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (9 shared connections)
- [Community 84](Community_84.md) (8 shared connections)
- [Community 43](Community_43.md) (3 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (2 shared connections)
- [Community 1143](Community_1143.md) (2 shared connections)
- [Community 691](Community_691.md) (2 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 279 (93%)
- INFERRED: 22 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*