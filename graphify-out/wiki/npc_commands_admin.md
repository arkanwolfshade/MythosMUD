# npc commands admin

> 29 nodes

## Key Concepts

- **__init__.py** (24 connections) — `server/commands/npc_admin/__init__.py`
- **instance.py** (22 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_spawn_command()** (13 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_despawn_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (10 connections) — `server/commands/npc_admin/instance.py`
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
- **NPC Admin Commands subpackage for MythosMUD.  Splits NPC admin functionality acr** (1 connections) — `server/commands/npc_admin/__init__.py`
- **NPC instance management commands (spawn, despawn, move, stats).** (1 connections) — `server/commands/npc_admin/instance.py`
- **npc' means current location; return None to resolve from player.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse numeric definition_id case. Returns (definition_id, room_id) or None if no** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse name-based spawn. Returns (npc_name, quantity, room_id).** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse args for npc spawn. Returns (definition_id, npc_name, quantity, room_id, e** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve NPC definition ID by name. Returns None if not found.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve room_id from player's current room when room_id is None. Returns (room_i** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve definition_id, room_id, and quantity for spawn. Returns (definition_id,** (1 connections) — `server/commands/npc_admin/instance.py`
- **Run the spawn loop and return result message or error.** (1 connections) — `server/commands/npc_admin/instance.py`
- *... and 4 more nodes in this community*

## Relationships

- [combat attack handler](combat_attack_handler.md) (14 shared connections)
- [container schemas containers](container_schemas_containers.md) (8 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (7 shared connections)
- [commands npc admin](commands_npc_admin.md) (7 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (6 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [help content websocket](help_content_websocket.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/instance.py`

## Audit Trail

- EXTRACTED: 135 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*