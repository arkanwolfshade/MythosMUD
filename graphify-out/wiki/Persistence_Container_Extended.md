# Persistence Container Extended

> 141 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **_run_command_service_for_validated()** (6 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (6 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (6 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (6 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **_handle_validation_error()** (5 connections) — `server/command_handler/processing.py`
- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **.is_valid_command_name()** (4 connections) — `server/validators/command_validator.py`
- *... and 116 more nodes in this community*

## Relationships

- [Chat Panel Components](Chat_Panel_Components.md) (10 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (9 shared connections)
- [Container Open Events](Container_Open_Events.md) (8 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (8 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (6 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (2 shared connections)
- [Config Model Tests](Config_Model_Tests.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (1 shared connections)
- [Audit Logger Service](Audit_Logger_Service.md) (1 shared connections)
- [Environmental Container Scenario](Environmental_Container_Scenario.md) (1 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 467 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*