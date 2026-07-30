# Spell Targeting

> 772 nodes

## Key Concepts

- **BaseCommand** (150 connections) — `server/models/command_base.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **command.py** (96 connections) — `server/models/command.py`
- **CommandType** (84 connections) — `server/models/command_base.py`
- **CommandFactory** (82 connections) — `server/utils/command_factories.py`
- **test_command_factories_inventory.py** (48 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **command_parser.py** (45 connections) — `server/utils/command_parser.py`
- **test_command_moderation.py** (38 connections) — `server/tests/unit/models/test_command_moderation.py`
- **security_validator.py** (34 connections) — `server/validators/security_validator.py`
- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **validate_player_name()** (23 connections) — `server/validators/security_validator.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **CastCommand** (20 connections) — `server/models/command_magic.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **command_communication.py** (19 connections) — `server/models/command_communication.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **MuteCommand** (18 connections) — `server/models/command_moderation.py`
- **command_utility.py** (18 connections) — `server/models/command_utility.py`
- *... and 747 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (191 shared connections)
- [.validate topic()](validate_topic%28%29.md) (64 shared connections)
- [test command factories utility](test_command_factories_utility.md) (41 shared connections)
- [.validate search term()](validate_search_term%28%29.md) (34 shared connections)
- [connection helpers](connection_helpers.md) (33 shared connections)
- [test command factories exploration](test_command_factories_exploration.md) (31 shared connections)
- [.validate target()](validate_target%28%29.md) (30 shared connections)
- [test room sync service](test_room_sync_service.md) (24 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (24 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (22 shared connections)
- [test command parser helpers](test_command_parser_helpers.md) (16 shared connections)
- [real time](real_time.md) (14 shared connections)

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
- `server/tests/unit/models/test_command_exploration.py`
- `server/tests/unit/models/test_command_moderation.py`
- `server/tests/unit/models/test_command_player_state.py`
- `server/tests/unit/models/test_command_utility.py`

## Audit Trail

- EXTRACTED: 3097 (90%)
- INFERRED: 330 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*