# processing

> 27 nodes

## Key Concepts

- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
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
- **ValidationError** (2 connections)
- **Exception** (2 connections)
- **Test CommandValidator.is_security_sensitive detects admin commands.** (2 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive returns False for non-sensitive comm** (2 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Command Processing Logic for MythosMUD.  This module contains the core command** (1 connections) — `server/command_handler/processing.py`
- **Validate the raw command string via CommandProcessor.      Returns:         (** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- **Parse the command line; on success run CommandService (see ``_parse_command_line** (1 connections) — `server/command_handler/processing.py`
- **Validate ``command_line`` via Click/Pydantic, dispatch to handlers; result dict** (1 connections) — `server/command_handler/processing.py`
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a validation error during command processing.** (1 connections) — `server/command_handler/processing.py`
- *... and 2 more nodes in this community*

## Relationships

- [Validate an expanded command for](Validate_an_expanded_command_for.md) (8 shared connections)
- [CommandExecutionRequest](CommandExecutionRequest.md) (6 shared connections)
- [Any](Any.md) (4 shared connections)
- [main()](main%28%29.md) (4 shared connections)
- [.validate topic()](validate_topic%28%29.md) (3 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (2 shared connections)
- [command execution request](command_execution_request.md) (1 shared connections)
- [CommandHandler](CommandHandler.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [APIRouter](APIRouter.md) (1 shared connections)
- [command processor()](command_processor%28%29.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 107 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*