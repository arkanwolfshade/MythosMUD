# Community 566

> 30 nodes

## Key Concepts

- **test_command_processing.py** (17 connections) — `server/tests/unit/commands/test_command_processing.py`
- **process_command_with_validation()** (12 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (6 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (5 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (5 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (5 connections) — `server/command_handler/processing.py`
- **test_process_command_with_validation_validation_error()** (5 connections) — `server/tests/unit/commands/test_command_processing.py`
- **asyncio** (5 connections)
- **test_handle_validation_error_security_sensitive()** (4 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_generic_error()** (4 connections) — `server/tests/unit/commands/test_command_processing.py`
- **CommandExecutionRequest** (4 connections)
- **test_dispatch_parsed_command_client_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_success()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_handle_processing_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_no_validated()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_with_message()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_run_command_service_security_sensitive_audit()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_log_security_sensitive_command_no_session()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **Exception** (1 connections)
- **Validate ``command_line`` via Click/Pydantic, dispatch to handlers; result dict…** (1 connections) — `server/command_handler/processing.py`
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a validation error during command processing.** (1 connections) — `server/command_handler/processing.py`
- *... and 5 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (9 shared connections)
- [Community 98](Community_98.md) (7 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (4 shared connections)
- [Community 836](Community_836.md) (1 shared connections)
- [Community 262](Community_262.md) (1 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (1 shared connections)
- [Community 41](Community_41.md) (1 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_command_processing.py`

## Audit Trail

- EXTRACTED: 63 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*