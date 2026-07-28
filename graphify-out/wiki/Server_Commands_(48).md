# Server Commands (48)

> 24 nodes

## Key Concepts

- **inventory_item_matching.py** (21 connections) — `server/commands/inventory_item_matching.py`
- **build_equipped_candidates()** (5 connections) — `server/commands/inventory_item_matching.py`
- **extract_item_identifier()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_drop_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_exact_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_prefix_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_substring_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_inventory_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **clean_item_value()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_exact_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_prefix_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_substring_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **Item matching utilities for inventory commands.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Extract and normalize item identifier from stack.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Build list of candidate tuples (index, item_name, item_id, prototype_id).** (1 connections) — `server/commands/inventory_item_matching.py`
- **Match by exact identifier (item_name, item_id, or prototype_id).** (1 connections) — `server/commands/inventory_item_matching.py`
- **Match by prefix: first item_name, then item_id/prototype_id.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Match by substring containment in any identifier.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Build list of candidate tuples (index, item_name, item_id, prototype_id) from in** (1 connections) — `server/commands/inventory_item_matching.py`
- **Clean item value for matching. Returns cleaned string or None.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Build list of candidates from equipped items. Returns list of (slot_key, item_na** (1 connections) — `server/commands/inventory_item_matching.py`
- **Search for exact match. Returns slot_key if found, None otherwise.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Search for prefix match. Returns slot_key if found, None otherwise.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Search for substring match. Returns slot_key if found, None otherwise.** (1 connections) — `server/commands/inventory_item_matching.py`

## Relationships

- [Server Commands (49)](Server_Commands_%2849%29.md) (6 shared connections)
- [Server Commands (60)](Server_Commands_%2860%29.md) (6 shared connections)
- [Server Commands (58)](Server_Commands_%2858%29.md) (5 shared connections)
- [Server Commands (2)](Server_Commands_%282%29.md) (2 shared connections)
- [Server Commands (67)](Server_Commands_%2867%29.md) (2 shared connections)
- [Server Commands (71)](Server_Commands_%2871%29.md) (1 shared connections)

## Source Files

- `server/commands/inventory_item_matching.py`

## Audit Trail

- EXTRACTED: 74 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*