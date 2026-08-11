# Database Helper Tests

> 22 nodes

## Key Concepts

- **WebSocketMessageValidator** (42 connections) — `server/realtime/message_validator.py`
- **test_message_validator.py** (28 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_rejects_oversized_raw_payload()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
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
- **test_validate_csrf_snake_case_key()** (2 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_strips_csrf_after_success()** (2 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_inherits_outer_csrf()** (2 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_unwraps_string_inner_message()** (2 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **Validates WebSocket messages for security and correctness.      Implements:** (1 connections) — `server/realtime/message_validator.py`
- **Unit tests for WebSocketMessageValidator (size, JSON depth, string length, CSRF)** (1 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **parse_and_validate applies byte size limit to the full wire payload.** (1 connections) — `server/tests/unit/realtime/test_message_validator.py`

## Relationships

- [Scenario Conversion Guide](Scenario_Conversion_Guide.md) (17 shared connections)
- [Security Issues And Fixes](Security_Issues_And_Fixes.md) (7 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (7 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (3 shared connections)
- [Cursor Plans Best](Cursor_Plans_Best.md) (3 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (3 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)
- [test_profession_get_mechanical_effects_none](test_profession_get_mechanical_effects_none.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/tests/unit/realtime/test_message_validator.py`

## Audit Trail

- EXTRACTED: 108 (92%)
- INFERRED: 10 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*