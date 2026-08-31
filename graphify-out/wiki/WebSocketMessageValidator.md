# WebSocketMessageValidator

> 45 nodes

## Key Concepts

- **WebSocketMessageValidator** (44 connections) — `server/realtime/message_validator.py`
- **MessageValidationError** (39 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (31 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **message_validator.py** (10 connections) — `server/realtime/message_validator.py`
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_csrf_inner_token_must_match_expected_not_outer_wrapper()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_oversized_raw_payload()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_accepts_depth_equal_to_limit()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_depth_exceeded()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_list_nesting_counts_toward_depth()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_size_counts_utf8_bytes()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_extract_csrf_invalid_type_rejected()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_invalid_json()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_non_object_json()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_unwraps_without_csrf_rejected()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_csrf_both_none_rejected()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_csrf_mismatch()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_csrf_missing_when_expected()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_csrf_present_without_expected_token_rejected()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_key_length_exceeded()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_string_length_exceeded()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_size_exceeds_limit()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **validator()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- *... and 20 more nodes in this community*

## Relationships

- [.parse_and_validate](parse_and_validate.md) (18 shared connections)
- [ErrorType](ErrorType.md) (7 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [test_websocket_handler_validation.py](test_websocket_handler_validation.py.md) (2 shared connections)
- [.__init__](__init__.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/tests/unit/realtime/test_message_validator.py`

## Audit Trail

- EXTRACTED: 94 (71%)
- INFERRED: 39 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*