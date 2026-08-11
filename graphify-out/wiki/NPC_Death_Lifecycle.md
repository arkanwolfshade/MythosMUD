# NPC Death Lifecycle

> 563 nodes

## Key Concepts

- **BaseCommand** (150 connections) — `server/models/command_base.py`
- **command.py** (96 connections) — `server/models/command.py`
- **CommandType** (84 connections) — `server/models/command_base.py`
- **CommandFactory** (82 connections) — `server/utils/command_factories.py`
- **test_command_communication.py** (45 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **test_command_base.py** (22 connections) — `server/tests/unit/models/test_command_base.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_communication.py** (19 connections) — `server/models/command_communication.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **command_utility.py** (18 connections) — `server/models/command_utility.py`
- **test_command_alias.py** (18 connections) — `server/tests/unit/models/test_command_alias.py`
- **AliasCommand** (17 connections) — `server/models/command_alias.py`
- **WhisperCommand** (15 connections) — `server/models/command_communication.py`
- **command_player_state.py** (15 connections) — `server/models/command_player_state.py`
- **LieCommand** (15 connections) — `server/models/command_player_state.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
- **command_combat.py** (14 connections) — `server/models/command_combat.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- *... and 538 more nodes in this community*

## Relationships

- [Spell Registry Costs](Spell_Registry_Costs.md) (45 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (35 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (28 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (27 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (26 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (22 shared connections)
- [NPC Occupant Processor](NPC_Occupant_Processor.md) (21 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (13 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (11 shared connections)
- [Container Open Events](Container_Open_Events.md) (5 shared connections)
- [Character Creation API](Character_Creation_API.md) (3 shared connections)
- [Base Command Models](Base_Command_Models.md) (3 shared connections)

## Source Files

- `server/models/command.py`
- `server/models/command_admin.py`
- `server/models/command_alias.py`
- `server/models/command_base.py`
- `server/models/command_channel.py`
- `server/models/command_combat.py`
- `server/models/command_communication.py`
- `server/models/command_exploration.py`
- `server/models/command_follow.py`
- `server/models/command_inventory.py`
- `server/models/command_magic.py`
- `server/models/command_party.py`
- `server/models/command_player_state.py`
- `server/models/command_utility.py`
- `server/tests/unit/models/test_command_admin.py`
- `server/tests/unit/models/test_command_alias.py`
- `server/tests/unit/models/test_command_base.py`
- `server/tests/unit/models/test_command_communication.py`
- `server/tests/unit/models/test_command_exploration.py`
- `server/tests/unit/models/test_command_player_state.py`

## Audit Trail

- EXTRACTED: 1909 (87%)
- INFERRED: 289 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*