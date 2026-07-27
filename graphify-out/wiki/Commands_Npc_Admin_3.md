# Commands Npc Admin

> 22 nodes · cohesion 0.13

## Key Concepts

- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_command()** (16 connections) — `server/commands/npc_admin/router.py`
- **_extract_npc_subcommand()** (5 connections) — `server/commands/npc_admin/router.py`
- **_invoke_npc_handler()** (5 connections) — `server/commands/npc_admin/router.py`
- **_resolve_npc_command_player()** (5 connections) — `server/commands/npc_admin/router.py`
- **Any** (5 connections) — `server/commands/npc_admin/router.py`
- **_build_subcommand_map()** (4 connections) — `server/commands/npc_admin/router.py`
- **test_handle_npc_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_unknown_subcommand()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_spawn_command_regression_routing_via_npc_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **_get_npc_help()** (3 connections) — `server/commands/npc_admin/router.py`
- **Test handle_npc_command() when player is not found.** (2 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **AliasStorage** (2 connections) — `server/commands/npc_admin/router.py`
- **Regression: Ensure /spawn (npc spawn) command is reachable and not removed.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() with unknown subcommand.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **NPC admin command router and permission validation.** (1 connections) — `server/commands/npc_admin/router.py`
- **Extract subcommand and normalize args. Returns (subcommand, args, help_result).** (1 connections) — `server/commands/npc_admin/router.py`
- **Build subcommand to handler mapping. Lazy imports avoid circular dependencies.** (1 connections) — `server/commands/npc_admin/router.py`
- **Invoke the handler for the given subcommand.** (1 connections) — `server/commands/npc_admin/router.py`
- **Handle the main NPC admin command with subcommand routing.      Args:         co** (1 connections) — `server/commands/npc_admin/router.py`
- **Resolve player for NPC command. Returns (player_obj, error).     If error is set** (1 connections) — `server/commands/npc_admin/router.py`
- **Get NPC admin command help text.** (1 connections) — `server/commands/npc_admin/router.py`

## Relationships

- [[NPC Admin Commands]] (13 shared connections)
- [[Commands Npc Admin]] (12 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Communication Command Handlers]] (1 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Player Domain Model]] (1 shared connections)
- [[Commands Admin Shutdown]] (1 shared connections)

## Source Files

- `server/commands/npc_admin/router.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 86 (91%)
- INFERRED: 9 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
