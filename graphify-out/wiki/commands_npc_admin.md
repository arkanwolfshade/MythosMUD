# commands npc admin

> 198 nodes

## Key Concepts

- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **test_npc_admin_commands.py** (54 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **__init__.py** (24 connections) — `server/commands/npc_admin/__init__.py`
- **instance.py** (22 connections) — `server/commands/npc_admin/instance.py`
- **npc_admin_commands.py** (21 connections) — `server/commands/npc_admin_commands.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **definition.py** (16 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_command()** (16 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_behavior_command()** (14 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_create_command()** (14 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_spawn_command()** (14 connections) — `server/commands/npc_admin/instance.py`
- **test_occupants.py** (14 connections) — `server/commands/npc_admin/test_occupants.py`
- **handle_npc_edit_command()** (13 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_test_occupants_command()** (13 connections) — `server/commands/npc_admin/test_occupants.py`
- **handle_npc_react_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_stop_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **behavior.py** (11 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_delete_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_despawn_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **monitoring.py** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_population_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_zone_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- *... and 173 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (36 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (23 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (12 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (6 shared connections)
- [room look commands](room_look_commands.md) (4 shared connections)
- [profession models rationale](profession_models_rationale.md) (4 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (4 shared connections)
- [command models moderation](command_models_moderation.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (3 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (3 shared connections)
- [schemas players profession](schemas_players_profession.md) (3 shared connections)

## Source Files

- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/definition.py`
- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin/test_occupants.py`
- `server/commands/npc_admin_commands.py`
- `server/models/npc.py`
- `server/npc/aggressive_mob_npc.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 811 (91%)
- INFERRED: 77 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*