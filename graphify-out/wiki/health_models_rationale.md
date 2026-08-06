# health models rationale

> 110 nodes

## Key Concepts

- **test_command_moderation.py** (38 connections) — `server/tests/unit/models/test_command_moderation.py`
- **MuteCommand** (18 connections) — `server/models/command_moderation.py`
- **MuteGlobalCommand** (15 connections) — `server/models/command_moderation.py`
- **AdminCommand** (15 connections) — `server/models/command_moderation.py`
- **UnmuteCommand** (10 connections) — `server/models/command_moderation.py`
- **UnmuteGlobalCommand** (10 connections) — `server/models/command_moderation.py`
- **AddAdminCommand** (10 connections) — `server/models/command_moderation.py`
- **.create_mute_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_mute_global_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_global_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **test_mute_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_reason_max_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_validate_subcommand_invalid()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_subcommand_min_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_subcommand_max_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **test_mute_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_with_duration()** (3 connections) — `server/tests/unit/models/test_command_moderation.py`
- *... and 85 more nodes in this community*

## Relationships

- [add used user](add_used_user.md) (26 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (21 shared connections)
- [command inventory factories](command_inventory_factories.md) (10 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (7 shared connections)
- [Inventory Equip](Inventory_Equip.md) (4 shared connections)

## Source Files

- `server/models/command_moderation.py`
- `server/tests/unit/models/test_command_moderation.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/utils/command_factories_moderation.py`

## Audit Trail

- EXTRACTED: 322 (94%)
- INFERRED: 20 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*