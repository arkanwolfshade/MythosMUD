# Chat Command Validation

> 186 nodes

## Key Concepts

- **test_security_validator.py** (101 connections) — `server/tests/unit/validators/test_security_validator.py`
- **validate_player_name()** (28 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **validate_action_content()** (11 connections) — `server/validators/security_validator.py`
- **validate_reason_content()** (10 connections) — `server/validators/security_validator.py`
- **field_validator** (9 connections)
- **validate_security_comprehensive()** (8 connections) — `server/validators/security_validator.py`
- **validate_target_player()** (8 connections) — `server/validators/security_validator.py`
- **field_validator** (8 connections)
- **check_dangerous_characters()** (6 connections) — `server/validators/security_validator.py`
- **check_injection_patterns()** (6 connections) — `server/validators/security_validator.py`
- **validate_filter_name()** (6 connections) — `server/validators/security_validator.py`
- **validate_help_topic()** (6 connections) — `server/validators/security_validator.py`
- **get_dangerous_characters()** (5 connections) — `server/validators/security_validator.py`
- **get_injection_patterns()** (5 connections) — `server/validators/security_validator.py`
- **Validate player name format using centralized validation.** (5 connections) — `server/models/command_moderation.py`
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **.validate_action()** (4 connections) — `server/models/command_communication.py`
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **.validate_target()** (4 connections) — `server/models/command_communication.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- *... and 161 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (43 shared connections)
- [Community 106](Community_106.md) (13 shared connections)
- [Community 167](Community_167.md) (10 shared connections)
- [Community 52](Community_52.md) (7 shared connections)
- [Community 315](Community_315.md) (5 shared connections)
- [Community 130](Community_130.md) (3 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (1 shared connections)
- [Community 25](Community_25.md) (1 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (1 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (1 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 339 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*