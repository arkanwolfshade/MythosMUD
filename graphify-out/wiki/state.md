# .state

> 40 nodes

## Key Concepts

- **.state()** (42 connections) — `server/realtime/connection_state_machine.py`
- **handle_emote_command()** (17 connections) — `server/commands/emote_commands.py`
- **emote_commands.py** (17 connections) — `server/commands/emote_commands.py`
- **handle_explore_command()** (9 connections) — `server/commands/exploration_commands.py`
- **test_emote_commands.py** (9 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Any** (6 connections)
- **_get_emote_services()** (5 connections) — `server/commands/emote_commands.py`
- **_handle_emote_result()** (5 connections) — `server/commands/emote_commands.py`
- **_get_ground_services()** (5 connections) — `server/commands/rescue_commands.py`
- **test_handle_emote_command()** (5 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_predefined_emote()** (5 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_exploration_commands.py** (5 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **_extract_emote_action()** (4 connections) — `server/commands/emote_commands.py`
- **_format_emote_messages()** (4 connections) — `server/commands/emote_commands.py`
- **_validate_player_for_emote()** (4 connections) — `server/commands/emote_commands.py`
- **test_handle_emote_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_message()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_explore_command()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_explore_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **asyncio** (4 connections)
- **asyncio** (2 connections)
- **Any** (1 connections)
- **Emote command handlers for MythosMUD. This module contains handlers for the…** (1 connections) — `server/commands/emote_commands.py`
- **Handle the result from chat service after sending emote. Args: result: Result…** (1 connections) — `server/commands/emote_commands.py`
- **Handle the emote command for performing emotes. Args: command_data: Command…** (1 connections) — `server/commands/emote_commands.py`
- *... and 15 more nodes in this community*

## Relationships

- [MessageCategory](MessageCategory.md) (7 shared connections)
- [alias_storage.py](alias_storage.py.md) (6 shared connections)
- [command_error](command_error.md) (4 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (4 shared connections)
- [GameStateProvider](GameStateProvider.md) (4 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)
- [real_time.py](real_time.py.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/rescue_commands.py`
- `server/realtime/connection_state_machine.py`
- `server/tests/unit/commands/test_emote_commands.py`
- `server/tests/unit/commands/test_exploration_commands.py`

## Audit Trail

- EXTRACTED: 81 (66%)
- INFERRED: 42 (34%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*