# dialogue definition persistence

> 90 nodes

## Key Concepts

- **command.py** (98 connections) — `server/models/command.py`
- **CommandType** (85 connections) — `server/models/command_base.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_utility.py** (19 connections) — `server/models/command_utility.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
- **command_combat.py** (14 connections) — `server/models/command_combat.py`
- **HelpCommand** (13 connections) — `server/models/command_utility.py`
- **WhoCommand** (13 connections) — `server/models/command_utility.py`
- **command_magic.py** (10 connections) — `server/models/command_magic.py`
- **command_follow.py** (8 connections) — `server/models/command_follow.py`
- **SpellsCommand** (8 connections) — `server/models/command_magic.py`
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
- **command_party.py** (6 connections) — `server/models/command_party.py`
- **PartyCommand** (6 connections) — `server/models/command_party.py`
- **RestCommand** (6 connections) — `server/models/command_player_state.py`
- *... and 65 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (29 shared connections)
- [command communication models](command_communication_models.md) (19 shared connections)
- [health models rationale](health_models_rationale.md) (18 shared connections)
- [inventory commands command](inventory_commands_command.md) (17 shared connections)
- [npc commands admin](npc_commands_admin.md) (17 shared connections)
- [world models rationale](world_models_rationale.md) (16 shared connections)
- [commands who helpers](commands_who_helpers.md) (13 shared connections)
- [room service sync](room_service_sync.md) (12 shared connections)
- [game models stats](game_models_stats.md) (12 shared connections)
- [command processor rationale](command_processor_rationale.md) (10 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (10 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (9 shared connections)

## Source Files

- `server/models/command.py`
- `server/models/command_admin.py`
- `server/models/command_base.py`
- `server/models/command_channel.py`
- `server/models/command_combat.py`
- `server/models/command_follow.py`
- `server/models/command_magic.py`
- `server/models/command_party.py`
- `server/models/command_player_state.py`
- `server/models/command_utility.py`
- `server/tests/unit/models/test_command_utility.py`
- `server/utils/command_factories_player_state.py`

## Audit Trail

- EXTRACTED: 427 (80%)
- INFERRED: 105 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*