# Server Models (4)

> 135 nodes

## Key Concepts

- **test_command_moderation.py** (38 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_command_factories_moderation.py** (29 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **MuteCommand** (18 connections) — `server/models/command_moderation.py`
- **command_moderation.py** (16 connections) — `server/models/command_moderation.py`
- **MuteGlobalCommand** (15 connections) — `server/models/command_moderation.py`
- **AdminCommand** (15 connections) — `server/models/command_moderation.py`
- **UnmuteCommand** (10 connections) — `server/models/command_moderation.py`
- **UnmuteGlobalCommand** (10 connections) — `server/models/command_moderation.py`
- **AddAdminCommand** (10 connections) — `server/models/command_moderation.py`
- **.create_mute_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_mute_global_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **MutesCommand** (8 connections) — `server/models/command_moderation.py`
- **Test create_mute_command() raises error with no args.** (7 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **.create_unmute_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_global_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_add_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_mutes_command()** (6 connections) — `server/utils/command_factories_moderation.py`
- **Validate player name format using centralized validation.** (5 connections) — `server/models/command_moderation.py`
- **test_mute_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_command_reason_max_length()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_mute_global_command_duration_validation_max()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_admin_command_validate_subcommand_invalid()** (4 connections) — `server/tests/unit/models/test_command_moderation.py`
- *... and 110 more nodes in this community*

## Relationships

- [Server Utils](Server_Utils.md) (20 shared connections)
- [Server Models](Server_Models.md) (17 shared connections)
- [Server Utils (2)](Server_Utils_%282%29.md) (16 shared connections)
- [Server Validators](Server_Validators.md) (10 shared connections)
- [Server Game](Server_Game.md) (7 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/models/command_moderation.py`
- `server/tests/unit/models/test_command_moderation.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/utils/command_factories_moderation.py`

## Audit Trail

- EXTRACTED: 459 (93%)
- INFERRED: 33 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*