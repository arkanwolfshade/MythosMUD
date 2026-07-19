# Alias Command Models

> 30 nodes · cohesion 0.08

## Key Concepts

- **test_command_alias.py** (17 connections) — `server/tests/unit/models/test_command_alias.py`
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
- **test_cast_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **Unit tests for admin command models.  Tests the admin command models and their v** (2 connections) — `server/tests/unit/models/test_command_admin.py`
- **Test UnaliasCommand validates alias_name min length.** (2 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand can have optional command.** (2 connections) — `server/tests/unit/models/test_command_alias.py`
- **Command for removing an alias.** (1 connections) — `server/models/command_alias.py`
- **Test UnaliasCommand requires alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test UnaliasCommand calls validate_alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand requires alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand calls validate_alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand calls validate_command_content when command provided.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- *... and 5 more nodes in this community*

## Relationships

- [[Base Command Models]] (18 shared connections)
- [[Command Field Validators]] (1 shared connections)
- [[Admin Command Models]] (1 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/tests/unit/models/test_command_admin.py`
- `server/tests/unit/models/test_command_alias.py`
- `server/tests/unit/models/test_command_magic.py`

## Audit Trail

- EXTRACTED: 86 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
