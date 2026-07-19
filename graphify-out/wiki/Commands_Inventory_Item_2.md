# Commands Inventory Item

> 19 nodes · cohesion 0.11

## Key Concepts

- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **search_exact_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_prefix_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_substring_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **test_match_equipped_item_by_name_empty_search()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_item_id_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_no_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_prefix_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_equipped_item_by_name_substring_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_equipped_item_by_name with exact match.** (2 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Search for exact match. Returns slot_key if found, None otherwise.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Search for prefix match. Returns slot_key if found, None otherwise.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Search for substring match. Returns slot_key if found, None otherwise.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Resolve an equipped slot identifier via fuzzy item name search.      Scholars: w** (1 connections) — `server/commands/inventory_item_matching.py`
- **Test _match_equipped_item_by_name with prefix match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_equipped_item_by_name with substring match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_equipped_item_by_name with item_id match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_equipped_item_by_name with empty search term.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`

## Relationships

- [[Admin Summon Command]] (7 shared connections)
- [[Commands Inventory Item]] (7 shared connections)
- [[Commands Inventory]] (3 shared connections)

## Source Files

- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 55 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
