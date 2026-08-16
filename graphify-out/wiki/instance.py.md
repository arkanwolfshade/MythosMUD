# instance.py

> 18 nodes

## Key Concepts

- **instance.py** (23 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_params()** (7 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_args()** (5 connections) — `server/commands/npc_admin/instance.py`
- **_execute_spawn_loop()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_normalize_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_numeric()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_definition_id_from_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **NPC instance management commands (spawn, despawn, move, stats).** (1 connections) — `server/commands/npc_admin/instance.py`
- **Run the spawn loop and return result message or error.** (1 connections) — `server/commands/npc_admin/instance.py`
- **npc' means current location; return None to resolve from player.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse numeric definition_id case. Returns (definition_id, room_id) or None if…** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse name-based spawn. Returns (npc_name, quantity, room_id).** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse args for npc spawn. Returns (definition_id, npc_name, quantity, room_id,…** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve NPC definition ID by name. Returns None if not found.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve room_id from player's current room when room_id is None. Returns…** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve definition_id, room_id, and quantity for spawn. Returns (definition_id,…** (1 connections) — `server/commands/npc_admin/instance.py`

## Relationships

- [test_npc_admin_commands.py](test_npc_admin_commands.py.md) (9 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*