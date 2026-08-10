# Player Name Validation

> 26 nodes

## Key Concepts

- **definition.py** (16 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_create_command()** (12 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_edit_command()** (10 connections) — `server/commands/npc_admin/definition.py`
- **NPCDefinitionType** (10 connections) — `server/models/npc.py`
- **handle_npc_delete_command()** (9 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (9 connections) — `server/commands/npc_admin/definition.py`
- **Any** (7 connections)
- **_parse_npc_edit_args()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_build_npc_edit_params()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_execute_npc_edit()** (5 connections) — `server/commands/npc_admin/definition.py`
- **test_handle_npc_delete_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
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
- **StrEnum** (1 connections)
- **Enumeration of valid NPC definition types.** (1 connections) — `server/models/npc.py`
- **Test handle_npc_delete_command() with no arguments.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_create_command() with invalid NPC type.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- *... and 1 more nodes in this community*

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (17 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Player Respawn Handlers](Player_Respawn_Handlers.md) (5 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/definition.py`
- `server/models/npc.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 98 (89%)
- INFERRED: 12 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*