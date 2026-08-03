# container find inventory

> 41 nodes

## Key Concepts

- **test_container_helpers_inventory_find.py** (55 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **find_container_in_room()** (13 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_item_in_inventory()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_inner_container()** (12 connections) — `server/commands/container_helpers_inventory_find.py`
- **try_inner_container_by_id()** (11 connections) — `server/commands/container_helpers_inventory_find.py`
- **find_matching_equipped_containers()** (9 connections) — `server/commands/container_helpers_inventory_find.py`
- **check_item_matches_target()** (7 connections) — `server/commands/container_helpers_inventory_find.py`
- **test_find_item_in_inventory_non_numeric_token_name_search()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_check_item_matches_target_partial_name()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_by_index()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_by_name_substring()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_miss()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_index_zero_invalid()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_item_in_inventory_uppercase_query()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_check_item_matches_target()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_matching_equipped_containers_by_name()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_matching_equipped_containers_inner_without_name_match()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_try_inner_container_by_id_none()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_try_inner_container_by_id_resolves()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_container_in_room_with_metadata_name()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_container_in_room_no_match()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_container_in_room_non_dict_entries_skipped()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_container_in_room_get_containers_not_callable()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_container_in_room_non_list_returns_empty()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_check_item_matches_target_name_miss_slot_exact()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- *... and 16 more nodes in this community*

## Relationships

- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (26 shared connections)
- [combat npc services](combat_npc_services.md) (14 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (7 shared connections)
- [inventory commands command](inventory_commands_command.md) (2 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_find.py`
- `server/tests/unit/commands/test_container_helpers_inventory_find.py`

## Audit Trail

- EXTRACTED: 177 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*