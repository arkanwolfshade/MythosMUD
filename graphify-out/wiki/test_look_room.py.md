# test_look_room.py

> 86 nodes

## Key Concepts

- **get_npc_instance_service()** (64 connections) — `server/services/npc_instance_service.py`
- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **npc_admin/__init__.py** (25 connections) — `server/commands/npc_admin/__init__.py`
- **instance.py** (23 connections) — `server/commands/npc_admin/instance.py`
- **npc_admin_commands.py** (22 connections) — `server/commands/npc_admin_commands.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_command()** (17 connections) — `server/commands/npc_admin/router.py`
- **definition.py** (17 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_behavior_command()** (14 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_create_command()** (14 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_spawn_command()** (14 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_edit_command()** (13 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_react_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_stop_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **NPCDefinitionType** (11 connections) — `server/models/npc.py`
- **handle_npc_delete_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_despawn_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_population_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_status_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_zone_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **behavior.py** (11 connections) — `server/commands/npc_admin/behavior.py`
- **npc_admin/monitoring.py** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_stats_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- *... and 61 more nodes in this community*

## Relationships

- [HealthStatus](HealthStatus.md) (51 shared connections)
- [CombatParticipant](CombatParticipant.md) (21 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (18 shared connections)
- [NPCDefinition](NPCDefinition.md) (13 shared connections)
- [maps.py](maps.py.md) (10 shared connections)
- [factory](factory.md) (5 shared connections)
- [RoomLoader](RoomLoader.md) (5 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [Stats](Stats.md) (4 shared connections)
- [mock_connection_manager](mock_connection_manager.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)

## Source Files

- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/definition.py`
- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin_commands.py`
- `server/models/npc.py`
- `server/services/npc_instance_service.py`

## Audit Trail

- EXTRACTED: 326 (91%)
- INFERRED: 32 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*