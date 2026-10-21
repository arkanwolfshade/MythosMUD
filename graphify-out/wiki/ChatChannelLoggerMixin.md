# ChatChannelLoggerMixin

> 33 nodes · cohesion 0.11

## Key Concepts

- **processing.py** (28 connections) — `server/command_handler/processing.py`
- **test_command_processing.py** (17 connections) — `server/tests/unit/commands/test_command_processing.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (7 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (7 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (7 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (6 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **asyncio** (5 connections)
- **test_process_command_with_validation_validation_error()** (5 connections) — `server/tests/unit/commands/test_command_processing.py`
- **CommandExecutionRequest** (4 connections)
- **test_handle_validation_error_security_sensitive()** (4 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_generic_error()** (4 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_client_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_success()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_handle_processing_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_no_validated()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_with_message()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_run_command_service_security_sensitive_audit()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_log_security_sensitive_command_no_session()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **Exception** (1 connections)
- **ValidationError** (1 connections)
- **Command Processing Logic for MythosMUD. This module contains the core command…** (1 connections) — `server/command_handler/processing.py`
- *... and 8 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (10 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (6 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [Room](Room.md) (3 shared connections)
- [test_look_item_helpers.py](test_look_item_helpers.py.md) (3 shared connections)
- [command_parser.py](command_parser.py.md) (3 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (2 shared connections)
- [CommandFactory](CommandFactory.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [test_passive_corruption_flux_rate_overrides.py](test_passive_corruption_flux_rate_overrides.py.md) (2 shared connections)
- [QuestService](QuestService.md) (2 shared connections)
- [Dream Messaging Subsystem Design](Dream_Messaging_Subsystem_Design.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_command_processing.py`

## Audit Trail

- EXTRACTED: 90 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*