# command processor rationale

> 34 nodes

## Key Concepts

- **test_command_alias.py** (18 connections) — `server/tests/unit/models/test_command_alias.py`
- **AliasCommand** (17 connections) — `server/models/command_alias.py`
- **UnaliasCommand** (12 connections) — `server/models/command_alias.py`
- **test_alias_command_alias_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_alias_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_command_max_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_alias_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_alias_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **.validate_alias_name_field()** (3 connections) — `server/models/command_alias.py`
- **test_alias_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_with_command()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_alias_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_none()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_aliases_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_validate_alias_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **Command for creating or viewing command aliases.** (1 connections) — `server/models/command_alias.py`
- **Command for removing an alias.** (1 connections) — `server/models/command_alias.py`
- **Validate alias name format using centralized validation.** (1 connections) — `server/models/command_alias.py`
- **Unit tests for alias command models.  Tests the alias command models and their v** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand requires alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand can have optional command.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand calls validate_alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand calls validate_command_content when command provided.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- *... and 9 more nodes in this community*

## Relationships

- [dialogue definition persistence](dialogue_definition_persistence.md) (9 shared connections)
- [add used user](add_used_user.md) (5 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (2 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/tests/unit/models/test_command_alias.py`

## Audit Trail

- EXTRACTED: 102 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*