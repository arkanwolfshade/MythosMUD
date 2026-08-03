# help content websocket

> 8 nodes

## Key Concepts

- **handle_npc_create_command()** (12 connections) — `server/commands/npc_admin/definition.py`
- **test_handle_npc_create_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_create_command_invalid_type()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_create_command_no_database()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Handle NPC creation command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Test handle_npc_create_command() with no arguments.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_create_command() with invalid NPC type.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_create_command() when database is not available.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`

## Relationships

- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [combat attack handler](combat_attack_handler.md) (2 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (1 shared connections)
- [npc commands admin](npc_commands_admin.md) (1 shared connections)
- [item models rationale](item_models_rationale.md) (1 shared connections)
- [container schemas containers](container_schemas_containers.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/definition.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 18 (72%)
- INFERRED: 7 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*