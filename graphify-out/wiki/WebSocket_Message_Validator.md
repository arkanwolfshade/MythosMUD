# WebSocket Message Validator

> 66 nodes · cohesion 0.06

## Key Concepts

- **WebSocketMessageValidator** (36 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (27 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **MessageValidationError** (26 connections) — `server/realtime/message_validator.py`
- **WebSocketMessageValidator** (25 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **.parse_and_validate()** (7 connections) — `server/realtime/message_validator.py`
- **._unwrap_string_inner_message_if_json()** (7 connections) — `server/realtime/message_validator.py`
- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **WebSocket** (7 connections) — `server/realtime/websocket_handler.py`
- **._parse_outer_json_object()** (6 connections) — `server/realtime/message_validator.py`
- **UUID** (6 connections) — `server/realtime/websocket_handler.py`
- **._extract_csrf_token_string()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_csrf()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_schema()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_size()** (5 connections) — `server/realtime/message_validator.py`
- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **._validate_string_lengths()** (4 connections) — `server/realtime/message_validator.py`
- **test_parse_and_validate_csrf_inner_token_must_match_expected_not_outer_wrapper()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_accepts_depth_equal_to_limit()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_list_nesting_counts_toward_depth()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_size_counts_utf8_bytes()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **._calculate_depth()** (3 connections) — `server/realtime/message_validator.py`
- **.__init__()** (3 connections) — `server/realtime/message_validator.py`
- **test_parse_and_validate_rejects_invalid_json()** (3 connections) — `server/tests/unit/realtime/test_message_validator.py`
- *... and 41 more nodes in this community*

## Relationships

- [[WebSocket Message Validation]] (12 shared connections)
- [[WebSocket Handler Helpers]] (7 shared connections)
- [[Pydantic Error Handlers]] (5 shared connections)
- [[Database Manager Tests]] (4 shared connections)
- [[WebSocket Coverage Gaps]] (4 shared connections)
- [[Realtime Websocket Handler]] (3 shared connections)
- [[WebSocket Message Handlers]] (3 shared connections)
- [[Help and WebSocket Core]] (2 shared connections)
- [[Room Occupant Events]] (2 shared connections)
- [[Realtime WebSocket Auth]] (2 shared connections)
- [[Combat Domain Events]] (1 shared connections)
- [[Combat Player Broadcasts]] (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_message_validator.py`

## Audit Trail

- EXTRACTED: 274 (93%)
- INFERRED: 21 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
