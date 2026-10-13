# Community 523

> 33 nodes

## Key Concepts

- **get_npc_instance_service()** (78 connections) — `server/services/npc_instance_service.py`
- **instance.py** (23 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_spawn_command()** (14 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_despawn_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_stats_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_params()** (7 connections) — `server/commands/npc_admin/instance.py`
- **Any** (6 connections)
- **_parse_npc_spawn_args()** (5 connections) — `server/commands/npc_admin/instance.py`
- **_execute_spawn_loop()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_normalize_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_numeric()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_definition_id_from_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **test_get_npc_instance_service_not_initialized()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **test_get_npc_instance_service_success()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPC instance management commands (spawn, despawn, move, stats).** (1 connections) — `server/commands/npc_admin/instance.py`
- **Run the spawn loop and return result message or error.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Handle NPC spawning command. Supports definition_id or name; room_id defaults…** (1 connections) — `server/commands/npc_admin/instance.py`
- **npc' means current location; return None to resolve from player.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Handle NPC despawning command.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Handle NPC movement command.** (1 connections) — `server/commands/npc_admin/instance.py`
- **Parse numeric definition_id case. Returns (definition_id, room_id) or None if…** (1 connections) — `server/commands/npc_admin/instance.py`
- **Handle NPC stats command.** (1 connections) — `server/commands/npc_admin/instance.py`
- *... and 8 more nodes in this community*

## Relationships

- [Community 275](Community_275.md) (25 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (14 shared connections)
- [Community 157](Community_157.md) (9 shared connections)
- [Community 449](Community_449.md) (6 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (5 shared connections)
- [Community 77](Community_77.md) (5 shared connections)
- [Community 213](Community_213.md) (4 shared connections)
- [Community 204](Community_204.md) (4 shared connections)
- [Community 74](Community_74.md) (3 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (3 shared connections)
- [Community 103](Community_103.md) (3 shared connections)
- [Magic & Tick Services](Magic_&_Tick_Services.md) (2 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 148 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*