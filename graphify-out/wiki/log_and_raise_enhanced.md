# log_and_raise_enhanced

> 221 nodes

## Key Concepts

- **log_and_raise_enhanced()** (113 connections) — `server/utils/enhanced_error_logging.py`
- **CommunicationCommandFactory** (42 connections) — `server/utils/command_factories_communication.py`
- **ModerationCommandFactory** (37 connections) — `server/utils/command_factories_moderation.py`
- **test_command_factories_communication.py** (31 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **CombatCommandFactory** (29 connections) — `server/utils/command_factories_combat.py`
- **test_command_factories_moderation.py** (29 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **command_factories.py** (21 connections) — `server/utils/command_factories.py`
- **test_command_factories_combat.py** (14 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **command_factories_communication.py** (11 connections) — `server/utils/command_factories_communication.py`
- **command_factories_exploration.py** (11 connections) — `server/utils/command_factories_exploration.py`
- **command_factories_moderation.py** (11 connections) — `server/utils/command_factories_moderation.py`
- **command_factories_player_state.py** (11 connections) — `server/utils/command_factories_player_state.py`
- **command_factories_utility.py** (11 connections) — `server/utils/command_factories_utility.py`
- **.__init__()** (9 connections) — `server/utils/command_factories.py`
- **.create_mute_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_mute_global_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **command_factories_combat.py** (9 connections) — `server/utils/command_factories_combat.py`
- **.create_channel_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_local_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.create_add_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_global_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- *... and 196 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (52 shared connections)
- [get_logger](get_logger.md) (51 shared connections)
- [BaseCommand](BaseCommand.md) (33 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (14 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (13 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (13 shared connections)
- [command_parser.py](command_parser.py.md) (11 shared connections)
- [CommandFactory](CommandFactory.md) (5 shared connections)
- [PlayerRespawnWrapper](PlayerRespawnWrapper.md) (5 shared connections)
- [PlayerCreationService](PlayerCreationService.md) (3 shared connections)
- [CorruptionService](CorruptionService.md) (1 shared connections)
- [test_command_communication.py](test_command_communication.py.md) (1 shared connections)

## Source Files

- `server/game/player_state_service.py`
- `server/tests/unit/commands/test_assist_wiring.py`
- `server/tests/unit/commands/test_protect_wiring.py`
- `server/tests/unit/utils/test_command_factories_combat.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_combat.py`
- `server/utils/command_factories_communication.py`
- `server/utils/command_factories_exploration.py`
- `server/utils/command_factories_moderation.py`
- `server/utils/command_factories_player_state.py`
- `server/utils/command_factories_utility.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 501 (84%)
- INFERRED: 93 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*