# ContainerComponent

> 248 nodes · cohesion 0.02

## Key Concepts

- **BaseCommand** (176 connections) — `server/models/command_base.py`
- **CommandType** (113 connections) — `server/models/command_base.py`
- **command.py** (112 connections) — `server/models/command.py`
- **command_base.py** (28 connections) — `server/models/command_base.py`
- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_command_base.py** (22 connections) — `server/tests/unit/models/test_command_base.py`
- **command_communication.py** (20 connections) — `server/models/command_communication.py`
- **command_utility.py** (20 connections) — `server/models/command_utility.py`
- **test_command_utility.py** (20 connections) — `server/tests/unit/models/test_command_utility.py`
- **command_combat.py** (16 connections) — `server/models/command_combat.py`
- **command_moderation.py** (16 connections) — `server/models/command_moderation.py`
- **command_player_state.py** (16 connections) — `server/models/command_player_state.py`
- **MuteGlobalCommand** (15 connections) — `server/models/command_moderation.py`
- **LieCommand** (15 connections) — `server/models/command_player_state.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
- **KickCommand** (14 connections) — `server/models/command_combat.py`
- **PunchCommand** (14 connections) — `server/models/command_combat.py`
- **StrikeCommand** (14 connections) — `server/models/command_combat.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **PoseCommand** (13 connections) — `server/models/command_communication.py`
- **LearnCommand** (13 connections) — `server/models/command_magic.py`
- **SpellCommand** (13 connections) — `server/models/command_magic.py`
- **HelpCommand** (13 connections) — `server/models/command_utility.py`
- **WhoCommand** (13 connections) — `server/models/command_utility.py`
- **GotoCommand** (12 connections) — `server/models/command_admin.py`
- *... and 223 more nodes in this community*

## Relationships

- [NPCCombatIntegration](NPCCombatIntegration.md) (77 shared connections)
- [test_nats_service_pool.py](test_nats_service_pool.py.md) (46 shared connections)
- [test_look_item_helpers.py](test_look_item_helpers.py.md) (34 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (30 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (27 shared connections)
- [LucidityRepository](LucidityRepository.md) (26 shared connections)
- [useMythosAppState.ts](useMythosAppState.ts.md) (26 shared connections)
- [container_query_helpers.py](container_query_helpers.py.md) (23 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (23 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (14 shared connections)
- [EmoteService](EmoteService.md) (13 shared connections)
- [File-by-File Changes](File-by-File_Changes.md) (12 shared connections)

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
- `server/tests/unit/commands/test_command_registry_consistency.py`
- `server/tests/unit/models/test_command_base.py`
- `server/tests/unit/models/test_command_player_state.py`
- `server/tests/unit/models/test_command_utility.py`
- `server/utils/command_factories_player_state.py`

## Audit Trail

- EXTRACTED: 849 (90%)
- INFERRED: 96 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*