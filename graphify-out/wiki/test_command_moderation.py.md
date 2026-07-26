# test_command_moderation.py

> 68 nodes · cohesion 0.04

## Key Concepts

- **test_command_moderation.py** (38 connections) — `server/tests/unit/models/test_command_moderation.py`
- **MuteCommand** (18 connections) — `server/models/command_moderation.py`
- **AdminCommand** (15 connections) — `server/models/command_moderation.py`
- **test_admin_command_subcommand_max_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_subcommand_min_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_validate_subcommand_invalid()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_reason_max_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **test_add_admin_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_add_admin_command_validate_player_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_validate_subcommand_case_insensitive()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_validate_subcommand_valid()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_with_args()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_validate_player_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_validate_reason_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_validate_reason_none()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_with_duration()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_with_reason()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- *... and 43 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (27 shared connections)
- [ValidationError](ValidationError.md) (8 shared connections)
- [test_command_factories_moderation.py](test_command_factories_moderation.py.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (2 shared connections)

## Source Files

- `server/models/command_moderation.py`
- `server/tests/unit/models/test_command_moderation.py`

## Audit Trail

- EXTRACTED: 193 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*