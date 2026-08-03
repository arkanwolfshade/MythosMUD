# container persistence rationale

> 94 nodes

## Key Concepts

- **command.py** (98 connections) — `server/models/command.py`
- **CommandType** (85 connections) — `server/models/command_base.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_utility.py** (19 connections) — `server/models/command_utility.py`
- **command_moderation.py** (16 connections) — `server/models/command_moderation.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
- **command_combat.py** (14 connections) — `server/models/command_combat.py`
- **command_inventory.py** (13 connections) — `server/models/command_inventory.py`
- **HelpCommand** (13 connections) — `server/models/command_utility.py`
- **WhoCommand** (13 connections) — `server/models/command_utility.py`
- **command_exploration.py** (9 connections) — `server/models/command_exploration.py`
- **command_follow.py** (8 connections) — `server/models/command_follow.py`
- **InventoryCommand** (8 connections) — `server/models/command_inventory.py`
- **MutesCommand** (8 connections) — `server/models/command_moderation.py`
- **StatusCommand** (8 connections) — `server/models/command_utility.py`
- **TimeCommand** (8 connections) — `server/models/command_utility.py`
- **WhoamiCommand** (8 connections) — `server/models/command_utility.py`
- **TauntCommand** (7 connections) — `server/models/command_combat.py`
- **command_channel.py** (6 connections) — `server/models/command_channel.py`
- **ChannelCommand** (6 connections) — `server/models/command_channel.py`
- **FleeCommand** (6 connections) — `server/models/command_combat.py`
- **FollowCommand** (6 connections) — `server/models/command_follow.py`
- **UnfollowCommand** (6 connections) — `server/models/command_follow.py`
- **FollowingCommand** (6 connections) — `server/models/command_follow.py`
- *... and 69 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (32 shared connections)
- [npc commands admin](npc_commands_admin.md) (21 shared connections)
- [command models moderation](command_models_moderation.md) (21 shared connections)
- [command communication models](command_communication_models.md) (19 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (17 shared connections)
- [calendar schemas validate](calendar_schemas_validate.md) (16 shared connections)
- [commands who helpers](commands_who_helpers.md) (15 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (13 shared connections)
- [combat attack handler](combat_attack_handler.md) (11 shared connections)
- [game chat service](game_chat_service.md) (11 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (11 shared connections)
- [feature services flag](feature_services_flag.md) (9 shared connections)

## Source Files

- `server/models/command.py`
- `server/models/command_admin.py`
- `server/models/command_base.py`
- `server/models/command_channel.py`
- `server/models/command_combat.py`
- `server/models/command_exploration.py`
- `server/models/command_follow.py`
- `server/models/command_inventory.py`
- `server/models/command_moderation.py`
- `server/models/command_party.py`
- `server/models/command_player_state.py`
- `server/models/command_utility.py`
- `server/tests/unit/models/test_command_utility.py`
- `server/utils/command_factories_player_state.py`

## Audit Trail

- EXTRACTED: 460 (81%)
- INFERRED: 107 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*