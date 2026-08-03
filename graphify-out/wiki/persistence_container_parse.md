# persistence container parse

> 37 nodes

## Key Concepts

- **handle_quest_command()** (20 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (20 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **_enter_quest_command_patches()** (7 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **ExitStack** (5 connections)
- **test_quest_ask_success()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_npc_not_in_room()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_success()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_npc_not_in_room()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_journal_returns_unavailable_when_no_container()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_journal_returns_log_when_available()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_journal_character_not_found()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_usage_when_no_subcommand()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_usage_when_wrong_subcommand()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_usage_when_no_quest_name()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_success()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_abandon_failure_message()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_usage_when_no_npc()** (3 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **current_user()** (2 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Handle quest command subcommands: abandon, ask, turnin.      Usage:       quest** (1 connections) — `server/commands/quest_commands.py`
- **Unit tests for quest commands: journal/quests (quest log) and quest abandon.  Te** (1 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Minimal current_user dict for command handlers.** (1 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Request with app.state.container (set per test).** (1 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Journal returns message when container/persistence not available.** (1 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Journal returns formatted quest log when services available.** (1 connections) — `server/tests/unit/commands/test_quest_commands.py`
- *... and 12 more nodes in this community*

## Relationships

- [commands quest rationale](commands_quest_rationale.md) (11 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (2 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/tests/unit/commands/test_quest_commands.py`

## Audit Trail

- EXTRACTED: 121 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*