# command models moderation

> 156 nodes

## Key Concepts

- **test_command_moderation.py** (38 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_command_factories_moderation.py** (29 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **validate_player_name()** (23 connections) — `server/validators/security_validator.py`
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
- **.create_add_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_mutes_command()** (6 connections) — `server/utils/command_factories_moderation.py`
- **test_mute_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_reason_max_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_validate_subcommand_invalid()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_subcommand_min_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_subcommand_max_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_create_mute_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- *... and 131 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (42 shared connections)
- [command inventory models](command_inventory_models.md) (20 shared connections)
- [command inventory factories](command_inventory_factories.md) (8 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (4 shared connections)
- [command communication models](command_communication_models.md) (3 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (3 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [services admin auth](services_admin_auth.md) (1 shared connections)
- [behavior engine npc](behavior_engine_npc.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_moderation.py`
- `server/tests/unit/models/test_command_moderation.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/utils/command_factories_moderation.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 470 (94%)
- INFERRED: 32 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*