# feature services flag

> 50 nodes

## Key Concepts

- **test_command_alias.py** (18 connections) — `server/tests/unit/models/test_command_alias.py`
- **AliasCommand** (17 connections) — `server/models/command_alias.py`
- **command_alias.py** (12 connections) — `server/models/command_alias.py`
- **UnaliasCommand** (12 connections) — `server/models/command_alias.py`
- **validate_alias_name()** (10 connections) — `server/validators/security_validator.py`
- **AliasesCommand** (8 connections) — `server/models/command_alias.py`
- **test_alias_command_alias_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_alias_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_command_max_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_alias_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_alias_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **.validate_alias_name_field()** (3 connections) — `server/models/command_alias.py`
- **.validate_alias_name_field()** (3 connections) — `server/models/command_alias.py`
- **test_alias_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_with_command()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_alias_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_none()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_aliases_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_validate_alias_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_validate_alias_name_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_alias_name_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_alias_name_rejects_invalid_format()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_alias_name_rejects_hyphens()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- *... and 25 more nodes in this community*

## Relationships

- [container persistence rationale](container_persistence_rationale.md) (9 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (9 shared connections)
- [command inventory models](command_inventory_models.md) (5 shared connections)
- [command factories create](command_factories_create.md) (4 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (3 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/tests/unit/models/test_command_alias.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 152 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*