# Player Schema Converter

> 140 nodes

## Key Concepts

- **AliasStorage** (230 connections) — `server/alias_storage.py`
- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **__init__.py** (24 connections) — `server/commands/npc_admin/__init__.py`
- **test_npc_admin_commands.py** (23 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **instance.py** (22 connections) — `server/commands/npc_admin/instance.py`
- **npc_admin_commands.py** (21 connections) — `server/commands/npc_admin_commands.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_command()** (17 connections) — `server/commands/npc_admin/router.py`
- **definition.py** (16 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_spawn_command()** (13 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_create_command()** (12 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_test_occupants_command()** (11 connections) — `server/commands/npc_admin/test_occupants.py`
- **handle_npc_edit_command()** (10 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_despawn_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_stats_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **NPCDefinitionType** (10 connections) — `server/models/npc.py`
- **handle_npc_behavior_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_react_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_stop_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_delete_command()** (9 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (9 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_population_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_zone_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_status_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- *... and 115 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (37 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (17 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (16 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (16 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (14 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (14 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (11 shared connections)
- [NPC Occupants Verification](NPC_Occupants_Verification.md) (7 shared connections)
- [Alias Storage Services](Alias_Storage_Services.md) (7 shared connections)
- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (6 shared connections)
- [E2E Suite Overview](E2E_Suite_Overview.md) (5 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (5 shared connections)

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
- `server/models/npc.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 716 (88%)
- INFERRED: 98 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*