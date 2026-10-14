# inventory_item_matching.py

> 37 nodes

## Key Concepts

- **inventory_item_matching.py** (26 connections) — `server/commands/inventory_item_matching.py`
- **match_inventory_item_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **_earliest_whole_word()** (5 connections) — `server/commands/inventory_item_matching.py`
- **match_word_drop()** (5 connections) — `server/commands/inventory_item_matching.py`
- **build_drop_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_inventory_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **extract_item_identifier()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_exact_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_prefix_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_substring_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **search_word_match()** (4 connections) — `server/commands/inventory_item_matching.py`
- **search_exact_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_prefix_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_substring_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **test_match_inventory_item_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_inventory_item_by_name_no_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_inventory_item_by_name_prefix_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_inventory_item_by_name_substring_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **K** (1 connections)
- **Item matching utilities for inventory commands.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Build list of candidate tuples (index, item_name, item_id, prototype_id) from…** (1 connections) — `server/commands/inventory_item_matching.py`
- **Resolve an inventory index from a fuzzy name search. Human scholars: this…** (1 connections) — `server/commands/inventory_item_matching.py`
- **Build list of candidate tuples (index, item_name, item_id, prototype_id).** (1 connections) — `server/commands/inventory_item_matching.py`
- **Search for exact match. Returns slot_key if found, None otherwise.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Search for a whole-word (or phrase) match in the item name only. Returns…** (1 connections) — `server/commands/inventory_item_matching.py`
- *... and 12 more nodes in this community*

## Relationships

- [test_inventory_helpers.py](test_inventory_helpers.py.md) (12 shared connections)
- [match_equipped_item_by_name](match_equipped_item_by_name.md) (7 shared connections)
- [alias_storage.py](alias_storage.py.md) (6 shared connections)
- [test_inventory_commands_helpers.py](test_inventory_commands_helpers.py.md) (4 shared connections)
- [test_inventory_item_matching.py](test_inventory_item_matching.py.md) (3 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*