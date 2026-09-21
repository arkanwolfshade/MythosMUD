# .state

> 50 nodes

## Key Concepts

- **.state()** (41 connections) — `server/realtime/connection_state_machine.py`
- **handle_emote_command()** (16 connections) — `server/commands/emote_commands.py`
- **emote_commands.py** (13 connections) — `server/commands/emote_commands.py`
- **handle_system_command()** (9 connections) — `server/commands/system_commands.py`
- **handle_explore_command()** (8 connections) — `server/commands/exploration_commands.py`
- **test_emote_commands.py** (7 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Any** (6 connections)
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **_get_emote_services()** (5 connections) — `server/commands/emote_commands.py`
- **test_exploration_commands.py** (5 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **_extract_emote_action()** (4 connections) — `server/commands/emote_commands.py`
- **_format_emote_messages()** (4 connections) — `server/commands/emote_commands.py`
- **_handle_emote_result()** (4 connections) — `server/commands/emote_commands.py`
- **_validate_player_for_emote()** (4 connections) — `server/commands/emote_commands.py`
- **test_handle_emote_command()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_message()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_predefined_emote()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_explore_command()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_explore_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_system_command()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (4 connections) — `server/tests/unit/commands/test_system_commands.py`
- **asyncio** (4 connections)
- **asyncio** (3 connections)
- *... and 25 more nodes in this community*

## Relationships

- [command_service.py](command_service.py.md) (7 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [GameStateProvider](GameStateProvider.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [utility_commands.py](utility_commands.py.md) (2 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [real_time.py](real_time.py.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (2 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (2 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/system_commands.py`
- `server/realtime/connection_state_machine.py`
- `server/tests/unit/commands/test_emote_commands.py`
- `server/tests/unit/commands/test_exploration_commands.py`
- `server/tests/unit/commands/test_system_commands.py`

## Audit Trail

- EXTRACTED: 88 (69%)
- INFERRED: 39 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*