# commands npc admin

> 195 nodes

## Key Concepts

- **AliasStorage** (283 connections) — `server/alias_storage.py`
- **alias_storage.py** (75 connections) — `server/alias_storage.py`
- **test_alias_storage.py** (67 connections) — `server/tests/unit/test_alias_storage.py`
- **Path** (11 connections)
- **.get_player_aliases()** (10 connections) — `server/alias_storage.py`
- **._load_alias_data()** (9 connections) — `server/alias_storage.py`
- **.get_alias_file_path()** (7 connections) — `server/alias_storage.py`
- **._save_alias_data()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **Path** (6 connections)
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **Any** (6 connections)
- **alias_storage()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **AliasPayload** (5 connections)
- **_apply_alias_timestamps()** (5 connections) — `server/alias_storage.py`
- **._resolved_alias_open_path()** (5 connections) — `server/alias_storage.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **test_alias_storage_init_with_env_var()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **MonkeyPatch** (5 connections)
- **test_delete_player_aliases_io_error()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_io_error()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- *... and 170 more nodes in this community*

## Relationships

- [alias models rationale](alias_models_rationale.md) (31 shared connections)
- [tick game processing](tick_game_processing.md) (26 shared connections)
- [command commands handler](command_commands_handler.md) (17 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (15 shared connections)
- [commands admin mute](commands_admin_mute.md) (13 shared connections)
- [character creation service](character_creation_service.md) (11 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (11 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (9 shared connections)
- [shutdown commands admin](shutdown_commands_admin.md) (8 shared connections)
- [zone configuration npc](zone_configuration_npc.md) (8 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (7 shared connections)
- [realtime real time](realtime_real_time.md) (7 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/combat_handler.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 889 (97%)
- INFERRED: 27 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*