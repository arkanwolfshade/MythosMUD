# commands rescue rationale

> 25 nodes

## Key Concepts

- **instance.py** (22 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_spawn_command()** (13 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_despawn_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_params()** (7 connections) — `server/commands/npc_admin/instance.py`
- **Any** (6 connections)
- **_parse_npc_spawn_args()** (5 connections) — `server/commands/npc_admin/instance.py`
- **_normalize_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_numeric()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_definition_id_from_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_execute_spawn_loop()** (4 connections) — `server/commands/npc_admin/instance.py`
- **test_handle_npc_spawn_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
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
- **Handle NPC despawning command.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Test handle_npc_spawn_command() with no arguments.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`

## Relationships

- [commands npc admin](commands_npc_admin.md) (16 shared connections)
- [commands admin mute](commands_admin_mute.md) (4 shared connections)
- [nats services metrics](nats_services_metrics.md) (4 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 95 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*