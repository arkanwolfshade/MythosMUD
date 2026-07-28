# Server Commands (45)

> 27 nodes

## Key Concepts

- **instance.py** (22 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_spawn_command()** (13 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_stats_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_params()** (7 connections) — `server/commands/npc_admin/instance.py`
- **Any** (6 connections)
- **_parse_npc_spawn_args()** (5 connections) — `server/commands/npc_admin/instance.py`
- **_normalize_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_numeric()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_definition_id_from_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_execute_spawn_loop()** (4 connections) — `server/commands/npc_admin/instance.py`
- **test_handle_npc_spawn_command_name_not_found()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_spawn_command_name_success()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **NPC instance management commands (spawn, despawn, move, stats).** (1 connections) — `server/commands/npc_admin/instance.py`
- **npc' means current location; return None to resolve from player.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse numeric definition_id case. Returns (definition_id, room_id) or None if no** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse name-based spawn. Returns (npc_name, quantity, room_id).** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse args for npc spawn. Returns (definition_id, npc_name, quantity, room_id, e** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve NPC definition ID by name. Returns None if not found.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve room_id from player's current room when room_id is None. Returns (room_i** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve definition_id, room_id, and quantity for spawn. Returns (definition_id,** (1 connections) — `server/commands/npc_admin/instance.py`
- **Run the spawn loop and return result message or error.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Handle NPC spawning command. Supports definition_id or name; room_id defaults to** (1 connections) — `server/commands/npc_admin/instance.py`
- **Handle NPC stats command.** (1 connections) — `server/commands/npc_admin/instance.py`
- *... and 2 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (6 shared connections)
- [Server Commands (39)](Server_Commands_%2839%29.md) (6 shared connections)
- [Server Commands (75)](Server_Commands_%2875%29.md) (5 shared connections)
- [Server Npc](Server_Npc.md) (4 shared connections)
- [Server Commands (53)](Server_Commands_%2853%29.md) (3 shared connections)
- [Server Infrastructure (7)](Server_Infrastructure_%287%29.md) (3 shared connections)
- [Server Commands (40)](Server_Commands_%2840%29.md) (3 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 98 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*