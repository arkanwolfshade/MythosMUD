# PlayerCreationService

> 19 nodes · cohesion 0.11

## Key Concepts

- **asyncio** (9 connections)
- **test_handle_who_command_error_handling()** (5 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_all_online()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_invalid_last_active()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_no_last_active()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_some_offline()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_no_players()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_success()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_with_filter()** (4 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filter_online_players with all players online.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filter_online_players with some players offline.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filter_online_players with players without last_active.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test handle_who_command when persistence is not available.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test handle_who_command when no players are found.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test handle_who_command successful execution.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test handle_who_command with filter term.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test handle_who_command handles exceptions gracefully.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filter_online_players() handles invalid last_active.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`

## Relationships

- [get_cached_player](get_cached_player.md) (9 shared connections)
- [Phase 2: Qualitative Analysis Results](Phase_2-_Qualitative_Analysis_Results.md) (9 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 36 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*