# AliasStorage

> 247 nodes

## Key Concepts

- **AliasStorage** (264 connections) — `server/alias_storage.py`
- **Alias** (70 connections) — `server/models/alias.py`
- **test_alias_storage.py** (68 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias.py** (30 connections) — `server/tests/unit/models/test_alias.py`
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
- *... and 222 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (22 shared connections)
- [command_service.py](command_service.py.md) (13 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (12 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (11 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (11 shared connections)
- [alias_storage.py](alias_storage.py.md) (11 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (8 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [position_commands.py](position_commands.py.md) (6 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (4 shared connections)
- [get_username_from_user](get_username_from_user.md) (4 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/models/alias.py`
- `server/tests/unit/models/test_alias.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 476 (78%)
- INFERRED: 131 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*