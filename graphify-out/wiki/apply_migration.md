# apply_migration

> 10 nodes

## Key Concepts

- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **test_command_validator_validate_expanded_command_inherits_content_validation()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_length_limit()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_valid()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_within_limit()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command returns True for valid expanded…** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command inherits content validation.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command enforces expanded length limit.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command allows commands within expanded…** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Validate command after alias expansion. Uses stricter length limits since…** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [test_room_service.py](test_room_service.py.md) (6 shared connections)
- [subject_controller.py](subject_controller.py.md) (4 shared connections)
- [RoomRepository](RoomRepository.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 16 (80%)
- INFERRED: 4 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*