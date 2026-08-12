# handle_quest_command

> 39 nodes

## Key Concepts

- **handle_quest_command()** (21 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (20 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **asyncio** (13 connections)
- **_enter_quest_command_patches()** (7 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_npc_not_in_room()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_success()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_npc_not_in_room()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_success()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **ExitStack** (5 connections)
- **test_journal_character_not_found()** (4 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_journal_returns_log_when_available()** (4 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_journal_returns_unavailable_when_no_container()** (4 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_failure_message()** (4 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_success()** (4 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_usage_when_no_quest_name()** (4 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_usage_when_no_subcommand()** (4 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_usage_when_wrong_subcommand()** (4 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_usage_when_no_npc()** (4 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **current_user()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **mock_request()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **fixture** (2 connections)
- **Handle quest command subcommands: abandon, ask, turnin. Usage: quest abandon…** (1 connections) — `server/commands/quest_commands.py`
- **Unit tests for quest commands: journal/quests (quest log) and quest abandon.…** (1 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Journal returns error when character not found.** (1 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Quest command returns usage when args empty or not 'abandon'.** (1 connections) — `server/tests/unit/commands/test_quest_commands.py`
- *... and 14 more nodes in this community*

## Relationships

- [quest_commands.py](quest_commands.py.md) (11 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/tests/unit/commands/test_quest_commands.py`

## Audit Trail

- EXTRACTED: 151 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*