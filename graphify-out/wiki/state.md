# .state

> 54 nodes

## Key Concepts

- **.state()** (37 connections) — `server/realtime/connection_state_machine.py`
- **handle_emote_command()** (16 connections) — `server/commands/emote_commands.py`
- **handle_time_command()** (14 connections) — `server/commands/time_commands.py`
- **emote_commands.py** (13 connections) — `server/commands/emote_commands.py`
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **handle_explore_command()** (9 connections) — `server/commands/exploration_commands.py`
- **test_emote_commands.py** (8 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Any** (6 connections)
- **test_exploration_commands.py** (6 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **_get_emote_services()** (5 connections) — `server/commands/emote_commands.py`
- **asyncio** (5 connections)
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
- **test_handle_time_command_holiday_service_error()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holiday_service()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holidays()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_success()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- *... and 29 more nodes in this community*

## Relationships

- [server/schemas/__init__.py](server-schemas-__init__.py.md) (8 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (3 shared connections)
- [command_service.py](command_service.py.md) (3 shared connections)
- [test_game_state_provider.py](test_game_state_provider.py.md) (3 shared connections)
- [real_time.py](real_time.py.md) (2 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (2 shared connections)
- [server/commands/__init__.py](server-commands-__init__.py.md) (2 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [server/config/__init__.py](server-config-__init__.py.md) (2 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/time_commands.py`
- `server/realtime/connection_state_machine.py`
- `server/tests/unit/commands/test_emote_commands.py`
- `server/tests/unit/commands/test_exploration_commands.py`
- `server/tests/unit/commands/test_time_commands.py`

## Audit Trail

- EXTRACTED: 106 (74%)
- INFERRED: 37 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*