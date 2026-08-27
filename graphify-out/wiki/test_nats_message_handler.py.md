# test_nats_message_handler.py

> 108 nodes

## Key Concepts

- **test_who_commands.py** (48 connections) — `server/tests/unit/commands/test_who_commands.py`
- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **who_commands.py** (16 connections) — `server/commands/who_commands.py`
- **filter_players_by_name()** (14 connections) — `server/commands/who_commands.py`
- **handle_who_command()** (14 connections) — `server/commands/who_commands.py`
- **parse_last_active_datetime()** (14 connections) — `server/commands/who_commands.py`
- **format_player_entry()** (13 connections) — `server/commands/who_commands.py`
- **format_player_location()** (13 connections) — `server/commands/who_commands.py`
- **test_who_commands_helpers.py** (12 connections) — `server/tests/unit/commands/test_who_commands_helpers.py`
- **filter_online_players()** (10 connections) — `server/commands/who_commands.py`
- **format_who_result()** (10 connections) — `server/commands/who_commands.py`
- **asyncio** (9 connections)
- **get_players_for_who()** (8 connections) — `server/commands/who_commands.py`
- **Any** (6 connections)
- **Test parse_last_active_datetime with None.** (5 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_all_online()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_invalid_last_active()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_no_last_active()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_some_offline()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_player_entry_error_handling()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_no_players()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_success()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_with_filter()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- *... and 83 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [asyncio](asyncio.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [_get_npc_room_id](_get_npc_room_id.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [MPRegenerationService](MPRegenerationService.md) (1 shared connections)
- [enum](enum.md) (1 shared connections)

## Source Files

- `server/commands/utility_commands.py`
- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`
- `server/tests/unit/commands/test_who_commands_helpers.py`

## Audit Trail

- EXTRACTED: 211 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*