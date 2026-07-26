# BaseCommand

> 691 nodes · cohesion 0.01

## Key Concepts

- **BaseCommand** (150 connections) — `server/models/command_base.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **command.py** (96 connections) — `server/models/command.py`
- **CommandType** (84 connections) — `server/models/command_base.py`
- **CommandFactory** (82 connections) — `server/utils/command_factories.py`
- **test_command_parser.py** (45 connections) — `server/tests/unit/utils/test_command_parser.py`
- **command_parser.py** (45 connections) — `server/utils/command_parser.py`
- **test_command_factories_player_state.py** (27 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **command_communication.py** (19 connections) — `server/models/command_communication.py`
- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **command_utility.py** (18 connections) — `server/models/command_utility.py`
- **test_command_alias.py** (18 connections) — `server/tests/unit/models/test_command_alias.py`
- **AliasCommand** (17 connections) — `server/models/command_alias.py`
- **ExplorationCommandFactory** (17 connections) — `server/utils/command_factories_exploration.py`
- **PlayerStateCommandFactory** (17 connections) — `server/utils/command_factories_player_state.py`
- **command_moderation.py** (16 connections) — `server/models/command_moderation.py`
- **InventoryCommandFactory** (16 connections) — `server/utils/command_factories_inventory.py`
- **MuteGlobalCommand** (15 connections) — `server/models/command_moderation.py`
- *... and 666 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (117 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (44 shared connections)
- [test_command_factories_utility.py](test_command_factories_utility.py.md) (35 shared connections)
- [test_command_inventory.py](test_command_inventory.py.md) (33 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (30 shared connections)
- [test_command_factories_exploration.py](test_command_factories_exploration.py.md) (30 shared connections)
- [test_command_combat.py](test_command_combat.py.md) (29 shared connections)
- [test_command_moderation.py](test_command_moderation.py.md) (27 shared connections)
- [test_command_factories_inventory.py](test_command_factories_inventory.py.md) (27 shared connections)
- [exceptions.py](exceptions.py.md) (27 shared connections)
- [test_command_factories_moderation.py](test_command_factories_moderation.py.md) (22 shared connections)
- [get_logger](get_logger.md) (19 shared connections)

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
- `server/tests/unit/models/test_command_alias.py`
- `server/tests/unit/models/test_command_player_state.py`
- `server/tests/unit/models/test_command_utility.py`
- `server/tests/unit/test_command_parser_smoke.py`
- `server/tests/unit/utils/test_command_factories_combat.py`

## Audit Trail

- EXTRACTED: 2688 (90%)
- INFERRED: 286 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*