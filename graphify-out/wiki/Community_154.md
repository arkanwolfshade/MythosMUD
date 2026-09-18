# Community 154

> 81 nodes

## Key Concepts

- **WebSocketMessageValidator** (51 connections) — `server/realtime/message_validator.py`
- **MessageValidationError** (43 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (30 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **message_validator.py** (11 connections) — `server/realtime/message_validator.py`
- **.parse_and_validate()** (8 connections) — `server/realtime/message_validator.py`
- **._unwrap_string_inner_message_if_json()** (7 connections) — `server/realtime/message_validator.py`
- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **._parse_outer_json_object()** (6 connections) — `server/realtime/message_validator.py`
- **._extract_csrf_token_string()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_csrf()** (5 connections) — `server/realtime/message_validator.py`
- **._validate_message_schema()** (5 connections) — `server/realtime/message_validator.py`
- **.validate_size()** (5 connections) — `server/realtime/message_validator.py`
- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **._validate_required_top_level_fields()** (4 connections) — `server/realtime/message_validator.py`
- **._validate_string_lengths()** (4 connections) — `server/realtime/message_validator.py`
- **test_parse_and_validate_csrf_inner_token_must_match_expected_not_outer_wrapper()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_oversized_raw_payload()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_accepts_depth_equal_to_limit()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_depth_exceeded()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_list_nesting_counts_toward_depth()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_size_counts_utf8_bytes()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_real_client_payload_validates()** (4 connections) — `server/tests/unit/realtime/test_websocket_message_schema_registry.py`
- **test_unknown_message_type_is_rejected()** (4 connections) — `server/tests/unit/realtime/test_websocket_message_schema_registry.py`
- **test_unrecognized_field_is_rejected()** (4 connections) — `server/tests/unit/realtime/test_websocket_message_schema_registry.py`
- *... and 56 more nodes in this community*

## Relationships

- [Realtime Message Handlers](Realtime_Message_Handlers.md) (9 shared connections)
- [Community 111](Community_111.md) (4 shared connections)
- [Community 243](Community_243.md) (4 shared connections)
- [Community 336](Community_336.md) (4 shared connections)
- [Community 272](Community_272.md) (3 shared connections)
- [Community 1093](Community_1093.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/tests/unit/realtime/test_message_validator.py`
- `server/tests/unit/realtime/test_websocket_message_schema_registry.py`

## Audit Trail

- EXTRACTED: 136 (75%)
- INFERRED: 45 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*