# Test process alias expansion function.

> 14 nodes

## Key Concepts

- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **match_prefix_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_substring_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **test_match_inventory_item_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_inventory_item_by_name_prefix_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_inventory_item_by_name_substring_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_inventory_item_by_name_no_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Match by prefix: first item_name, then item_id/prototype_id.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Match by substring containment in any identifier.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Resolve an inventory index from a fuzzy name search.      Human scholars: this m** (1 connections) — `server/commands/inventory_item_matching.py`
- **Test _match_inventory_item_by_name with exact match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_inventory_item_by_name with prefix match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test match_inventory_item_by_name with substring match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_inventory_item_by_name with no match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`

## Relationships

- [test format metadata empty()](test_format_metadata_empty%28%29.md) (7 shared connections)
- [chat pose helpers](chat_pose_helpers.md) (5 shared connections)
- [populate test npc databases](populate_test_npc_databases.md) (3 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (2 shared connections)

## Source Files

- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*