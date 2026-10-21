# Communities (10 total, 2 thin omitted)

> 20 nodes · cohesion 0.18

## Key Concepts

- **handle_help_command()** (16 connections) — `server/commands/system_commands.py`
- **test_help_commands.py** (16 connections) — `server/tests/unit/commands/test_help_commands.py`
- **asyncio** (6 connections)
- **_text()** (6 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_hides_admin_commands_from_players()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_no_topic()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_positional_arg_fallback()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_too_many_args()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_unknown_topic()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_with_topic()** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **help_commands.py** (4 connections) — `server/commands/help_commands.py`
- **Help command adapter module. The original help command handler lives in…** (1 connections) — `server/commands/help_commands.py`
- **Handle the help command: ``help`` lists topics, ``help <command|alias|guide>``…** (1 connections) — `server/commands/system_commands.py`
- **Unit tests for help command handlers. Tests the help command functionality,…** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **With no topic, help lists the topics and flags the result as HTML.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **The validated command's topic field selects one entry, not the general listing.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **Callers that only supply args still reach the entry.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **An unknown topic is reported as not found.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **More than one argument is a usage error.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`
- **npc is documented for admins only.** (1 connections) — `server/tests/unit/commands/test_help_commands.py`

## Relationships

- [command_parser.py](command_parser.py.md) (7 shared connections)
- [CommandFactory](CommandFactory.md) (5 shared connections)
- [look_container.py](look_container.py.md) (3 shared connections)
- [properties](properties.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)

## Source Files

- `server/commands/help_commands.py`
- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_help_commands.py`

## Audit Trail

- EXTRACTED: 44 (85%)
- INFERRED: 8 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*