# health models rationale

> 108 nodes

## Key Concepts

- **test_command_moderation.py** (38 connections) — `server/tests/unit/models/test_command_moderation.py`
- **validate_player_name()** (23 connections) — `server/validators/security_validator.py`
- **MuteCommand** (18 connections) — `server/models/command_moderation.py`
- **command_moderation.py** (16 connections) — `server/models/command_moderation.py`
- **MuteGlobalCommand** (15 connections) — `server/models/command_moderation.py`
- **AdminCommand** (15 connections) — `server/models/command_moderation.py`
- **UnmuteCommand** (10 connections) — `server/models/command_moderation.py`
- **UnmuteGlobalCommand** (10 connections) — `server/models/command_moderation.py`
- **AddAdminCommand** (10 connections) — `server/models/command_moderation.py`
- **MutesCommand** (8 connections) — `server/models/command_moderation.py`
- **test_mute_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_reason_max_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_validate_subcommand_invalid()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_subcommand_min_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_subcommand_max_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_reason()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_reason()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_moderation.py`
- *... and 83 more nodes in this community*

## Relationships

- [dialogue definition persistence](dialogue_definition_persistence.md) (18 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (13 shared connections)
- [command inventory factories](command_inventory_factories.md) (8 shared connections)
- [command inventory models](command_inventory_models.md) (8 shared connections)
- [stores connectionStore commandStore](stores_connectionStore_commandStore.md) (7 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [inventory commands command](inventory_commands_command.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)

## Source Files

- `server/models/command_moderation.py`
- `server/tests/unit/models/test_command_moderation.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 333 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*