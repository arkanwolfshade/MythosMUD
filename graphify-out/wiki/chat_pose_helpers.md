# chat pose helpers

> 18 nodes

## Key Concepts

- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **build_equipped_candidates()** (5 connections) — `server/commands/inventory_item_matching.py`
- **extract_item_identifier()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_drop_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_exact_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_inventory_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **clean_item_value()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_exact_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_substring_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **Item matching utilities for inventory commands.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Extract and normalize item identifier from stack.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Build list of candidate tuples (index, item_name, item_id, prototype_id).** (1 connections) — `server/commands/inventory_item_matching.py`
- **Match by exact identifier (item_name, item_id, or prototype_id).** (1 connections) — `server/commands/inventory_item_matching.py`
- **Build list of candidate tuples (index, item_name, item_id, prototype_id) from in** (1 connections) — `server/commands/inventory_item_matching.py`
- **Clean item value for matching. Returns cleaned string or None.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Build list of candidates from equipped items. Returns list of (slot_key, item_na** (1 connections) — `server/commands/inventory_item_matching.py`
- **Search for exact match. Returns slot_key if found, None otherwise.** (1 connections) — `server/commands/inventory_item_matching.py`
- **Search for substring match. Returns slot_key if found, None otherwise.** (1 connections) — `server/commands/inventory_item_matching.py`

## Relationships

- [Test check grace period block](Test_check_grace_period_block.md) (5 shared connections)
- [Test process alias expansion function.](Test_process_alias_expansion_function.md) (5 shared connections)
- [test format metadata empty()](test_format_metadata_empty%28%29.md) (4 shared connections)
- [Any](Any.md) (2 shared connections)
- [Update player's connection list to](Update_player%27s_connection_list_to.md) (2 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (1 shared connections)
- [.add message()](add_message%28%29.md) (1 shared connections)
- [populate test npc databases](populate_test_npc_databases.md) (1 shared connections)

## Source Files

- `server/commands/inventory_item_matching.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*