# dialogue definition persistence

> 166 nodes

## Key Concepts

- **command.py** (98 connections) — `server/models/command.py`
- **CommandType** (85 connections) — `server/models/command_base.py`
- **security_validator.py** (36 connections) — `server/validators/security_validator.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_communication.py** (19 connections) — `server/models/command_communication.py`
- **command_utility.py** (19 connections) — `server/models/command_utility.py`
- **command_moderation.py** (16 connections) — `server/models/command_moderation.py`
- **command_player_state.py** (15 connections) — `server/models/command_player_state.py`
- **LieCommand** (15 connections) — `server/models/command_player_state.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
- **command_combat.py** (14 connections) — `server/models/command_combat.py`
- **command_inventory.py** (13 connections) — `server/models/command_inventory.py`
- **HelpCommand** (13 connections) — `server/models/command_utility.py`
- **WhoCommand** (13 connections) — `server/models/command_utility.py`
- **command_alias.py** (12 connections) — `server/models/command_alias.py`
- **GroundCommand** (12 connections) — `server/models/command_player_state.py`
- **command_magic.py** (10 connections) — `server/models/command_magic.py`
- **command_exploration.py** (9 connections) — `server/models/command_exploration.py`
- **AliasesCommand** (8 connections) — `server/models/command_alias.py`
- **command_follow.py** (8 connections) — `server/models/command_follow.py`
- **InventoryCommand** (8 connections) — `server/models/command_inventory.py`
- **SpellsCommand** (8 connections) — `server/models/command_magic.py`
- *... and 141 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (56 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (37 shared connections)
- [command communication models](command_communication_models.md) (25 shared connections)
- [inventory commands command](inventory_commands_command.md) (24 shared connections)
- [npc commands admin](npc_commands_admin.md) (21 shared connections)
- [health models rationale](health_models_rationale.md) (21 shared connections)
- [Inventory Equip](Inventory_Equip.md) (20 shared connections)
- [commands who helpers](commands_who_helpers.md) (13 shared connections)
- [room service sync](room_service_sync.md) (13 shared connections)
- [game models stats](game_models_stats.md) (12 shared connections)
- [command processor rationale](command_processor_rationale.md) (11 shared connections)
- [add used user](add_used_user.md) (9 shared connections)

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
- `server/tests/unit/models/test_command_player_state.py`
- `server/tests/unit/models/test_command_utility.py`
- `server/tests/unit/utils/test_command_factories_player_state.py`
- `server/utils/command_factories_player_state.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 737 (84%)
- INFERRED: 145 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*