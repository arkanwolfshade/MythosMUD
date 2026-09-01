# test_command_alias.py

> 32 nodes

## Key Concepts

- **test_command_alias.py** (20 connections) — `server/tests/unit/models/test_command_alias.py`
- **AliasCommand** (17 connections) — `server/models/command_alias.py`
- **UnaliasCommand** (12 connections) — `server/models/command_alias.py`
- **test_alias_command_alias_name_max_length()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_alias_name_min_length()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_command_max_length()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_alias_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_none()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_with_command()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_aliases_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_alias_name_max_length()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_alias_name_min_length()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_validate_alias_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **Command for creating or viewing command aliases.** (1 connections) — `server/models/command_alias.py`
- **Command for removing an alias.** (1 connections) — `server/models/command_alias.py`
- **Unit tests for alias command models. Tests the alias command models and their…** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test UnaliasCommand requires alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test UnaliasCommand calls validate_alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test UnaliasCommand validates alias_name min length.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test UnaliasCommand validates alias_name max length.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand requires alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand can have optional command.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- *... and 7 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (11 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [pydantic.md](pydantic.md.md) (1 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/tests/unit/models/test_command_alias.py`

## Audit Trail

- EXTRACTED: 59 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*