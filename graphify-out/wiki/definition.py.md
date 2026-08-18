# definition.py

> 18 nodes

## Key Concepts

- **definition.py** (17 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_edit_command()** (13 connections) — `server/commands/npc_admin/definition.py`
- **NPCDefinitionType** (11 connections) — `server/models/npc.py`
- **Any** (7 connections)
- **_build_npc_edit_params()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_execute_npc_edit()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_parse_npc_edit_args()** (5 connections) — `server/commands/npc_admin/definition.py`
- **test_handle_npc_edit_command_invalid_id()** (4 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_edit_command_success()** (4 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **StrEnum** (1 connections)
- **NPC definition management commands (create, edit, delete, list).** (1 connections) — `server/commands/npc_admin/definition.py`
- **Parse and validate NPC edit command args. Returns: (npc_id, field, value) on…** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC editing command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Map a single NPC field/value into NPCDefinitionUpdateParams, or return an error…** (1 connections) — `server/commands/npc_admin/definition.py`
- **Run NPC definition update in DB session. Returns result or error dict.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Enumeration of valid NPC definition types.** (1 connections) — `server/models/npc.py`
- **Test handle_npc_edit_command() rejects non-numeric ids.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_edit_command() updates definition field.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (17 shared connections)
- [npc_service/__init__.py](npc_service-__init__.py.md) (4 shared connections)
- [test_npc_definitions_api.py](test_npc_definitions_api.py.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [models/player.py](models-player.py.md) (1 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/definition.py`
- `server/models/npc.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 55 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*