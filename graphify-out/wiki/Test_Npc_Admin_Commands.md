# Test Npc Admin Commands

> 172 nodes

## Key Concepts

- **AliasStorage** (235 connections) — `server/alias_storage.py`
- **get_npc_instance_service()** (70 connections) — `server/services/npc_instance_service.py`
- **test_npc_admin_commands.py** (55 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **asyncio** (41 connections)
- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **npc_admin/__init__.py** (25 connections) — `server/commands/npc_admin/__init__.py`
- **instance.py** (23 connections) — `server/commands/npc_admin/instance.py`
- **npc_admin_commands.py** (22 connections) — `server/commands/npc_admin_commands.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **definition.py** (17 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_command()** (16 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_behavior_command()** (14 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_create_command()** (14 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_spawn_command()** (14 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_edit_command()** (13 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_test_occupants_command()** (13 connections) — `server/commands/npc_admin/test_occupants.py`
- **handle_npc_react_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_stop_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_delete_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_despawn_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_population_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_status_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_zone_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- *... and 147 more nodes in this community*

## Relationships

- [Command Aliases Storage](Command_Aliases_Storage.md) (57 shared connections)
- [Alias Storage](Alias_Storage.md) (25 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (14 shared connections)
- [Test Magic Commands](Test_Magic_Commands.md) (12 shared connections)
- [Test Admin Commands](Test_Admin_Commands.md) (11 shared connections)
- [Npc Admin](Npc_Admin.md) (10 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (10 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (8 shared connections)
- [Combat Loader](Combat_Loader.md) (7 shared connections)
- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (7 shared connections)
- [Test Lucidity Recovery Commands](Test_Lucidity_Recovery_Commands.md) (7 shared connections)
- [Test Occupants](Test_Occupants.md) (7 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/definition.py`
- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin/test_occupants.py`
- `server/commands/npc_admin_commands.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 606 (86%)
- INFERRED: 102 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*