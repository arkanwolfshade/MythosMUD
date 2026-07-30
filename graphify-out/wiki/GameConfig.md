# GameConfig

> 21 nodes

## Key Concepts

- **who_commands.py** (16 connections) — `server/commands/who_commands.py`
- **filter_players_by_name()** (14 connections) — `server/commands/who_commands.py`
- **handle_who_command()** (14 connections) — `server/commands/who_commands.py`
- **filter_online_players()** (10 connections) — `server/commands/who_commands.py`
- **format_who_result()** (10 connections) — `server/commands/who_commands.py`
- **get_players_for_who()** (8 connections) — `server/commands/who_commands.py`
- **Any** (6 connections)
- **test_filter_players_by_name_case_insensitive()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_format_who_result_with_players_and_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_get_players_for_who_with_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_online_players_invalid_last_active()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Who command handlers and utilities for MythosMUD.  This module contains the who** (1 connections) — `server/commands/who_commands.py`
- **Filter players by case-insensitive partial name matching.      Args:         pla** (1 connections) — `server/commands/who_commands.py`
- **Filter players to only those who are online (active within threshold).      Args** (1 connections) — `server/commands/who_commands.py`
- **Format the who command result message.      Args:         players: List of playe** (1 connections) — `server/commands/who_commands.py`
- **Get the list of players to show and the effective filter term.      Args:** (1 connections) — `server/commands/who_commands.py`
- **Handle the who command for listing online players.      Args:         command_da** (1 connections) — `server/commands/who_commands.py`
- **Test filtering players is case-insensitive.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test format_who_result with players and filter term.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test get_players_for_who with filter.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filter_online_players() handles invalid last_active.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`

## Relationships

- [utility commands](utility_commands.md) (21 shared connections)
- [Any](Any.md) (5 shared connections)
- [disconnect player connections()](disconnect_player_connections%28%29.md) (3 shared connections)
- [AuthenticationBackend](AuthenticationBackend.md) (3 shared connections)
- [test utility commands whoami](test_utility_commands_whoami.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [CharacterNameScreen](CharacterNameScreen.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [Test should echo to sender](Test_should_echo_to_sender.md) (1 shared connections)
- [test_alias_hash_same_name_and_command](test_alias_hash_same_name_and_command.md) (1 shared connections)
- [test_alias_hash_different_name](test_alias_hash_different_name.md) (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 99 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*