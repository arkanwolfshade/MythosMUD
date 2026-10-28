# get_cached_player

> 23 nodes · cohesion 0.11

## Key Concepts

- **who_commands.py** (18 connections) — `server/commands/who_commands.py`
- **handle_who_command()** (15 connections) — `server/commands/who_commands.py`
- **filter_players_by_name()** (14 connections) — `server/commands/who_commands.py`
- **filter_online_players()** (10 connections) — `server/commands/who_commands.py`
- **get_players_for_who()** (8 connections) — `server/commands/who_commands.py`
- **Any** (6 connections)
- **test_filter_players_by_name_case_insensitive()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_exact_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_no_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_filter_players_by_name_partial_match()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_get_players_for_who_no_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **test_get_players_for_who_with_filter()** (3 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Who command handlers and utilities for MythosMUD. This module contains the who…** (1 connections) — `server/commands/who_commands.py`
- **Filter players to only those who are online (active within threshold). Args:…** (1 connections) — `server/commands/who_commands.py`
- **Get the list of players to show and the effective filter term. Args:…** (1 connections) — `server/commands/who_commands.py`
- **Filter players by case-insensitive partial name matching. Args: players: List…** (1 connections) — `server/commands/who_commands.py`
- **Handle the who command for listing online players. Args: command_data: Command…** (1 connections) — `server/commands/who_commands.py`
- **Test filtering players with no filter term.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test get_players_for_who without filter.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test get_players_for_who with filter.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filtering players with exact match.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filtering players with partial match.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`
- **Test filtering players is case-insensitive.** (1 connections) — `server/tests/unit/commands/test_who_commands.py`

## Relationships

- [Phase 2: Qualitative Analysis Results](Phase_2-_Qualitative_Analysis_Results.md) (14 shared connections)
- [PlayerCreationService](PlayerCreationService.md) (9 shared connections)
- [NpcDisposition](NpcDisposition.md) (6 shared connections)
- [command_parser.py](command_parser.py.md) (4 shared connections)
- [test_player_event_handlers_utils.py](test_player_event_handlers_utils.py.md) (3 shared connections)
- [HallucinationRng](HallucinationRng.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [RoomRepository](RoomRepository.md) (1 shared connections)

## Source Files

- `server/commands/who_commands.py`
- `server/tests/unit/commands/test_who_commands.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*