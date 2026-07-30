# Any

> 21 nodes

## Key Concepts

- **handle_npc_command()** (17 connections) — `server/commands/npc_admin/router.py`
- **_resolve_npc_command_player()** (5 connections) — `server/commands/npc_admin/router.py`
- **Any** (5 connections)
- **_extract_npc_subcommand()** (5 connections) — `server/commands/npc_admin/router.py`
- **_invoke_npc_handler()** (5 connections) — `server/commands/npc_admin/router.py`
- **test_handle_npc_command_no_player_service()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_no_permission()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_spawn_command_regression_routing_via_npc_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_unknown_subcommand()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Resolve player for NPC command. Returns (player_obj, error).     If error is set** (1 connections) — `server/commands/npc_admin/router.py`
- **Extract subcommand and normalize args. Returns (subcommand, args, help_result).** (1 connections) — `server/commands/npc_admin/router.py`
- **Invoke the handler for the given subcommand.** (1 connections) — `server/commands/npc_admin/router.py`
- **Handle the main NPC admin command with subcommand routing.      Args:         co** (1 connections) — `server/commands/npc_admin/router.py`
- **Test handle_npc_command() when player service is not available.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() when player is not found.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() when player lacks admin permission.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() with no arguments.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Regression: Ensure /spawn (npc spawn) command is reachable and not removed.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() with unknown subcommand.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`

## Relationships

- [Any](Any.md) (9 shared connections)
- [NATSMetrics](NATSMetrics.md) (7 shared connections)
- [test magic commands](test_magic_commands.md) (2 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/router.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 52 (80%)
- INFERRED: 13 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*