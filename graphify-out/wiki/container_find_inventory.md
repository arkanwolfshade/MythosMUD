# container find inventory

> 53 nodes

## Key Concepts

- **test_container_helpers_inventory_find.py** (55 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **find_wearable_container()** (17 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_container_in_room()** (13 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_item_in_inventory()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_inner_container()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **_player_for_wearable()** (12 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **try_inner_container_by_id()** (11 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_matching_equipped_containers()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **check_item_matches_target()** (7 connections) — `server/commands/container_helpers_inventory_find.py`
- **test_find_item_in_inventory_non_numeric_token_name_search()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_check_item_matches_target_partial_name()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_create_wearable_container_uses_equip_dict_branch()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_create_wearable_container_fallback_when_equip_returns_non_dict()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_for_put_hits_inner_container()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_for_put_creates_on_slot_only_match()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_no_match_returns_none()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_inner_id_short_circuits()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_resolves_via_wearable_instance_id()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_falls_back_to_name_slot_match()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_wearable_raises_returns_none()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_by_index()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_by_name_substring()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_miss()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_index_zero_invalid()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_uppercase_query()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- *... and 28 more nodes in this community*

## Relationships

- [logout command commands](logout_command_commands.md) (38 shared connections)
- [services admin auth](services_admin_auth.md) (8 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (2 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (1 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_find.py`
- `server/tests/unit/commands/test_container_helpers_inventory_find.py`

## Audit Trail

- EXTRACTED: 233 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*