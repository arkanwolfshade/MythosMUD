# AliasStorage

> 175 nodes

## Key Concepts

- **AliasStorage** (264 connections) — `server/alias_storage.py`
- **test_alias_storage.py** (68 connections) — `server/tests/unit/test_alias_storage.py`
- **Path** (11 connections)
- **.get_player_aliases()** (10 connections) — `server/alias_storage.py`
- **.get_alias_file_path()** (9 connections) — `server/alias_storage.py`
- **._load_alias_data()** (9 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **._save_alias_data()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **alias_storage()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **Path** (6 connections)
- **test_alias_storage_init_with_env_var()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_io_error()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_delete_player_aliases_io_error()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **AliasPayload** (5 connections)
- **MonkeyPatch** (5 connections)
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias_count()** (4 connections) — `server/alias_storage.py`
- **.remove_alias()** (4 connections) — `server/alias_storage.py`
- **_as_alias_payload()** (4 connections) — `server/alias_storage.py`
- **_get_alias_validator()** (4 connections) — `server/alias_storage.py`
- *... and 150 more nodes in this community*

## Relationships

- [Alias](Alias.md) (29 shared connections)
- [test_npc_admin_commands.py](test_npc_admin_commands.py.md) (19 shared connections)
- [command_service.py](command_service.py.md) (12 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (12 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (9 shared connections)
- [alias_storage.py](alias_storage.py.md) (9 shared connections)
- [combat_loader.py](combat_loader.py.md) (7 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (7 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (6 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (6 shared connections)
- [position_commands.py](position_commands.py.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 400 (80%)
- INFERRED: 103 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*