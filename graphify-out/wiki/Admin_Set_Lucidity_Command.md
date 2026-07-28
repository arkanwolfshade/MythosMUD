# Admin Set Lucidity Command

> 231 nodes · cohesion 0.02

## Key Concepts

- **AliasStorage** (230 connections) — `server/alias_storage.py`
- **command_service.py** (92 connections) — `server/commands/command_service.py`
- **.__init__()** (71 connections) — `server/commands/command_service.py`
- **alias_storage.py** (66 connections) — `server/alias_storage.py`
- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **MagicCommandHandler** (34 connections) — `server/commands/magic_commands.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **admin_setlucidity_command.py** (28 connections) — `server/commands/admin_setlucidity_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **lucidity_recovery_commands.py** (25 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_mute_command()** (20 connections) — `server/commands/admin_mute_commands.py`
- **Any** (20 connections)
- **position_commands.py** (19 connections) — `server/commands/position_commands.py`
- **Any** (16 connections)
- **channel_commands.py** (16 connections) — `server/commands/channel_commands.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **handle_admin_command()** (14 connections) — `server/commands/admin_commands.py`
- **handle_inventory_command()** (14 connections) — `server/commands/inventory_commands.py`
- **handle_unmute_command()** (13 connections) — `server/commands/admin_mute_commands.py`
- **handle_unalias_command()** (13 connections) — `server/commands/alias_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_add_admin_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- *... and 206 more nodes in this community*

## Relationships

- [Lucidity Recovery Commands](Lucidity_Recovery_Commands.md) (34 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (32 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (32 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (32 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (29 shared connections)
- [Health Check Models](Health_Check_Models.md) (28 shared connections)
- [Server Config Loading](Server_Config_Loading.md) (22 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (22 shared connections)
- [Alias Expansion Logic](Alias_Expansion_Logic.md) (22 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (18 shared connections)
- [Client Event Store](Client_Event_Store.md) (17 shared connections)
- [Command Request App State](Command_Request_App_State.md) (16 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/admin_setlucidity_command.py`
- `server/commands/admin_summon_command.py`
- `server/commands/alias_commands.py`
- `server/commands/channel_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/lucidity_recovery_commands.py`
- `server/commands/magic_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`

## Audit Trail

- EXTRACTED: 1451 (89%)
- INFERRED: 184 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*