# validate_player_name

> 39 nodes

## Key Concepts

- **validate_player_name()** (23 connections) — `server/validators/security_validator.py`
- **field_validator** (8 connections)
- **.validate_player_name_field()** (4 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_target_player()** (4 connections) — `server/models/command_player_state.py`
- **field_validator** (4 connections)
- **.validate_subcommand()** (3 connections) — `server/models/command_moderation.py`
- **.validate_modifier()** (3 connections) — `server/models/command_player_state.py`
- **test_validate_player_name_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_long()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_rejects_invalid_chars()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_rejects_special_chars()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_sanitizes_unicode()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_single_char()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **field_validator** (2 connections)
- **Validate player name format using centralized validation.** (1 connections) — `server/models/command_admin.py`
- **Validate player name format using centralized validation.** (1 connections) — `server/models/command_admin.py`
- **Validate and normalize admin subcommand names.** (1 connections) — `server/models/command_moderation.py`
- **Validate player name format using centralized validation.** (1 connections) — `server/models/command_moderation.py`
- *... and 14 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (13 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (10 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (2 shared connections)
- [test_command_moderation.py](test_command_moderation.py.md) (1 shared connections)
- [.get_alias_file_path](get_alias_file_path.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_moderation.py`
- `server/models/command_player_state.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 70 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*