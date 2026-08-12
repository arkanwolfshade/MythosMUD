# NPC Death Lifecycle

> 557 nodes

## Key Concepts

- **BaseCommand** (150 connections) — `server/models/command_base.py`
- **command.py** (96 connections) — `server/models/command.py`
- **CommandType** (84 connections) — `server/models/command_base.py`
- **CommandFactory** (82 connections) — `server/utils/command_factories.py`
- **test_command_parser.py** (45 connections) — `server/tests/unit/utils/test_command_parser.py`
- **command_parser.py** (45 connections) — `server/utils/command_parser.py`
- **test_command_moderation.py** (38 connections) — `server/tests/unit/models/test_command_moderation.py`
- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **CastCommand** (20 connections) — `server/models/command_magic.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **MuteCommand** (18 connections) — `server/models/command_moderation.py`
- **command_utility.py** (18 connections) — `server/models/command_utility.py`
- **ExplorationCommandFactory** (17 connections) — `server/utils/command_factories_exploration.py`
- **PlayerStateCommandFactory** (17 connections) — `server/utils/command_factories_player_state.py`
- **command_moderation.py** (16 connections) — `server/models/command_moderation.py`
- **InventoryCommandFactory** (16 connections) — `server/utils/command_factories_inventory.py`
- **MuteGlobalCommand** (15 connections) — `server/models/command_moderation.py`
- **AdminCommand** (15 connections) — `server/models/command_moderation.py`
- **command_player_state.py** (15 connections) — `server/models/command_player_state.py`
- *... and 532 more nodes in this community*

## Relationships

- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (56 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (34 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (33 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (30 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (29 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (29 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (29 shared connections)
- [Mythos Time HUD](Mythos_Time_HUD.md) (24 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (21 shared connections)
- [NPC Occupant Processor](NPC_Occupant_Processor.md) (20 shared connections)
- [Client Event Store](Client_Event_Store.md) (19 shared connections)
- [Base Command Models](Base_Command_Models.md) (18 shared connections)

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
- `server/models/command_moderation.py`
- `server/models/command_party.py`
- `server/models/command_player_state.py`
- `server/models/command_utility.py`
- `server/tests/unit/models/test_command_moderation.py`
- `server/tests/unit/models/test_command_player_state.py`
- `server/tests/unit/models/test_command_utility.py`
- `server/tests/unit/test_command_parser_smoke.py`
- `server/tests/unit/utils/test_command_factories_combat.py`

## Audit Trail

- EXTRACTED: 2102 (89%)
- INFERRED: 261 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*