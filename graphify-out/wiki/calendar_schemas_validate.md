# calendar schemas validate

> 25 nodes

## Key Concepts

- **definition.py** (16 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_create_command()** (12 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_edit_command()** (10 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_delete_command()** (9 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (9 connections) — `server/commands/npc_admin/definition.py`
- **Any** (7 connections)
- **_parse_npc_edit_args()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_build_npc_edit_params()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_execute_npc_edit()** (5 connections) — `server/commands/npc_admin/definition.py`
- **test_handle_npc_create_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_list_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_create_command_invalid_type()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_create_command_no_database()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **NPC definition management commands (create, edit, delete, list).** (1 connections) — `server/commands/npc_admin/definition.py`
- **Parse and validate NPC edit command args.      Returns:         (npc_id, field,** (1 connections) — `server/commands/npc_admin/definition.py`
- **Map a single NPC field/value into NPCDefinitionUpdateParams, or return an error** (1 connections) — `server/commands/npc_admin/definition.py`
- **Run NPC definition update in DB session. Returns result or error dict.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC creation command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC editing command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC deletion command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC listing command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Test handle_npc_create_command() with no arguments.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_list_command() lists NPCs.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_create_command() with invalid NPC type.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_create_command() when database is not available.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`

## Relationships

- [commands npc admin](commands_npc_admin.md) (17 shared connections)
- [commands admin mute](commands_admin_mute.md) (6 shared connections)
- [nats services metrics](nats_services_metrics.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [combat commands handler](combat_commands_handler.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/definition.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 89 (87%)
- INFERRED: 13 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*