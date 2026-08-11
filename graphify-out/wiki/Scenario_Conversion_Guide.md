# Scenario Conversion Guide

> 15 nodes

## Key Concepts

- **MessageValidationError** (36 connections) — `server/realtime/message_validator.py`
- **test_validate_size_counts_utf8_bytes()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_list_nesting_counts_toward_depth()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_csrf_inner_token_must_match_expected_not_outer_wrapper()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_message_failure()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_process_message_validation_failed()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **test_validate_message_validation_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **Exception** (1 connections)
- **Raised when message validation fails.** (1 connections) — `server/realtime/message_validator.py`
- **Size limit uses UTF-8 byte length, not Python len(str).** (1 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **Lists contribute to nesting depth the same way as objects.** (1 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **If inner JSON carries its own csrfToken, it is validated (outer wrapper token is** (1 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **Test _validate_message() returns None when validation fails.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **Test _process_message() continues when validation fails.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- **Test _validate_message returns None and sends error when validation fails.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Relationships

- [Database Helper Tests](Database_Helper_Tests.md) (17 shared connections)
- [Security Issues And Fixes](Security_Issues_And_Fixes.md) (6 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (3 shared connections)
- [Combat Feature Flags](Combat_Feature_Flags.md) (3 shared connections)
- [Cursor Plans Best](Cursor_Plans_Best.md) (2 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (2 shared connections)
- [Game Instance Manager](Game_Instance_Manager.md) (2 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (1 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/tests/unit/realtime/test_message_validator.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers_extended.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 47 (72%)
- INFERRED: 18 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*