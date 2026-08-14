# AliasStorage

> God node · 271 connections · `server/alias_storage.py`

**Community:** [AliasStorage](AliasStorage.md)

## Connections by Relation

### calls
- _websocket_unified_command_result() `EXTRACTED`
- .delete_player() `EXTRACTED`
- test_alias_storage_init_with_env_var() `EXTRACTED`
- test_alias_storage_creates_directory() `EXTRACTED`
- test_alias_storage_init_with_storage_dir() `EXTRACTED`
- test_alias_storage_init_without_env_var() `EXTRACTED`

### contains
- alias_storage.py `EXTRACTED`

### imports
- command_service.py `EXTRACTED`
- test_alias_storage.py `EXTRACTED`
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) `EXTRACTED`
- [command_handler_unified.py](command_handler_unified.py.md) `EXTRACTED`
- combat_handler.py `EXTRACTED`
- [inventory_equip_command.py](inventory_equip_command.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- [admin_teleport_commands.py](admin_teleport_commands.py.md) `EXTRACTED`
- [quest_commands.py](quest_commands.py.md) `EXTRACTED`
- [look_command.py](look_command.py.md) `EXTRACTED`
- [admin_shutdown_command.py](admin_shutdown_command.py.md) `EXTRACTED`
- admin_summon_command.py `EXTRACTED`
- [inventory_pickup_command.py](inventory_pickup_command.py.md) `EXTRACTED`
- admin_commands.py `EXTRACTED`
- inventory_unequip_command.py `EXTRACTED`
- [rescue_commands.py](rescue_commands.py.md) `EXTRACTED`
- combat_taunt.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`
- admin_setlucidity_command.py `EXTRACTED`
- communication_commands.py `EXTRACTED`

### method
- .get_player_aliases() `EXTRACTED`
- .get_alias_file_path() `EXTRACTED`
- ._load_alias_data() `EXTRACTED`
- ._save_alias_data() `EXTRACTED`
- .save_player_aliases() `EXTRACTED`
- .create_alias() `EXTRACTED`
- ._validate_alias_payload() `EXTRACTED`
- .add_alias() `EXTRACTED`
- .remove_alias() `EXTRACTED`
- .get_alias() `EXTRACTED`
- .get_alias_count() `EXTRACTED`
- .backup_aliases() `EXTRACTED`
- ._resolved_alias_open_path() `EXTRACTED`
- .clear_aliases() `EXTRACTED`
- .validate_alias_name() `EXTRACTED`
- .validate_alias_command() `EXTRACTED`
- .delete_player_aliases() `EXTRACTED`
- .__init__() `EXTRACTED`
- .list_alias_files() `EXTRACTED`

### rationale_for
- Manages player alias storage in JSON files. Each player's aliases are stored in… `EXTRACTED`

### references
- _handle_admin_set_stat_command() `EXTRACTED`
- handle_teleport_command() `EXTRACTED`
- handle_ground_command() `EXTRACTED`
- handle_alias_command() `EXTRACTED`
- handle_logout_command() `EXTRACTED`
- handle_read_command() `EXTRACTED`
- _prepare_command_for_processing() `EXTRACTED`
- handle_pray_command() `EXTRACTED`
- handle_party_command() `EXTRACTED`
- handle_rest_command() `EXTRACTED`
- handle_goto_command() `EXTRACTED`
- handle_whisper_command() `EXTRACTED`
- handle_go_command() `EXTRACTED`
- handle_quest_command() `EXTRACTED`
- _process_alias_expansion() `EXTRACTED`
- process_command_unified() `EXTRACTED`
- handle_debrief_command() `EXTRACTED`
- handle_teach_command() `EXTRACTED`
- handle_mute_command() `EXTRACTED`
- handle_unequip_command() `EXTRACTED`

### uses
- [CombatCommandHandler](CombatCommandHandler.md) `INFERRED`
- MagicCommandHandler `INFERRED`
- [TestHelperFunctions](TestHelperFunctions.md) `INFERRED`
- TauntCommandHandler `INFERRED`
- [SchemaValidator](SchemaValidator.md) `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- _NpcWithLife `INFERRED`
- SpellCommandError `INFERRED`
- [CommandRequest](CommandRequest.md) `INFERRED`
- TestHandleSpecialCommandRouting `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*