# command factories create

> 711 nodes

## Key Concepts

- **BaseCommand** (152 connections) — `server/models/command_base.py`
- **command.py** (98 connections) — `server/models/command.py`
- **CommandType** (85 connections) — `server/models/command_base.py`
- **CommandFactory** (83 connections) — `server/utils/command_factories.py`
- **get_username_from_user()** (53 connections) — `server/utils/command_helpers.py`
- **command_parser.py** (46 connections) — `server/utils/command_parser.py`
- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_command_combat.py** (31 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_command_factories_player_state.py** (27 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_command_helpers.py** (27 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **test_command_base.py** (22 connections) — `server/tests/unit/models/test_command_base.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **command_utility.py** (19 connections) — `server/models/command_utility.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **PlayerStateCommandFactory** (18 connections) — `server/utils/command_factories_player_state.py`
- **command_helpers.py** (18 connections) — `server/utils/command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- *... and 686 more nodes in this community*

## Relationships

- [command inventory models](command_inventory_models.md) (79 shared connections)
- [command communication models](command_communication_models.md) (47 shared connections)
- [command models moderation](command_models_moderation.md) (42 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (40 shared connections)
- [command inventory factories](command_inventory_factories.md) (40 shared connections)
- [Inventory Equip](Inventory_Equip.md) (24 shared connections)
- [commands admin mute](commands_admin_mute.md) (14 shared connections)
- [feature services flag](feature_services_flag.md) (11 shared connections)
- [command parser rationale](command_parser_rationale.md) (6 shared connections)
- [commands who helpers](commands_who_helpers.md) (6 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [target resolution service](target_resolution_service.md) (4 shared connections)

## Source Files

- `server/models/command.py`
- `server/models/command_admin.py`
- `server/models/command_alias.py`
- `server/models/command_base.py`
- `server/models/command_channel.py`
- `server/models/command_combat.py`
- `server/models/command_exploration.py`
- `server/models/command_follow.py`
- `server/models/command_moderation.py`
- `server/models/command_party.py`
- `server/models/command_player_state.py`
- `server/models/command_utility.py`
- `server/tests/unit/models/test_command_admin.py`
- `server/tests/unit/models/test_command_base.py`
- `server/tests/unit/models/test_command_combat.py`
- `server/tests/unit/models/test_command_exploration.py`
- `server/tests/unit/models/test_command_player_state.py`
- `server/tests/unit/models/test_command_utility.py`
- `server/tests/unit/utils/test_command_factories_combat.py`
- `server/tests/unit/utils/test_command_factories_player_state.py`

## Audit Trail

- EXTRACTED: 2439 (89%)
- INFERRED: 316 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*