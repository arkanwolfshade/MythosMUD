# processing.py

> 90 nodes

## Key Concepts

- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **AliasGraph** (18 connections) — `server/utils/alias_graph.py`
- **alias_expansion.py** (17 connections) — `server/command_handler/alias_expansion.py`
- **test_command_processing.py** (16 connections) — `server/tests/unit/commands/test_command_processing.py`
- **command_handler/__init__.py** (14 connections) — `server/command_handler/__init__.py`
- **test_alias_expansion.py** (14 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_graph.py** (9 connections) — `server/tests/unit/utils/test_alias_graph.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **alias_graph.py** (8 connections) — `server/utils/alias_graph.py`
- **_handle_processing_error()** (7 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (7 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (7 connections) — `server/command_handler/processing.py`
- **get_command_processor()** (7 connections) — `server/utils/command_processor.py`
- **_handle_validation_error()** (6 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **asyncio** (5 connections)
- **asyncio** (5 connections)
- **test_process_command_with_validation_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_processing.py`
- **CommandExecutionRequest** (4 connections)
- **test_check_alias_safety_cycle_detected()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_depth_too_deep()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- *... and 65 more nodes in this community*

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (15 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [AliasStorage](AliasStorage.md) (8 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (7 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [CommandProcessor](CommandProcessor.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_alias_expansion.py`
- `server/tests/unit/commands/test_command_processing.py`
- `server/tests/unit/utils/test_alias_graph.py`
- `server/utils/alias_graph.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 203 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*