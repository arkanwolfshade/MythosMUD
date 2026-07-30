# Spell Targeting

> 978 nodes

## Key Concepts

- **BaseCommand** (150 connections) — `server/models/command_base.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **command.py** (96 connections) — `server/models/command.py`
- **CommandType** (84 connections) — `server/models/command_base.py`
- **CommandFactory** (82 connections) — `server/utils/command_factories.py`
- **test_command_factories_exploration.py** (48 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_command_communication.py** (45 connections) — `server/tests/unit/models/test_command_communication.py`
- **command_parser.py** (45 connections) — `server/utils/command_parser.py`
- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_command_moderation.py** (38 connections) — `server/tests/unit/models/test_command_moderation.py`
- **test_command_combat.py** (31 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_command_magic.py** (27 connections) — `server/tests/unit/models/test_command_magic.py`
- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **CastCommand** (20 connections) — `server/models/command_magic.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **command_communication.py** (19 connections) — `server/models/command_communication.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- *... and 953 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (113 shared connections)
- [.validate topic()](validate_topic%28%29.md) (49 shared connections)
- [world](world.md) (45 shared connections)
- [test command factories utility](test_command_factories_utility.md) (41 shared connections)
- [.validate search term()](validate_search_term%28%29.md) (33 shared connections)
- [test command service](test_command_service.md) (25 shared connections)
- [connection delegates](connection_delegates.md) (20 shared connections)
- [test command parser helpers](test_command_parser_helpers.md) (19 shared connections)
- [Player](Player.md) (14 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (11 shared connections)
- [as event data dict()](as_event_data_dict%28%29.md) (10 shared connections)
- [Player Position Service](Player_Position_Service.md) (10 shared connections)

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
- `server/tests/unit/models/test_command_admin.py`
- `server/tests/unit/models/test_command_alias.py`
- `server/tests/unit/models/test_command_combat.py`
- `server/tests/unit/models/test_command_communication.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 3477 (90%)
- INFERRED: 368 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*