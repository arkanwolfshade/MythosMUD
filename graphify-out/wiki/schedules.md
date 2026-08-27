# schedules

> 8 nodes

## Key Concepts

- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **test_command_validator_extract_command_name()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_empty()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_with_slash()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.extract_command_name extracts command name.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.extract_command_name handles slash prefix.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.extract_command_name returns None for empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Extract the base command name from a command string. Handles various formats: -…** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [test_room_service.py](test_room_service.py.md) (4 shared connections)
- [subject_controller.py](subject_controller.py.md) (3 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 11 (79%)
- INFERRED: 3 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*