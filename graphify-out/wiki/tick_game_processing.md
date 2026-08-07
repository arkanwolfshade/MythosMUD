# tick game processing

> 177 nodes

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
- **handle_npc_edit_command()** (13 connections) — `server/commands/npc_admin/definition.py`
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
- **handle_npc_status_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **NPCDefinitionType** (11 connections) — `server/models/npc.py`
- *... and 152 more nodes in this community*

## Relationships

- [commands npc admin](commands_npc_admin.md) (26 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (13 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (12 shared connections)
- [Error Conversion](Error_Conversion.md) (11 shared connections)
- [instance game manager](instance_game_manager.md) (7 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (5 shared connections)
- [room look commands](room_look_commands.md) (4 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (4 shared connections)
- [command player state](command_player_state.md) (4 shared connections)
- [command models moderation](command_models_moderation.md) (4 shared connections)
- [commands inventory command](commands_inventory_command.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/definition.py`
- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin_commands.py`
- `server/models/npc.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 732 (91%)
- INFERRED: 69 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*