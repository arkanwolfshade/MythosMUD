# Server Utils (2)

> 128 nodes

## Key Concepts

- **BaseCommand** (150 connections) — `server/models/command_base.py`
- **CommandFactory** (82 connections) — `server/utils/command_factories.py`
- **Create SayCommand from arguments.** (35 connections) — `server/utils/command_factories.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **PlayerStateCommandFactory** (17 connections) — `server/utils/command_factories_player_state.py`
- **InventoryCommandFactory** (16 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- **ModerationCommandFactory** (13 connections) — `server/utils/command_factories_moderation.py`
- **CombatCommandFactory** (12 connections) — `server/utils/command_factories_combat.py`
- **.__init__()** (9 connections) — `server/utils/command_factories.py`
- **command_factories_combat.py** (7 connections) — `server/utils/command_factories_combat.py`
- **_build_command_factory()** (6 connections) — `server/utils/command_parser.py`
- **_parse_equip_selector()** (5 connections) — `server/utils/command_factories_inventory.py`
- **.create_npc_command()** (4 connections) — `server/utils/command_factories.py`
- **.create_spawn_command()** (4 connections) — `server/utils/command_factories.py`
- **._parse_quantity_from_args()** (4 connections) — `server/utils/command_factories_inventory.py`
- **._parse_index_or_search_term()** (4 connections) — `server/utils/command_factories_inventory.py`
- **_build_command_factory_part1()** (4 connections) — `server/utils/command_parser.py`
- **_build_command_factory_part2()** (4 connections) — `server/utils/command_parser.py`
- **.create_say_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_local_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_system_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_emote_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_me_command()** (3 connections) — `server/utils/command_factories.py`
- *... and 103 more nodes in this community*

## Relationships

- [Server Models](Server_Models.md) (57 shared connections)
- [Server Utils](Server_Utils.md) (20 shared connections)
- [Server Models (4)](Server_Models_%284%29.md) (16 shared connections)
- [Server Commands](Server_Commands.md) (16 shared connections)
- [Server Utils (4)](Server_Utils_%284%29.md) (15 shared connections)
- [Server Models (7)](Server_Models_%287%29.md) (12 shared connections)
- [Server Utils (10)](Server_Utils_%2810%29.md) (12 shared connections)
- [Server Models (8)](Server_Models_%288%29.md) (6 shared connections)
- [Server Models (20)](Server_Models_%2820%29.md) (5 shared connections)
- [Server Game](Server_Game.md) (5 shared connections)
- [Server Models (5)](Server_Models_%285%29.md) (4 shared connections)
- [Server Utils (5)](Server_Utils_%285%29.md) (3 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_combat.py`
- `server/utils/command_factories_inventory.py`
- `server/utils/command_factories_moderation.py`
- `server/utils/command_factories_player_state.py`
- `server/utils/command_factories_utility.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 594 (89%)
- INFERRED: 77 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*