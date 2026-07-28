# Command Field Validators

> 118 nodes · cohesion 0.02

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **alias_expansion.py** (16 connections) — `server/command_handler/alias_expansion.py`
- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **.is_valid_command_name()** (4 connections) — `server/validators/command_validator.py`
- **test_clean_command_input_basic()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_unicode()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_whitespace()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_with_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_admin()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_case_insensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 93 more nodes in this community*

## Relationships

- [Combat Taunt Tests](Combat_Taunt_Tests.md) (11 shared connections)
- [Command Request App State](Command_Request_App_State.md) (7 shared connections)
- [Realtime Message Formatters](Realtime_Message_Formatters.md) (7 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (2 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (2 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (2 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (2 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 373 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*