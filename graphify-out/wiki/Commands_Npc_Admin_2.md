# Commands Npc Admin

> 22 nodes · cohesion 0.11

## Key Concepts

- **handle_npc_spawn_command()** (12 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_despawn_command()** (9 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (9 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_stats_command()** (9 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_params()** (7 connections) — `server/commands/npc_admin/instance.py`
- **Any** (6 connections) — `server/commands/npc_admin/instance.py`
- **_execute_spawn_loop()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **AliasStorage** (4 connections) — `server/commands/npc_admin/instance.py`
- **test_handle_npc_spawn_command_name_not_found()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_spawn_command_name_success()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_stats_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Handle NPC stats command.** (2 connections) — `server/commands/npc_admin/instance.py`
- **Test handle_npc_spawn_command() when NPC name is not found.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_spawn_command() with name-based spawn.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_stats_command() displays NPC stats.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Run the spawn loop and return result message or error.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Handle NPC spawning command. Supports definition_id or name; room_id defaults to** (1 connections) — `server/commands/npc_admin/instance.py`
- **Handle NPC despawning command.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Handle NPC movement command.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve room_id from player's current room when room_id is None. Returns (room_i** (1 connections) — `server/commands/npc_admin/instance.py`
- **Resolve definition_id, room_id, and quantity for spawn. Returns (definition_id,** (1 connections) — `server/commands/npc_admin/instance.py`

## Relationships

- [[Commands Npc Admin]] (10 shared connections)
- [[NPC Database Sessions]] (9 shared connections)
- [[NPC Admin Commands]] (9 shared connections)
- [[NPC Occupant Verification]] (4 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 75 (89%)
- INFERRED: 9 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
