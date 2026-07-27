# Commands Inventory Item

> 21 nodes · cohesion 0.11

## Key Concepts

- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **match_exact_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_prefix_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_substring_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **test_match_room_drop_by_name_exact()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **Test _match_room_drop_by_name with exact match.** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_room_drop_by_name_empty_search()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_room_drop_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_room_drop_by_name_item_id_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_room_drop_by_name_no_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_room_drop_by_name_prefix_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_room_drop_by_name_prototype_id_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_match_room_drop_by_name_substring_match()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_room_drop_by_name with prefix match.** (2 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Match by exact identifier (item_name, item_id, or prototype_id).** (1 connections) — `server/commands/inventory_item_matching.py`
- **Match by prefix: first item_name, then item_id/prototype_id.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Match by substring containment in any identifier.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Resolve a room drop index using Lovecraftian-grade fuzzy matching heuristics.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Test _match_room_drop_by_name with empty search term.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_room_drop_by_name with substring match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test _match_room_drop_by_name with item_id match.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`

## Relationships

- [[Commands Inventory Item]] (12 shared connections)
- [[Admin Summon Command]] (6 shared connections)
- [[Commands Inventory]] (3 shared connections)

## Source Files

- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
