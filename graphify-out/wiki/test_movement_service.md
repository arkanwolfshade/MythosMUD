# test movement service

> 33 nodes

## Key Concepts

- **alias_expansion.py** (16 connections) — `server/command_handler/alias_expansion.py`
- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **handle_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **_run_command_service_for_validated()** (6 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (6 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (6 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (6 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **_handle_validation_error()** (5 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (3 connections) — `server/command_handler/processing.py`
- **test_command_validator_is_security_sensitive_admin()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_case_insensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_non_sensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Any** (2 connections)
- **CommandExecutionRequest** (2 connections)
- **ValidationError** (2 connections)
- **Exception** (2 connections)
- **Alias Expansion Logic for MythosMUD.  This module handles alias resolution, expa** (1 connections) — `server/command_handler/alias_expansion.py`
- **Handle command processing with alias expansion and loop detection.      This fun** (1 connections) — `server/command_handler/alias_expansion.py`
- **Validate the raw command string via CommandProcessor.      Returns:         (** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- **Parse the command line; on success run CommandService (see ``_parse_command_line** (1 connections) — `server/command_handler/processing.py`
- **Validate ``command_line`` via Click/Pydantic, dispatch to handlers; result dict** (1 connections) — `server/command_handler/processing.py`
- *... and 8 more nodes in this community*

## Relationships

- [CommandExecutionRequest](CommandExecutionRequest.md) (8 shared connections)
- [Player Position Service](Player_Position_Service.md) (8 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (6 shared connections)
- [Validate an expanded command for](Validate_an_expanded_command_for.md) (5 shared connections)
- [world](world.md) (4 shared connections)
- [ContainerDataCore](ContainerDataCore.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [parse json field()](parse_json_field%28%29.md) (1 shared connections)
- [test alias graph](test_alias_graph.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 109 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*