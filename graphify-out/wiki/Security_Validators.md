# Security Validators

> 226 nodes

## Key Concepts

- **test_security_validator.py** (102 connections) — `server/tests/unit/validators/test_security_validator.py`
- **validate_player_name()** (28 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **validate_combat_target()** (15 connections) — `server/validators/security_validator.py`
- **validate_alias_name()** (10 connections) — `server/validators/security_validator.py`
- **validate_reason_content()** (10 connections) — `server/validators/security_validator.py`
- **validate_command_content()** (9 connections) — `server/validators/security_validator.py`
- **validate_pose_content()** (9 connections) — `server/validators/security_validator.py`
- **field_validator** (9 connections)
- **validate_filter_name()** (8 connections) — `server/validators/security_validator.py`
- **validate_security_comprehensive()** (8 connections) — `server/validators/security_validator.py`
- **field_validator** (8 connections)
- **check_dangerous_characters()** (6 connections) — `server/validators/security_validator.py`
- **check_injection_patterns()** (6 connections) — `server/validators/security_validator.py`
- **get_dangerous_characters()** (5 connections) — `server/validators/security_validator.py`
- **get_injection_patterns()** (5 connections) — `server/validators/security_validator.py`
- **field_validator** (5 connections)
- **Validate combat target name format using centralized validation.** (5 connections) — `server/models/command_combat.py`
- **Validate player name format using centralized validation.** (5 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_admin.py`
- **.validate_direction_field()** (4 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_admin.py`
- **.validate_alias_name_field()** (4 connections) — `server/models/command_alias.py`
- **.validate_command()** (4 connections) — `server/models/command_alias.py`
- **.validate_alias_name_field()** (4 connections) — `server/models/command_alias.py`
- *... and 201 more nodes in this community*

## Relationships

- [Command Aliases](Command_Aliases.md) (60 shared connections)
- [Test Command Validator](Test_Command_Validator.md) (22 shared connections)
- [Test Command Admin](Test_Command_Admin.md) (5 shared connections)
- [Test Command Moderation](Test_Command_Moderation.md) (2 shared connections)
- [Alias Storage](Alias_Storage.md) (2 shared connections)
- [Test Rooms Write Api](Test_Rooms_Write_Api.md) (1 shared connections)
- [Command Player State](Command_Player_State.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_alias.py`
- `server/models/command_combat.py`
- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 406 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*