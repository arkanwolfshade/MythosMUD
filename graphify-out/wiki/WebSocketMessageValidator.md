# WebSocketMessageValidator

> 67 nodes

## Key Concepts

- **WebSocketMessageValidator** (44 connections) — `server/realtime/message_validator.py`
- **MessageValidationError** (39 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (31 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **message_validator.py** (10 connections) — `server/realtime/message_validator.py`
- **.parse_and_validate()** (7 connections) — `server/realtime/message_validator.py`
- **._unwrap_string_inner_message_if_json()** (7 connections) — `server/realtime/message_validator.py`
- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **._parse_outer_json_object()** (6 connections) — `server/realtime/message_validator.py`
- **._extract_csrf_token_string()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_csrf()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_schema()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_size()** (5 connections) — `server/realtime/message_validator.py`
- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **._validate_string_lengths()** (4 connections) — `server/realtime/message_validator.py`
- **test_parse_and_validate_csrf_inner_token_must_match_expected_not_outer_wrapper()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_oversized_raw_payload()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_accepts_depth_equal_to_limit()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_depth_exceeded()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_list_nesting_counts_toward_depth()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_size_counts_utf8_bytes()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **._calculate_depth()** (3 connections) — `server/realtime/message_validator.py`
- **.__init__()** (3 connections) — `server/realtime/message_validator.py`
- **test_extract_csrf_invalid_type_rejected()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_invalid_json()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- *... and 42 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (7 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [test_websocket_handler_validation.py](test_websocket_handler_validation.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/tests/unit/realtime/test_message_validator.py`

## Audit Trail

- EXTRACTED: 117 (75%)
- INFERRED: 39 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*