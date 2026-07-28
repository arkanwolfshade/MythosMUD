# Server Commands (5)

> 117 nodes

## Key Concepts

- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **CommandService** (20 connections) — `server/commands/command_service.py`
- **command_input.py** (14 connections) — `server/command_handler/command_input.py`
- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (10 connections) — `server/command_handler/command_input.py`
- **Any** (10 connections)
- **CommandExecutionRequest** (9 connections)
- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **handle_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **_is_predefined_emote()** (8 connections) — `server/command_handler/command_input.py`
- **test_command_input.py** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **TestEmoteDetection** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (7 connections) — `server/commands/command_service.py`
- **get_command_processor()** (7 connections) — `server/utils/command_processor.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- *... and 92 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (28 shared connections)
- [Server Commands (3)](Server_Commands_%283%29.md) (18 shared connections)
- [Server Validators (4)](Server_Validators_%284%29.md) (16 shared connections)
- [Server Validators](Server_Validators.md) (12 shared connections)
- [Server Command Handler](Server_Command_Handler.md) (5 shared connections)
- [Server Validators (17)](Server_Validators_%2817%29.md) (4 shared connections)
- [Server Commands (10)](Server_Commands_%2810%29.md) (3 shared connections)
- [Server Utils (22)](Server_Utils_%2822%29.md) (3 shared connections)
- [Server Validators (9)](Server_Validators_%289%29.md) (2 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (1 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)
- [Server Utils](Server_Utils.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_input.py`
- `server/command_handler/processing.py`
- `server/commands/command_service.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/utils/command_processor.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 441 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*