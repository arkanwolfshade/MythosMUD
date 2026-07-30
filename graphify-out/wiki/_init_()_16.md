# . init ()

> 42 nodes

## Key Concepts

- **WebSocketMessageValidator** (42 connections) — `server/realtime/message_validator.py`
- **MessageValidationError** (36 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (28 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **message_validator.py** (9 connections) — `server/realtime/message_validator.py`
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_size_counts_utf8_bytes()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_depth_exceeded()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_accepts_depth_equal_to_limit()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_list_nesting_counts_toward_depth()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_oversized_raw_payload()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_csrf_inner_token_must_match_expected_not_outer_wrapper()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_size_exceeds_limit()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_string_length_exceeded()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_key_length_exceeded()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_extract_csrf_invalid_type_rejected()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_csrf_missing_when_expected()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_csrf_mismatch()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_csrf_present_without_expected_token_rejected()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_invalid_json()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_non_object_json()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **validator()** (2 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_size_within_limit()** (2 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_csrf_matches_expected()** (2 connections) — `server/tests/unit/realtime/test_message_validator.py`
- *... and 17 more nodes in this community*

## Relationships

- [nudgeStandBothPlayers()](nudgeStandBothPlayers%28%29.md) (18 shared connections)
- [.is required()](is_required%28%29.md) (4 shared connections)
- [websocket handler commands](websocket_handler_commands.md) (4 shared connections)
- [convert pydantic error()](convert_pydantic_error%28%29.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [local channel isolation.spec](local_channel_isolation.spec.md) (2 shared connections)
- [quest events](quest_events.md) (2 shared connections)
- [test websocket handler helpers extended](test_websocket_handler_helpers_extended.md) (1 shared connections)
- [test_parse_command_parts_empty_string](test_parse_command_parts_empty_string.md) (1 shared connections)
- [test_command_parser_initialization](test_command_parser_initialization.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/tests/unit/realtime/test_message_validator.py`

## Audit Trail

- EXTRACTED: 178 (86%)
- INFERRED: 30 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*