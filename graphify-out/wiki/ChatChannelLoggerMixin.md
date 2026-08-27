# ChatChannelLoggerMixin

> 33 nodes

## Key Concepts

- **validate_player_name()** (30 connections) — `server/validators/security_validator.py`
- **field_validator** (8 connections)
- **Validate player name format using centralized validation.** (5 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_moderation.py`
- **.validate_subcommand()** (3 connections) — `server/models/command_moderation.py`
- **test_validate_player_name_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_long()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_max_length_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_min_length_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_rejects_invalid_chars()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_rejects_spaces()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_rejects_special_chars()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_sanitizes_unicode()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_single_char()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_too_short()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Validate and normalize admin subcommand names.** (1 connections) — `server/models/command_moderation.py`
- **Test validating empty player name (returns empty string).** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating single character player name (invalid under ADR-021 min length).** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating two-character player name (invalid under ADR-021).** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating player name over max length.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- *... and 8 more nodes in this community*

## Relationships

- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (12 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (10 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (2 shared connections)
- [sub_zone](sub_zone.md) (2 shared connections)
- [holidays.schema.json](holidays.schema.json.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [Main Foyer Starting Room](Main_Foyer_Starting_Room.md) (1 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (1 shared connections)
- [test_look_container.py](test_look_container.py.md) (1 shared connections)

## Source Files

- `server/models/command_moderation.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*