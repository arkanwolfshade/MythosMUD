# useAsciiMapState.ts

> 98 nodes · cohesion 0.04

## Key Concepts

- **WebSocketMessageValidator** (51 connections) — `server/realtime/message_validator.py`
- **MessageValidationError** (43 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (30 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **websocket_handler_validation.py** (22 connections) — `server/realtime/websocket_handler_validation.py`
- **message_validator.py** (11 connections) — `server/realtime/message_validator.py`
- **.parse_and_validate()** (8 connections) — `server/realtime/message_validator.py`
- **._unwrap_string_inner_message_if_json()** (7 connections) — `server/realtime/message_validator.py`
- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **validate_websocket_message()** (7 connections) — `server/realtime/websocket_handler_validation.py`
- **._parse_outer_json_object()** (6 connections) — `server/realtime/message_validator.py`
- **resolve_expected_csrf_token()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **._extract_csrf_token_string()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_csrf()** (5 connections) — `server/realtime/message_validator.py`
- **._validate_message_schema()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_size()** (5 connections) — `server/realtime/message_validator.py`
- **check_websocket_message_rate_limit()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_message_csrf_and_restore_metadata()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **._validate_required_top_level_fields()** (4 connections) — `server/realtime/message_validator.py`
- **._validate_string_lengths()** (4 connections) — `server/realtime/message_validator.py`
- **get_connection_csrf_context()** (4 connections) — `server/realtime/websocket_handler_validation.py`
- **WebSocket** (4 connections)
- **test_parse_and_validate_csrf_inner_token_must_match_expected_not_outer_wrapper()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_oversized_raw_payload()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- *... and 73 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (10 shared connections)
- [EventBus](EventBus.md) (9 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (7 shared connections)
- [Room](Room.md) (4 shared connections)
- [Alias](Alias.md) (4 shared connections)
- [Distill Skill](Distill_Skill.md) (2 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/realtime/test_message_validator.py`
- `server/tests/unit/realtime/test_websocket_message_schema_registry.py`

## Audit Trail

- EXTRACTED: 173 (79%)
- INFERRED: 47 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*