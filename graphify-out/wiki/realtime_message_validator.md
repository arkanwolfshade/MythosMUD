# realtime message validator

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

- [auth invites rationale](auth_invites_rationale.md) (18 shared connections)
- [room look commands](room_look_commands.md) (4 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [persistence damage player()](persistence_damage_player%28%29.md) (2 shared connections)
- [logging utilities structured](logging_utilities_structured.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [test_process_message_validation_failed](test_process_message_validation_failed.md) (1 shared connections)
- [test_validate_message_failure](test_validate_message_failure.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/tests/unit/realtime/test_message_validator.py`

## Audit Trail

- EXTRACTED: 178 (86%)
- INFERRED: 30 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*