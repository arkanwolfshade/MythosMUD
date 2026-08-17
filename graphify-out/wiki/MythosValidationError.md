# MythosValidationError

> 11 nodes

## Key Concepts

- **MythosValidationError** (10 connections)
- **test_process_validated_command_validation_error()** (5 connections) — `server/tests/unit/commands/test_command_service.py`
- **.test_handle_transfer_items_exceptions_validation_error()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_create_command_object_re_raises_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_process_command_string_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Test handle_transfer_items_exceptions returns 400 for ValidationError.** (1 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **Test _parse_command_string handles ValidationError.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command handles ValidationError.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test _create_command_object re-raises MythosValidationError without wrapping.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test process_command_string handles MythosMUD validation errors.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (2 shared connections)
- [test_command_service.py](test_command_service.py.md) (2 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (2 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (1 shared connections)
- [test_command_processor.py](test_command_processor.py.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)
- [CommunicationCommandFactory](CommunicationCommandFactory.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 14 (54%)
- INFERRED: 12 (46%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*