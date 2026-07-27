# Moderation Command Models

> 96 nodes · cohesion 0.03

## Key Concepts

- **test_command_moderation.py** (37 connections) — `server/tests/unit/models/test_command_moderation.py`
- **validate_player_name()** (21 connections) — `server/validators/security_validator.py`
- **MuteCommand** (18 connections) — `server/models/command_moderation.py`
- **command_moderation.py** (15 connections) — `server/models/command_moderation.py`
- **AdminCommand** (15 connections) — `server/models/command_moderation.py`
- **MuteGlobalCommand** (15 connections) — `server/models/command_moderation.py`
- **AddAdminCommand** (10 connections) — `server/models/command_moderation.py`
- **UnmuteCommand** (10 connections) — `server/models/command_moderation.py`
- **UnmuteGlobalCommand** (10 connections) — `server/models/command_moderation.py`
- **Validate player name format using centralized validation.** (5 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_reason()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_reason()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_target_player()** (3 connections) — `server/models/command_player_state.py`
- **Test GotoCommand calls validate_player_name.** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_add_admin_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_add_admin_command_validate_player_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_subcommand_max_length()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- *... and 71 more nodes in this community*

## Relationships

- [[Base Command Models]] (33 shared connections)
- [[Command Field Validators]] (14 shared connections)
- [[Admin Command Models]] (4 shared connections)
- [[Lie Ground Commands]] (1 shared connections)
- [[Combat Command Models]] (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_moderation.py`
- `server/models/command_player_state.py`
- `server/tests/unit/models/test_command_admin.py`
- `server/tests/unit/models/test_command_moderation.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 331 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
