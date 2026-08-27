# sub_zone

> 8 nodes

## Key Concepts

- **.validate_player_name_field()** (4 connections) — `server/models/command_admin.py`
- **.validate_direction_field()** (4 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_admin.py`
- **field_validator** (4 connections)
- **.validate_prototype_id()** (3 connections) — `server/models/command_admin.py`
- **Validate player name format using centralized validation.** (2 connections) — `server/models/command_admin.py`
- **Validate prototype ID format. Args: value: The prototype ID to validate…** (1 connections) — `server/models/command_admin.py`
- **Ensure provided direction is part of the allowed set.** (1 connections) — `server/models/command_admin.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (2 shared connections)
- [.change_position](change_position.md) (1 shared connections)
- [TestCombatConfigurationService](TestCombatConfigurationService.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*