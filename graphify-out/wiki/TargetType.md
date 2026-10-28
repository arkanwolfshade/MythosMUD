# TargetType

> 126 nodes · cohesion 0.03

## Key Concepts

- **test_inventory_helpers.py** (38 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **inventory_item_matching.py** (26 connections) — `server/commands/inventory_item_matching.py`
- **match_room_drop_by_name()** (22 connections) — `server/commands/inventory_item_matching.py`
- **match_equipped_item_by_name()** (21 connections) — `server/commands/inventory_item_matching.py`
- **test_inventory_item_matching.py** (21 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **match_inventory_item_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **_stack()** (16 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **ALL_FAMILIES** (12 connections)
- **build_equipped_candidates()** (5 connections) — `server/commands/inventory_item_matching.py`
- **_earliest_whole_word()** (5 connections) — `server/commands/inventory_item_matching.py`
- **match_word_drop()** (5 connections) — `server/commands/inventory_item_matching.py`
- **build_drop_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_inventory_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **extract_item_identifier()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_exact_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_prefix_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_substring_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **search_word_match()** (4 connections) — `server/commands/inventory_item_matching.py`
- **_equipped()** (4 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_a_term_inside_an_id_is_not_a_whole_word_of_another_item()** (4 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_ids_are_not_word_matched_ahead_of_name_prefixes()** (4 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_ids_are_the_substring_fallback()** (4 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **clean_item_value()** (3 connections) — `server/commands/inventory_item_matching.py`
- *... and 101 more nodes in this community*

## Relationships

- [test_command_alias.py](test_command_alias.py.md) (9 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (8 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (6 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)

## Source Files

- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers.py`
- `server/tests/unit/commands/test_inventory_item_matching.py`

## Audit Trail

- EXTRACTED: 243 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*