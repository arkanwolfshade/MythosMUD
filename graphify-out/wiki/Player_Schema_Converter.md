# Player Schema Converter

> 39 nodes

## Key Concepts

- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **__init__.py** (24 connections) — `server/commands/npc_admin/__init__.py`
- **npc_admin_commands.py** (21 connections) — `server/commands/npc_admin_commands.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_command()** (17 connections) — `server/commands/npc_admin/router.py`
- **behavior.py** (11 connections) — `server/commands/npc_admin/behavior.py`
- **monitoring.py** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_behavior_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_react_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_stop_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_population_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_zone_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_status_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **validate_npc_admin_permission()** (9 connections) — `server/commands/npc_admin/router.py`
- **_resolve_npc_command_player()** (5 connections) — `server/commands/npc_admin/router.py`
- **Any** (5 connections)
- **_extract_npc_subcommand()** (5 connections) — `server/commands/npc_admin/router.py`
- **_invoke_npc_handler()** (5 connections) — `server/commands/npc_admin/router.py`
- **_get_npc_help()** (4 connections) — `server/commands/npc_admin/router.py`
- **Any** (3 connections)
- **Any** (3 connections)
- **NPC Admin Commands subpackage for MythosMUD.  Splits NPC admin functionality acr** (1 connections) — `server/commands/npc_admin/__init__.py`
- **NPC behavior control commands (behavior, react, stop).** (1 connections) — `server/commands/npc_admin/behavior.py`
- **Handle NPC behavior control command.** (1 connections) — `server/commands/npc_admin/behavior.py`
- **Handle NPC reaction trigger command.** (1 connections) — `server/commands/npc_admin/behavior.py`
- *... and 14 more nodes in this community*

## Relationships

- [Player Name Validation](Player_Name_Validation.md) (17 shared connections)
- [Death Delirium UI Modals](Death_Delirium_UI_Modals.md) (17 shared connections)
- [Client Event Store](Client_Event_Store.md) (17 shared connections)
- [Player Respawn Handlers](Player_Respawn_Handlers.md) (11 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (10 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (6 shared connections)
- [NPC Occupants Verification](NPC_Occupants_Verification.md) (5 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 211 (86%)
- INFERRED: 34 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*