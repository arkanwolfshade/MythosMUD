# Admin Set Lucidity Command

> 15 nodes · cohesion 0.02

## Key Concepts

- **AliasStorage** (132 connections) — `server/alias_storage.py`
- **alias_storage.py** (64 connections) — `server/alias_storage.py`
- **Any** (25 connections) — `server/commands/magic_commands.py`
- **Any** (16 connections) — `server/commands/admin_mute_commands.py`
- **Any** (12 connections) — `server/commands/admin_setlucidity_command.py`
- **Any** (10 connections) — `server/commands/admin_summon_command.py`
- **UUID** (6 connections) — `server/commands/admin_setlucidity_command.py`
- **Any** (4 connections) — `server/commands/channel_commands.py`
- **Any** (4 connections) — `server/commands/position_commands.py`
- **Any** (3 connections) — `server/commands/admin_commands.py`
- **.list_alias_files()** (2 connections) — `server/alias_storage.py`
- **Alias storage utilities for MythosMUD.  As noted in the restricted archives of M** (1 connections) — `server/alias_storage.py`
- **List all alias files in the storage directory.** (1 connections) — `server/alias_storage.py`
- **Manages player alias storage in JSON files.      Each player's aliases are store** (1 connections) — `server/alias_storage.py`
- **CommandResponse** (1 connections) — `server/commands/inventory_commands.py`

## Relationships

- [Server Config Loading](Server_Config_Loading.md) (22 shared connections)
- [Command Request App State](Command_Request_App_State.md) (7 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (1 shared connections)
- [Cursor Plans Uvicorn](Cursor_Plans_Uvicorn.md) (1 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)
- [Spellbook Read Command](Spellbook_Read_Command.md) (1 shared connections)
- [Room Planning Archive](Room_Planning_Archive.md) (1 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/admin_setlucidity_command.py`
- `server/commands/admin_summon_command.py`
- `server/commands/channel_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/magic_commands.py`
- `server/commands/position_commands.py`

## Audit Trail

- EXTRACTED: 228 (81%)
- INFERRED: 54 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*