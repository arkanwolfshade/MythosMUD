# commands party examples

> 39 nodes

## Key Concepts

- **AliasStorage** (231 connections) — `server/alias_storage.py`
- **._get_alias_file_path()** (8 connections) — `server/alias_storage.py`
- **.get_player_aliases()** (8 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **._load_alias_data()** (6 connections) — `server/alias_storage.py`
- **._save_alias_data()** (6 connections) — `server/alias_storage.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **Path** (4 connections)
- **.remove_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias_count()** (4 connections) — `server/alias_storage.py`
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- **Any** (3 connections)
- **.clear_aliases()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_name()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_command()** (3 connections) — `server/alias_storage.py`
- **.delete_player_aliases()** (3 connections) — `server/alias_storage.py`
- **.__init__()** (2 connections) — `server/alias_storage.py`
- **.list_alias_files()** (2 connections) — `server/alias_storage.py`
- **Manages player alias storage in JSON files.      Each player's aliases are store** (1 connections) — `server/alias_storage.py`
- **Get the file path for a player's aliases.          Human: reject path separators** (1 connections) — `server/alias_storage.py`
- **Load alias data from JSON file.** (1 connections) — `server/alias_storage.py`
- **Save alias data to JSON file.** (1 connections) — `server/alias_storage.py`
- *... and 14 more nodes in this community*

## Relationships

- [commands npc admin](commands_npc_admin.md) (21 shared connections)
- [command commands handler](command_commands_handler.md) (16 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (14 shared connections)
- [commands admin mute](commands_admin_mute.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (7 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (7 shared connections)
- [realtime real time](realtime_real_time.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [position player service](position_player_service.md) (6 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (5 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (5 shared connections)

## Source Files

- `server/alias_storage.py`

## Audit Trail

- EXTRACTED: 321 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*