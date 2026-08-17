# server realtime message validator

> 146 nodes

## Key Concepts

- **WebSocketMessageValidator** (42 connections) — `server/realtime/message_validator.py`
- **test_websocket_handler_validation_errors.py** (40 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **MessageValidationError** (37 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (29 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **asyncio** (25 connections)
- **websocket_handler_validation.py** (22 connections) — `server/realtime/websocket_handler_validation.py`
- **message_validator.py** (10 connections) — `server/realtime/message_validator.py`
- **.parse_and_validate()** (7 connections) — `server/realtime/message_validator.py`
- **._unwrap_string_inner_message_if_json()** (7 connections) — `server/realtime/message_validator.py`
- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **validate_websocket_message()** (7 connections) — `server/realtime/websocket_handler_validation.py`
- **._parse_outer_json_object()** (6 connections) — `server/realtime/message_validator.py`
- **resolve_expected_csrf_token()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **._extract_csrf_token_string()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_csrf()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_schema()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_size()** (5 connections) — `server/realtime/message_validator.py`
- **check_websocket_message_rate_limit()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_message_csrf_and_restore_metadata()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_message_validation_error()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **._validate_string_lengths()** (4 connections) — `server/realtime/message_validator.py`
- **get_connection_csrf_context()** (4 connections) — `server/realtime/websocket_handler_validation.py`
- *... and 121 more nodes in this community*

## Relationships

- [server realtime envelope build event](server_realtime_envelope_build_event.md) (13 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (12 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server error types errormessages](server_error_types_errormessages.md) (4 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [playercombatservice](playercombatservice.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/realtime/test_message_validator.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 243 (81%)
- INFERRED: 57 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*