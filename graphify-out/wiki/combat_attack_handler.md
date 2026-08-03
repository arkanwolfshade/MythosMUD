# combat attack handler

> 24 nodes

## Key Concepts

- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_command()** (16 connections) — `server/commands/npc_admin/router.py`
- **monitoring.py** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_population_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_zone_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_status_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **_resolve_npc_command_player()** (5 connections) — `server/commands/npc_admin/router.py`
- **Any** (5 connections)
- **_extract_npc_subcommand()** (5 connections) — `server/commands/npc_admin/router.py`
- **_invoke_npc_handler()** (5 connections) — `server/commands/npc_admin/router.py`
- **_get_npc_help()** (4 connections) — `server/commands/npc_admin/router.py`
- **Any** (3 connections)
- **NPC monitoring commands (population, zone, status).** (1 connections) — `server/commands/npc_admin/monitoring.py`
- **Handle NPC population stats command.** (1 connections) — `server/commands/npc_admin/monitoring.py`
- **Handle NPC zone stats command.** (1 connections) — `server/commands/npc_admin/monitoring.py`
- **Handle NPC system status command.** (1 connections) — `server/commands/npc_admin/monitoring.py`
- **NPC admin command router and permission validation.** (1 connections) — `server/commands/npc_admin/router.py`
- **Resolve player for NPC command. Returns (player_obj, error).     If error is set** (1 connections) — `server/commands/npc_admin/router.py`
- **Get NPC admin command help text.** (1 connections) — `server/commands/npc_admin/router.py`
- **Extract subcommand and normalize args. Returns (subcommand, args, help_result).** (1 connections) — `server/commands/npc_admin/router.py`
- **Build subcommand to handler mapping. Lazy imports avoid circular dependencies.** (1 connections) — `server/commands/npc_admin/router.py`
- **Invoke the handler for the given subcommand.** (1 connections) — `server/commands/npc_admin/router.py`
- **Handle the main NPC admin command with subcommand routing.      Args:         co** (1 connections) — `server/commands/npc_admin/router.py`

## Relationships

- [npc commands admin](npc_commands_admin.md) (14 shared connections)
- [container schemas containers](container_schemas_containers.md) (10 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (9 shared connections)
- [commands npc admin](commands_npc_admin.md) (8 shared connections)
- [item models rationale](item_models_rationale.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [help content websocket](help_content_websocket.md) (2 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`

## Audit Trail

- EXTRACTED: 116 (82%)
- INFERRED: 26 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*