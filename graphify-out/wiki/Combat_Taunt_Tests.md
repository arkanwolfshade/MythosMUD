# Combat Taunt Tests

> 249 nodes · cohesion 0.01

## Key Concepts

- **test_security_validator.py** (96 connections) — `server/tests/unit/validators/test_security_validator.py`
- **security_validator.py** (34 connections) — `server/validators/security_validator.py`
- **validate_player_name()** (23 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **validate_combat_target()** (14 connections) — `server/validators/security_validator.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **validate_action_content()** (11 connections) — `server/validators/security_validator.py`
- **validate_alias_name()** (10 connections) — `server/validators/security_validator.py`
- **validate_reason_content()** (10 connections) — `server/validators/security_validator.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **sanitize_unicode_input()** (9 connections) — `server/validators/security_validator.py`
- **validate_command_content()** (9 connections) — `server/validators/security_validator.py`
- **validate_pose_content()** (9 connections) — `server/validators/security_validator.py`
- **validate_filter_name()** (8 connections) — `server/validators/security_validator.py`
- **validate_help_topic()** (8 connections) — `server/validators/security_validator.py`
- **validate_security_comprehensive()** (8 connections) — `server/validators/security_validator.py`
- **validate_target_player()** (8 connections) — `server/validators/security_validator.py`
- **check_dangerous_characters()** (6 connections) — `server/validators/security_validator.py`
- **check_injection_patterns()** (6 connections) — `server/validators/security_validator.py`
- **get_dangerous_characters()** (5 connections) — `server/validators/security_validator.py`
- **get_injection_patterns()** (5 connections) — `server/validators/security_validator.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_admin.py`
- **.validate_alias_name_field()** (3 connections) — `server/models/command_alias.py`
- *... and 224 more nodes in this community*

## Relationships

- [Admin Command Models](Admin_Command_Models.md) (44 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (11 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (4 shared connections)
- [Realtime Message Formatters](Realtime_Message_Formatters.md) (3 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (2 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Player State Factories](Player_State_Factories.md) (1 shared connections)
- [Server Config Loading](Server_Config_Loading.md) (1 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_alias.py`
- `server/models/command_combat.py`
- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/models/command_player_state.py`
- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 759 (98%)
- INFERRED: 18 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*