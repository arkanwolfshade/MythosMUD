# get_help_content

> 31 nodes

## Key Concepts

- **get_help_content()** (40 connections) — `server/help/help_content.py`
- **test_bank_wiring.py** (19 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- **test_websocket_handler_help.py** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **_doc()** (4 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- **test_detailed_help_exists_and_says_you_must_be_at_a_bank()** (4 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- **test_a_bank_verb_is_never_mistaken_for_an_emote()** (3 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- **test_use_has_help_text_naming_its_aliases()** (3 connections) — `server/tests/unit/models/test_command_use.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_general()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_get_help_content_specific()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_get_help_content_talk()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **test_help_explains_both_new_combat_verbs()** (2 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **test_general_help_lists_each_bank_verb()** (2 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- **test_plain_help_describes_each_bank_verb()** (2 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- **test_the_bank_verbs_appear_under_the_inventory_help_category()** (2 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- **test_help_explains_protect()** (2 connections) — `server/tests/unit/commands/test_protect_wiring.py`
- **test_a_near_miss_gets_suggestions()** (2 connections) — `server/tests/unit/help/test_help_docs.py`
- **test_a_topic_is_matched_without_regard_to_case_or_a_leading_slash()** (2 connections) — `server/tests/unit/help/test_help_docs.py`
- **test_the_index_lists_commands_by_category_and_points_at_the_manual()** (2 connections) — `server/tests/unit/help/test_help_docs.py`
- **test_the_topic_is_escaped_in_the_not_found_notice()** (2 connections) — `server/tests/unit/help/test_help_docs.py`
- **parametrize** (2 connections)
- **test_the_bank_verbs_are_registered_with_the_command_service()** (1 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- **Render help as allowlisted HTML. Args: topic: Command name, command alias, or…** (1 connections) — `server/help/help_content.py`
- **Tests that `bank`, `deposit` and `withdraw` are reachable end to end: route,…** (1 connections) — `server/tests/unit/commands/test_bank_wiring.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_help_docs.py](test_help_docs.py.md) (14 shared connections)
- [help_content.py](help_content.py.md) (9 shared connections)
- [command_parser.py](command_parser.py.md) (4 shared connections)
- [BaseCommand](BaseCommand.md) (3 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [system_commands.py](system_commands.py.md) (2 shared connections)
- [command_result_text](command_result_text.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (2 shared connections)
- [_AllowlistChecker](_AllowlistChecker.md) (1 shared connections)
- [arkham_grid_spec.py](arkham_grid_spec.py.md) (1 shared connections)

## Source Files

- `server/help/help_content.py`
- `server/tests/unit/commands/test_assist_wiring.py`
- `server/tests/unit/commands/test_bank_wiring.py`
- `server/tests/unit/commands/test_protect_wiring.py`
- `server/tests/unit/help/test_help_docs.py`
- `server/tests/unit/models/test_command_use.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 80 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*