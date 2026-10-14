# test_inventory_item_matching.py

> 23 nodes

## Key Concepts

- **test_inventory_item_matching.py** (21 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **_stack()** (16 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **ALL_FAMILIES** (12 connections)
- **_equipped()** (4 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_a_term_inside_an_id_is_not_a_whole_word_of_another_item()** (4 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_ids_are_not_word_matched_ahead_of_name_prefixes()** (4 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_ids_are_the_substring_fallback()** (4 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **_inventory()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **_room()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_a_whole_word_beats_a_longer_word_that_starts_with_it()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_an_abbreviation_falls_through_to_prefix()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_an_exact_id_still_beats_a_whole_word()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_an_exact_name_still_beats_a_whole_word()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_equal_word_positions_keep_list_order()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_multi_word_terms_match_as_a_phrase()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_no_match_and_blank_terms()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_regex_metacharacters_in_the_term_are_literal()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **test_the_earliest_word_position_wins_among_whole_words()** (3 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **Tests for item-name matching order: exact -> whole word (name) -> prefix ->…** (1 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **No name has the word, but an id contains it: still found, as before.** (1 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **`weapon` is a whole word of the first item's id only; the second item's name…** (1 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **Equipped items resolve to a slot key; slots here are numbered so results…** (1 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`
- **The codex's id `artifact.miskatonic.codex` contains "tonic", but its name does…** (1 connections) — `server/tests/unit/commands/test_inventory_item_matching.py`

## Relationships

- [inventory_item_matching.py](inventory_item_matching.py.md) (3 shared connections)
- [match_equipped_item_by_name](match_equipped_item_by_name.md) (2 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (2 shared connections)

## Source Files

- `server/tests/unit/commands/test_inventory_item_matching.py`

## Audit Trail

- EXTRACTED: 52 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*