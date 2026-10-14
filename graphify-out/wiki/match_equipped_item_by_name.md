# match_equipped_item_by_name

> 18 nodes

## Key Concepts

- **match_equipped_item_by_name()** (21 connections) — `server/commands/inventory_item_matching.py`
- **build_equipped_candidates()** (5 connections) — `server/commands/inventory_item_matching.py`
- **clean_item_value()** (3 connections) — `server/commands/inventory_item_matching.py`
- **test_match_equipped_item_by_name_empty_search()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_item_id_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_no_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_prefix_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_substring_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Clean item value for matching. Returns cleaned string or None.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Build list of candidates from equipped items. Returns list of (slot_key,…** (1 connections) — `server/commands/inventory_item_matching.py`
- **Resolve an equipped slot identifier via fuzzy item name search. Scholars: we…** (1 connections) — `server/commands/inventory_item_matching.py`
- **Test _match_equipped_item_by_name with exact match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_equipped_item_by_name with prefix match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_equipped_item_by_name with substring match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_equipped_item_by_name with item_id match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_equipped_item_by_name with no match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_equipped_item_by_name with empty search term.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`

## Relationships

- [inventory_item_matching.py](inventory_item_matching.py.md) (7 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (7 shared connections)
- [alias_storage.py](alias_storage.py.md) (3 shared connections)
- [test_inventory_commands_helpers.py](test_inventory_commands_helpers.py.md) (3 shared connections)
- [test_inventory_item_matching.py](test_inventory_item_matching.py.md) (2 shared connections)

## Source Files

- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*