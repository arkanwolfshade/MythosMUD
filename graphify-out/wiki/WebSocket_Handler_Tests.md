# WebSocket Handler Tests

> 32 nodes

## Key Concepts

- **test_optimized_security_validator.py** (78 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **optimized_validate_message_content()** (19 connections) — `server/validators/optimized_security_validator.py`
- **test_optimized_validate_message_content_empty()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_valid()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_dangerous_chars()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_injection_pattern()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_sql_injection()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_xss()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_path_traversal()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_javascript_url()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_event_handler()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_data_url()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_python_injection()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_format_string()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_logging()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_message_content_logging_warning()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Unit tests for optimized security validation utilities.  Tests the optimized sec** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating empty message.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating valid message.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating message with dangerous characters.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating message with injection pattern.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating message with SQL injection pattern.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating message with XSS pattern.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating message with path traversal pattern.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating message with javascript: URL.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- *... and 7 more nodes in this community*

## Relationships

- [Cursor Workflows Docs](Cursor_Workflows_Docs.md) (9 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (9 shared connections)
- [Async Anti-Pattern Guide](Async_Anti-Pattern_Guide.md) (8 shared connections)
- [Services Combat Initialization](Services_Combat_Initialization.md) (5 shared connections)
- [Persistence Player Effect](Persistence_Player_Effect.md) (5 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (5 shared connections)
- [Command Factories Inventory](Command_Factories_Inventory.md) (4 shared connections)
- [Cursor Plans Uvicorn](Cursor_Plans_Uvicorn.md) (4 shared connections)
- [Realtime Player Event](Realtime_Player_Event.md) (4 shared connections)
- [Game Instance Manager](Game_Instance_Manager.md) (4 shared connections)
- [E 2 E Whisper System](E_2_E_Whisper_System.md) (4 shared connections)
- [Realtime Schemas Presence](Realtime_Schemas_Presence.md) (4 shared connections)

## Source Files

- `server/tests/unit/validators/test_optimized_security_validator.py`
- `server/validators/optimized_security_validator.py`

## Audit Trail

- EXTRACTED: 155 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*