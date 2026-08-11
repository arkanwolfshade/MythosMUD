# Admin Command Models

> 144 nodes

## Key Concepts

- **test_command_moderation.py** (38 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_command_factories_moderation.py** (29 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **MuteCommand** (18 connections) — `server/models/command_moderation.py`
- **command_moderation.py** (16 connections) — `server/models/command_moderation.py`
- **MuteGlobalCommand** (15 connections) — `server/models/command_moderation.py`
- **AdminCommand** (15 connections) — `server/models/command_moderation.py`
- **ModerationCommandFactory** (13 connections) — `server/utils/command_factories_moderation.py`
- **UnmuteCommand** (10 connections) — `server/models/command_moderation.py`
- **UnmuteGlobalCommand** (10 connections) — `server/models/command_moderation.py`
- **AddAdminCommand** (10 connections) — `server/models/command_moderation.py`
- **.create_mute_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_mute_global_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **MutesCommand** (8 connections) — `server/models/command_moderation.py`
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
- *... and 119 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (26 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (20 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (10 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (7 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (4 shared connections)
- [Base Command Models](Base_Command_Models.md) (1 shared connections)

## Source Files

- `server/models/command_moderation.py`
- `server/tests/unit/models/test_command_moderation.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/utils/command_factories_moderation.py`

## Audit Trail

- EXTRACTED: 452 (93%)
- INFERRED: 34 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*