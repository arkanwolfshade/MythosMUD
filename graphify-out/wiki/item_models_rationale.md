# item models rationale

> 17 nodes

## Key Concepts

- **handle_npc_edit_command()** (10 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_delete_command()** (9 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (9 connections) — `server/commands/npc_admin/definition.py`
- **Any** (7 connections)
- **_parse_npc_edit_args()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_build_npc_edit_params()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_execute_npc_edit()** (5 connections) — `server/commands/npc_admin/definition.py`
- **test_handle_npc_list_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_delete_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Parse and validate NPC edit command args.      Returns:         (npc_id, field,** (1 connections) — `server/commands/npc_admin/definition.py`
- **Map a single NPC field/value into NPCDefinitionUpdateParams, or return an error** (1 connections) — `server/commands/npc_admin/definition.py`
- **Run NPC definition update in DB session. Returns result or error dict.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC editing command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC deletion command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC listing command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Test handle_npc_list_command() lists NPCs.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_delete_command() with no arguments.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (8 shared connections)
- [combat attack handler](combat_attack_handler.md) (6 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (3 shared connections)
- [npc commands admin](npc_commands_admin.md) (3 shared connections)
- [container schemas containers](container_schemas_containers.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [help content websocket](help_content_websocket.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/definition.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 57 (89%)
- INFERRED: 7 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*