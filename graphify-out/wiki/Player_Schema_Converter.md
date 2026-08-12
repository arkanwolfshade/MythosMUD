# Player Schema Converter

> 194 nodes

## Key Concepts

- **AliasStorage** (230 connections) — `server/alias_storage.py`
- **alias_storage.py** (64 connections) — `server/alias_storage.py`
- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **__init__.py** (24 connections) — `server/commands/npc_admin/__init__.py`
- **test_npc_admin_commands.py** (23 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **instance.py** (22 connections) — `server/commands/npc_admin/instance.py`
- **npc_admin_commands.py** (21 connections) — `server/commands/npc_admin_commands.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_command()** (17 connections) — `server/commands/npc_admin/router.py`
- **alias_expansion.py** (16 connections) — `server/command_handler/alias_expansion.py`
- **definition.py** (16 connections) — `server/commands/npc_admin/definition.py`
- **test_occupants.py** (14 connections) — `server/commands/npc_admin/test_occupants.py`
- **handle_npc_spawn_command()** (13 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_create_command()** (12 connections) — `server/commands/npc_admin/definition.py`
- **behavior.py** (11 connections) — `server/commands/npc_admin/behavior.py`
- **monitoring.py** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_test_occupants_command()** (11 connections) — `server/commands/npc_admin/test_occupants.py`
- **handle_npc_edit_command()** (10 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_despawn_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_stats_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **NPCDefinitionType** (10 connections) — `server/models/npc.py`
- **handle_npc_behavior_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_react_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_stop_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- *... and 169 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (39 shared connections)
- [Container Open Events](Container_Open_Events.md) (24 shared connections)
- [Room Exploration API](Room_Exploration_API.md) (15 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (15 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (15 shared connections)
- [Alias Storage Services](Alias_Storage_Services.md) (11 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (11 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (10 shared connections)
- [Character Creation API](Character_Creation_API.md) (8 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (8 shared connections)
- [Communication Command Handlers](Communication_Command_Handlers.md) (7 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (7 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/command_handler/alias_expansion.py`
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
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 977 (91%)
- INFERRED: 102 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*