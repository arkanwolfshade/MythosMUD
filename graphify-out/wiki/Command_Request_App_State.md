# Command Request App State

> 28 nodes

## Key Concepts

- **test_command_alias.py** (18 connections) — `server/tests/unit/models/test_command_alias.py`
- **AliasCommand** (17 connections) — `server/models/command_alias.py`
- **test_alias_command_alias_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_alias_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_command_max_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **.validate_command()** (3 connections) — `server/models/command_alias.py`
- **test_alias_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_with_command()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_alias_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_none()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_aliases_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_validate_alias_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **Command for creating or viewing command aliases.** (1 connections) — `server/models/command_alias.py`
- **Validate command content for security using centralized validation.** (1 connections) — `server/models/command_alias.py`
- **Unit tests for alias command models.  Tests the alias command models and their v** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand requires alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand can have optional command.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand calls validate_alias_name.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand calls validate_command_content when command provided.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand accepts None for command.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand validates alias_name min length.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand validates alias_name max length.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- **Test AliasCommand validates command max length.** (1 connections) — `server/tests/unit/models/test_command_alias.py`
- *... and 3 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (8 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (5 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (4 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/tests/unit/models/test_command_alias.py`

## Audit Trail

- EXTRACTED: 83 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*