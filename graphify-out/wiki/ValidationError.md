# ValidationError

> 1375 nodes

## Key Concepts

- **ValidationError** (330 connections) — `server/exceptions.py`
- **BaseCommand** (152 connections) — `server/models/command_base.py`
- **pydantic.md** (117 connections) — `.claude/rules/pydantic.md`
- **command.py** (98 connections) — `server/models/command.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **CommandType** (96 connections) — `server/models/command_base.py`
- **CommandFactory** (83 connections) — `server/utils/command_factories.py`
- **UtilityCommandFactory** (65 connections) — `server/utils/command_factories_utility.py`
- **ExplorationCommandFactory** (59 connections) — `server/utils/command_factories_exploration.py`
- **test_command_factories_utility.py** (52 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_command_factories_exploration.py** (49 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_command_communication.py** (47 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_command_parser.py** (47 connections) — `server/tests/unit/utils/test_command_parser.py`
- **command_parser.py** (47 connections) — `server/utils/command_parser.py`
- **test_command_admin.py** (44 connections) — `server/tests/unit/models/test_command_admin.py`
- **PlayerStateCommandFactory** (40 connections) — `server/utils/command_factories_player_state.py`
- **test_command_moderation.py** (40 connections) — `server/tests/unit/models/test_command_moderation.py`
- **CommunicationCommandFactory** (39 connections) — `server/utils/command_factories_communication.py`
- **ModerationCommandFactory** (37 connections) — `server/utils/command_factories_moderation.py`
- **security_validator.py** (36 connections) — `server/validators/security_validator.py`
- **test_command_combat.py** (33 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_command_factories_communication.py** (30 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_factories_moderation.py** (30 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_command_magic.py** (29 connections) — `server/tests/unit/models/test_command_magic.py`
- **Direction** (28 connections) — `server/models/command_base.py`
- *... and 1350 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (83 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (69 shared connections)
- [test_command_inventory.py](test_command_inventory.py.md) (34 shared connections)
- [test_player_service_mutations.py](test_player_service_mutations.py.md) (24 shared connections)
- [DatabaseManager](DatabaseManager.md) (23 shared connections)
- [ErrorType](ErrorType.md) (17 shared connections)
- [pytest.md](pytest.md.md) (17 shared connections)
- [get_username_from_user](get_username_from_user.md) (13 shared connections)
- [InventoryCommandFactory](InventoryCommandFactory.md) (13 shared connections)
- [MythosMUDError](MythosMUDError.md) (12 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (12 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (11 shared connections)

## Source Files

- `.claude/rules/pydantic.md`
- `server/exceptions.py`
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
- `server/tests/unit/models/test_command_base.py`

## Audit Trail

- EXTRACTED: 2708 (85%)
- INFERRED: 486 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*