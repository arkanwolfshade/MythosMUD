# Server Realtime (25)

> 66 nodes

## Key Concepts

- **WebSocketMessageValidator** (40 connections) — `server/realtime/message_validator.py`
- **MessageValidationError** (35 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (28 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **message_validator.py** (7 connections) — `server/realtime/message_validator.py`
- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **._unwrap_string_inner_message_if_json()** (7 connections) — `server/realtime/message_validator.py`
- **.parse_and_validate()** (7 connections) — `server/realtime/message_validator.py`
- **._parse_outer_json_object()** (6 connections) — `server/realtime/message_validator.py`
- **.validate_size()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_schema()** (5 connections) — `server/realtime/message_validator.py`
- **._extract_csrf_token_string()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_csrf()** (5 connections) — `server/realtime/message_validator.py`
- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **._validate_string_lengths()** (4 connections) — `server/realtime/message_validator.py`
- **test_validate_size_counts_utf8_bytes()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_depth_exceeded()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_accepts_depth_equal_to_limit()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_list_nesting_counts_toward_depth()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_oversized_raw_payload()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_csrf_inner_token_must_match_expected_not_outer_wrapper()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **.__init__()** (3 connections) — `server/realtime/message_validator.py`
- **._calculate_depth()** (3 connections) — `server/realtime/message_validator.py`
- **get_message_validator()** (3 connections) — `server/realtime/message_validator.py`
- **test_validate_size_exceeds_limit()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- *... and 41 more nodes in this community*

## Relationships

- [Server Realtime (29)](Server_Realtime_%2829%29.md) (4 shared connections)
- [Server Realtime (33)](Server_Realtime_%2833%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Realtime (107)](Server_Realtime_%28107%29.md) (2 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/tests/unit/realtime/test_message_validator.py`

## Audit Trail

- EXTRACTED: 243 (89%)
- INFERRED: 30 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*