# Zone Config Loader

> 138 nodes

## Key Concepts

- **command.py** (96 connections) — `server/models/command.py`
- **CommandType** (84 connections) — `server/models/command_base.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_communication.py** (19 connections) — `server/models/command_communication.py`
- **command_utility.py** (18 connections) — `server/models/command_utility.py`
- **command_player_state.py** (15 connections) — `server/models/command_player_state.py`
- **LieCommand** (15 connections) — `server/models/command_player_state.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
- **command_combat.py** (14 connections) — `server/models/command_combat.py`
- **command_inventory.py** (13 connections) — `server/models/command_inventory.py`
- **HelpCommand** (13 connections) — `server/models/command_utility.py`
- **WhoCommand** (13 connections) — `server/models/command_utility.py`
- **GroundCommand** (12 connections) — `server/models/command_player_state.py`
- **command_magic.py** (10 connections) — `server/models/command_magic.py`
- **command_follow.py** (8 connections) — `server/models/command_follow.py`
- **InventoryCommand** (8 connections) — `server/models/command_inventory.py`
- **SpellsCommand** (8 connections) — `server/models/command_magic.py`
- **QuitCommand** (8 connections) — `server/models/command_player_state.py`
- **LogoutCommand** (8 connections) — `server/models/command_player_state.py`
- **SitCommand** (8 connections) — `server/models/command_player_state.py`
- **StandCommand** (8 connections) — `server/models/command_player_state.py`
- **StatusCommand** (8 connections) — `server/models/command_utility.py`
- **TimeCommand** (8 connections) — `server/models/command_utility.py`
- *... and 113 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (37 shared connections)
- [NPC Occupant Processor](NPC_Occupant_Processor.md) (25 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (21 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (20 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (17 shared connections)
- [Environmental Container Scenario](Environmental_Container_Scenario.md) (16 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (15 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (15 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (12 shared connections)
- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (11 shared connections)
- [Integer Coercion Utils](Integer_Coercion_Utils.md) (9 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (9 shared connections)

## Source Files

- `server/models/command.py`
- `server/models/command_admin.py`
- `server/models/command_base.py`
- `server/models/command_channel.py`
- `server/models/command_combat.py`
- `server/models/command_communication.py`
- `server/models/command_follow.py`
- `server/models/command_inventory.py`
- `server/models/command_magic.py`
- `server/models/command_party.py`
- `server/models/command_player_state.py`
- `server/models/command_utility.py`
- `server/tests/unit/models/test_command_player_state.py`
- `server/tests/unit/models/test_command_utility.py`

## Audit Trail

- EXTRACTED: 608 (84%)
- INFERRED: 120 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*