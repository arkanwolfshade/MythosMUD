# commands emote rationale

> 62 nodes

## Key Concepts

- **.state()** (36 connections) — `server/realtime/connection_state_machine.py`
- **emote_commands.py** (14 connections) — `server/commands/emote_commands.py`
- **handle_emote_command()** (14 connections) — `server/commands/emote_commands.py`
- **handle_time_command()** (13 connections) — `server/commands/time_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **handle_explore_command()** (8 connections) — `server/commands/exploration_commands.py`
- **test_time_commands.py** (8 connections) — `server/tests/unit/commands/test_time_commands.py`
- **_get_emote_services()** (7 connections) — `server/commands/emote_commands.py`
- **test_emote_commands.py** (6 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **Any** (5 connections)
- **test_exploration_commands.py** (5 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **_extract_emote_action()** (4 connections) — `server/commands/emote_commands.py`
- **_validate_player_for_emote()** (4 connections) — `server/commands/emote_commands.py`
- **_format_emote_messages()** (4 connections) — `server/commands/emote_commands.py`
- **_handle_emote_result()** (4 connections) — `server/commands/emote_commands.py`
- **test_handle_emote_command()** (3 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_message()** (3 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_explore_command()** (3 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_explore_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_system_command()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- *... and 37 more nodes in this community*

## Relationships

- [commands npc admin](commands_npc_admin.md) (6 shared connections)
- [commands whisper command](commands_whisper_command.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [commands who rationale](commands_who_rationale.md) (4 shared connections)
- [services nats service](services_nats_service.md) (3 shared connections)
- [nats services metrics](nats_services_metrics.md) (3 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (2 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (2 shared connections)
- [connection realtime statistics](connection_realtime_statistics.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [combat commands handler](combat_commands_handler.md) (2 shared connections)
- [commands communication flows](commands_communication_flows.md) (2 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/system_commands.py`
- `server/commands/time_commands.py`
- `server/realtime/connection_state_machine.py`
- `server/tests/unit/commands/test_emote_commands.py`
- `server/tests/unit/commands/test_exploration_commands.py`
- `server/tests/unit/commands/test_system_commands.py`
- `server/tests/unit/commands/test_time_commands.py`

## Audit Trail

- EXTRACTED: 190 (83%)
- INFERRED: 40 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*