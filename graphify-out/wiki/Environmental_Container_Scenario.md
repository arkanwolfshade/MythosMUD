# Environmental Container Scenario

> 100 nodes

## Key Concepts

- **test_command_combat.py** (30 connections) — `server/tests/unit/models/test_command_combat.py`
- **AttackCommand** (14 connections) — `server/models/command_combat.py`
- **PunchCommand** (14 connections) — `server/models/command_combat.py`
- **KickCommand** (14 connections) — `server/models/command_combat.py`
- **StrikeCommand** (14 connections) — `server/models/command_combat.py`
- **test_command_factories_combat.py** (14 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **CombatCommandFactory** (12 connections) — `server/utils/command_factories_combat.py`
- **.__init__()** (9 connections) — `server/utils/command_factories.py`
- **command_factories_combat.py** (7 connections) — `server/utils/command_factories_combat.py`
- **.create_attack_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_punch_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_kick_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_strike_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_taunt_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **test_attack_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_punch_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_punch_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_strike_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_strike_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **.create_flee_command()** (4 connections) — `server/utils/command_factories_combat.py`
- **test_attack_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- *... and 75 more nodes in this community*

## Relationships

- [Zone Config Loader](Zone_Config_Loader.md) (16 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (8 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (6 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (2 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (1 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (1 shared connections)
- [Base Command Models](Base_Command_Models.md) (1 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)
- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (1 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/models/command_combat.py`
- `server/tests/unit/models/test_command_combat.py`
- `server/tests/unit/utils/test_command_factories_combat.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_combat.py`

## Audit Trail

- EXTRACTED: 303 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*