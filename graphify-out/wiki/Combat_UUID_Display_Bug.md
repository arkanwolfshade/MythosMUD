# Combat UUID Display Bug

> 24 nodes

## Key Concepts

- **test_who_commands.py** (47 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_no_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_partial_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_some_offline()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_no_last_active()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_no_players_with_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_with_players()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_no_players()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_success()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_with_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_handle_who_command_error_handling()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Unit tests for who commands.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filtering players with no filter term.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filtering players with exact match.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filtering players with partial match.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filter_online_players with some players offline.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filter_online_players with players without last_active.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_who_result with no players and filter term.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_who_result with players.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test handle_who_command when no players are found.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test handle_who_command successful execution.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test handle_who_command with filter term.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test handle_who_command handles exceptions gracefully.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`

## Relationships

- [Legacy Cleanup Summary](Legacy_Cleanup_Summary.md) (21 shared connections)
- [Combat Disconnect Bug](Combat_Disconnect_Bug.md) (10 shared connections)
- [Exploration Command Factory](Exploration_Command_Factory.md) (6 shared connections)
- [Plan Modernization Archive](Plan_Modernization_Archive.md) (5 shared connections)
- [Plans Gladiator Ring](Plans_Gladiator_Ring.md) (1 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (1 shared connections)
- [E 2 E Ai Execution](E_2_E_Ai_Execution.md) (1 shared connections)
- [E 2 E Timeout Analysis](E_2_E_Timeout_Analysis.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 92 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*