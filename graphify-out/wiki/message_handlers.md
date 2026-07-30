# message handlers

> 20 nodes

## Key Concepts

- **definition.py** (16 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_create_command()** (12 connections) — `server/commands/npc_admin/definition.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **handle_npc_edit_command()** (10 connections) — `server/commands/npc_admin/definition.py`
- **NPCDefinitionType** (10 connections) — `server/models/npc.py`
- **handle_npc_delete_command()** (9 connections) — `server/commands/npc_admin/definition.py`
- **Any** (7 connections)
- **_parse_npc_edit_args()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_build_npc_edit_params()** (5 connections) — `server/commands/npc_admin/definition.py`
- **_execute_npc_edit()** (5 connections) — `server/commands/npc_admin/definition.py`
- **NPC definition management commands (create, edit, delete, list).** (1 connections) — `server/commands/npc_admin/definition.py`
- **Parse and validate NPC edit command args.      Returns:         (npc_id, field,** (1 connections) — `server/commands/npc_admin/definition.py`
- **Map a single NPC field/value into NPCDefinitionUpdateParams, or return an error** (1 connections) — `server/commands/npc_admin/definition.py`
- **Run NPC definition update in DB session. Returns result or error dict.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC creation command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC editing command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **Handle NPC deletion command.** (1 connections) — `server/commands/npc_admin/definition.py`
- **StrEnum** (1 connections)
- **Enumeration of valid NPC definition types.** (1 connections) — `server/models/npc.py`
- **Internal params for NPC definition update data builder.** (1 connections) — `server/services/npc_service_models.py`

## Relationships

- [Any](Any.md) (15 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (9 shared connections)
- [test magic commands](test_magic_commands.md) (4 shared connections)
- [NATSMetrics](NATSMetrics.md) (4 shared connections)
- [metrics](metrics.md) (3 shared connections)
- [test mp regeneration service](test_mp_regeneration_service.md) (2 shared connections)
- [AuthSlice](AuthSlice.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [. repr ()](_repr_%28%29.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/definition.py`
- `server/models/npc.py`
- `server/services/npc_service_models.py`

## Audit Trail

- EXTRACTED: 93 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*