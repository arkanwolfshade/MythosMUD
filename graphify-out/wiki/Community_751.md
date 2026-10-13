# Community 751

> 22 nodes

## Key Concepts

- **handle_help_command()** (15 connections) — `server/commands/system_commands.py`
- **test_help_commands.py** (14 connections) — `server/tests/unit/commands/test_help_commands.py`
- **_text()** (6 connections) — `server/tests/unit/commands/test_help_commands.py`
- **asyncio** (6 connections)
- **test_handle_help_command_hides_admin_commands_from_players()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_no_topic()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_positional_arg_fallback()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_unknown_topic()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_with_topic()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_too_many_args()** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **help_commands.py** (4 connections) — `server/commands/help_commands.py`
- **_help_topic()** (3 connections) — `server/commands/system_commands.py`
- **Help command adapter module. The original help command handler lives in…** (1 connections) — `server/commands/help_commands.py`
- **Topic from the validated command's ``topic`` field, falling back to the first…** (1 connections) — `server/commands/system_commands.py`
- **Handle the help command: ``help`` lists topics, ``help <command|alias|guide>``…** (1 connections) — `server/commands/system_commands.py`
- **Unit tests for help command handlers. Tests the help command functionality,…** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **With no topic, help lists the topics and flags the result as HTML.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **The validated command's topic field selects one entry, not the general listing.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **Callers that only supply args still reach the entry.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **An unknown topic is reported as not found.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **More than one argument is a usage error.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **npc is documented for admins only.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Assist Wiring Tests](Assist_Wiring_Tests.md) (4 shared connections)
- [Community 42](Community_42.md) (2 shared connections)
- [Community 390](Community_390.md) (1 shared connections)
- [Community 179](Community_179.md) (1 shared connections)
- [Channel Commands](Channel_Commands.md) (1 shared connections)

## Source Files

- `server/commands/help_commands.py`
- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_help_commands.py`

## Audit Trail

- EXTRACTED: 43 (86%)
- INFERRED: 7 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*